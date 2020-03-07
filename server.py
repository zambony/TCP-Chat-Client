import socket
import json
import threading
import errno


class Server():
	"""A server class for receiving and dispatching chat messages, or general data.

	Attributes:
		socket (WrappedSocket): The socket the server is bound to
		hostname (str): The hostname of the server
		port (int): The port number for the server
		connections: Contains all client connections as a tuple of (connection, ip)
	"""
	socket = None
	hostname = ''
	port = 0
	connections = []

	def __init__(self, hostname, port):
		"""Initialize a server with specified hostname and port

		Args:
			hostname (str): The name of the host to connect to
			port (int): The port number to connect to
		"""
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.socket.bind((hostname, port))
		self.socket.listen(10)

		self.socket.setblocking(False)

		self.hostname = hostname
		self.port = port

		self.__connectionThread = threading.Thread(target = self.acceptconnections)
		self.__connectionThread.setDaemon(True)
		self.__connectionThread.start()

		self.__thread = threading.Thread(target = self.handle)
		self.__thread.setDaemon(True)
		self.__thread.start()

	def acceptconnections(self):
		while True:
			try:
				connection, address = self.socket.accept()

				for _, _address in self.connections:
					if (_address == address):
						connection.close()
						continue

				connection.setblocking(False)
				self.connections.append((connection, address))

				print(address)
			except:
				pass

	def handle(self):
		"""The main loop to handle all incoming message

		This method is run in a ``Thread`` and continues to check for
		messages from all connected clients.

		Will drop a connection the connection seems terminated.

		If a message is received, it is sent through ``onmessagereceived``
		"""
		while True:
			for client, address in self.connections:
				try:
					packet = client.recv(2048).strip()

					# If the packet is empty, just ignore it
					if (not packet):
						print("Dropped client for bad recv:", address)
						self.connections.remove((client, address))
						client.close()
						continue

					# Unpack the bytes
					packet = packet.decode('utf8')
					# print(packet)
					# Reconstruct the packet into usable code
					data = json.loads(packet)

					self.onmessagereceived(client, data["userName"], data["message"])
				except socket.error as e:
					err = e.args[0]

					if (err == errno.EAGAIN or err == errno.EWOULDBLOCK):
						continue
					elif (err == errno.EPIPE):
						print("PIPE ERROR")
						print("Dropped client:", address)
						self.connections.remove((client, address))
						client.close()
					else:
						print(e.args)
						print("Dropped client:", address)
						self.connections.remove((client, address))
						client.close()

	def broadcast(self, response):
		"""Encodes and sends a response to all connected clients.

		Responses should be JSON strings containing the keys 'userName' and 'message', and any
		other necessary data.

		Examples:
			>>> import json
			>>> broadcast(json.dumps({'userName': 'Alice','message': 'Hello, world'}))
			Sends a chat message from Alice containing the text 'Hello, world'

		Args:
			response (str): The JSON string to encode and send
		"""
		for client, address in self.connections:
			print(client, address)
			client.sendall(response.encode('utf8'))

	def onmessagereceived(self, sender, username, message):
		"""Event function for when a message is received from a client.

		Args:
			sender (WrappedSocket): The socket object of the client who sent the message
			username (str): The client's username
			message (str): The client's message
		"""
		if (len(message) == 0):
			return

		response = {'userName': username, 'message': message}

		if (message[0] == "/"):
			exploded = message.split(" ")
			command = exploded[0][1:]
			del exploded[0]

			if (command == "shrug"):
				response['message'] = ' '.join(exploded)
				response['append'] = " ¯\\_(ツ)_/¯"

		data = json.dumps(response)

		print(response)

		self.broadcast(data)
