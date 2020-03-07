from socket import *
import json
from PyQt5.QtCore import QThread, pyqtSignal


class Client(QThread):
	signal = pyqtSignal('PyQt_PyObject')
	onDeath = pyqtSignal()

	def __init__(self, userName = "Client"):
		super().__init__()
		self.socket = None
		self.__thread = None
		self.userName = userName
		self.hook = None

	def connect(self, address: str, port: int):
		host = gethostbyname(address)
		self.socket = socket(AF_INET, SOCK_STREAM)
		self.socket.connect((address, port))
		self.socket.setblocking(False)

	def disconnect(self):
		self.quit()
		self.socket.close()

	def sendMessage(self, message: str):
		packed = json.dumps({
			"userName": self.userName,
			"message": message
		})

		self.socket.sendall(packed.encode('utf8'))

	def run(self):
		while True:
			try:
				packet = self.socket.recv(2048)

				if (not packet):
					self.disconnect()
					self.onDeath.emit()

					break

				data = json.loads(packet.decode('utf8'))

				self.onMessageReceived(data)
			except:
				pass

	def onMessageReceived(self, messageInfo):
		self.signal.emit(messageInfo)
