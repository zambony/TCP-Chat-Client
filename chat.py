from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from client import Client
from server import Server
import mistune
import html
import datetime as dt
import configparser


class ChatClient(QtCore.QObject):
	kill = pyqtSignal()
	BGCol = QtGui.QColor(54, 57, 63)
	BorderCol = QtGui.QColor(47, 49, 54)
	EditableColor = QtGui.QColor(72, 75, 81)
	TextColor = QtGui.QColor(220, 221, 222)
	DockColor = QtGui.QColor(32, 34, 37)
	history = []
	server = None
	client = None
	Markdown = mistune.Markdown()
	config = configparser.ConfigParser(allow_no_value = True)

	def setupUi(self, MainWindow):
		### GENERATED CODE ###

		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(793, 591)
		dockIcon = QtGui.QIcon()
		dockIcon.addPixmap(QtGui.QPixmap(":/icons/biscord"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		MainWindow.setWindowIcon(dockIcon)

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
		self.verticalLayout.setObjectName("verticalLayout")

		self.chatLog = QtWidgets.QTextEdit(self.centralwidget)
		self.chatLog.setEnabled(True)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.chatLog.sizePolicy().hasHeightForWidth())
		self.chatLog.setSizePolicy(sizePolicy)
		self.chatLog.setAcceptDrops(False)
		self.chatLog.setAutoFillBackground(False)
		self.chatLog.setReadOnly(True)
		self.chatLog.setObjectName("chatLog")

		self.verticalLayout.addWidget(self.chatLog)

		self.inputBox = QtWidgets.QLineEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.inputBox.sizePolicy().hasHeightForWidth())
		self.inputBox.setSizePolicy(sizePolicy)
		self.inputBox.setMinimumSize(QtCore.QSize(0, 20))
		self.inputBox.setMaximumSize(QtCore.QSize(16777215, 40))
		self.inputBox.setText("")
		self.inputBox.setFrame(True)
		self.inputBox.setClearButtonEnabled(True)
		self.inputBox.setObjectName("inputBox")
		self.inputBox.setEnabled(False)

		self.verticalLayout.addWidget(self.inputBox)

		self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setSpacing(10)
		self.horizontalLayout.setObjectName("horizontalLayout")

		self.hostName = QtWidgets.QLineEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.hostName.sizePolicy().hasHeightForWidth())
		self.hostName.setSizePolicy(sizePolicy)
		self.hostName.setMaximumSize(QtCore.QSize(150, 20))
		self.hostName.setObjectName("hostName")

		self.horizontalLayout.addWidget(self.hostName)

		self.portNumber = QtWidgets.QSpinBox(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.portNumber.sizePolicy().hasHeightForWidth())
		self.portNumber.setSizePolicy(sizePolicy)
		self.portNumber.setMinimumSize(QtCore.QSize(62, 0))
		self.portNumber.setMaximumSize(QtCore.QSize(62, 0))
		self.portNumber.setObjectName("portNumber")
		self.portNumber.setMaximum(65535)

		self.horizontalLayout.addWidget(self.portNumber)

		self.userName = QtWidgets.QLineEdit(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.userName.sizePolicy().hasHeightForWidth())
		self.userName.setSizePolicy(sizePolicy)
		self.userName.setMaximumSize(QtCore.QSize(150, 20))
		self.userName.setObjectName("userName")

		self.horizontalLayout.addWidget(self.userName)

		spacerItem = QtWidgets.QSpacerItem(59, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem)

		self.connectServer = QtWidgets.QPushButton(self.centralwidget)
		self.connectServer.setToolTipDuration(-1)
		self.connectServer.setStatusTip("")
		self.connectServer.setWhatsThis("")
		self.connectServer.setText("")
		self.connectServer.setObjectName("connectServer")
		self.connectServer.setText("Connect")
		self.connectServer.setCursor(QtCore.Qt.PointingHandCursor)

		self.horizontalLayout.addWidget(self.connectServer)

		self.startServer = QtWidgets.QPushButton(self.centralwidget)
		self.startServer.setText("Start Server")
		self.startServer.setCursor(QtCore.Qt.PointingHandCursor)
		self.startServer.setObjectName("startServer")

		self.horizontalLayout.addWidget(self.startServer)

		self.disconnect = QtWidgets.QPushButton(self.centralwidget)
		self.disconnect.setText("Disconnect")
		self.disconnect.setCursor(QtCore.Qt.PointingHandCursor)
		self.disconnect.setObjectName("disconnect")
		self.disconnect.setProperty("dangerous", True)

		self.horizontalLayout.addWidget(self.disconnect)

		self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
		spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
		self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)

		### END GENERATED CODE ###

		self.hostName.setFocus(QtCore.Qt.PopupFocusReason)

		palette = self.chatLog.palette()
		palette.setColor(QtGui.QPalette.Base, self.BGCol)
		self.chatLog.setPalette(palette)
		self.chatLog.setFrameStyle(0)

		palette = self.inputBox.palette()
		palette.setColor(QtGui.QPalette.Text, self.TextColor)
		palette.setColor(QtGui.QPalette.Base, self.DockColor)
		self.inputBox.setPalette(palette)
		self.inputBox.setFrame(False)

		palette = self.hostName.palette()
		palette.setColor(QtGui.QPalette.Text, self.TextColor)
		palette.setColor(QtGui.QPalette.Base, self.EditableColor)
		self.hostName.setPalette(palette)
		self.hostName.setFrame(False)

		palette = self.portNumber.palette()
		palette.setColor(QtGui.QPalette.Text, self.TextColor)
		palette.setColor(QtGui.QPalette.Base, self.EditableColor)
		palette.setColor(QtGui.QPalette.Background, self.EditableColor)
		self.portNumber.setPalette(palette)
		self.portNumber.setFrame(False)

		palette = self.userName.palette()
		palette.setColor(QtGui.QPalette.Base, self.EditableColor)
		palette.setColor(QtGui.QPalette.Text, self.TextColor)
		self.userName.setPalette(palette)
		self.userName.setFrame(False)

		palette = MainWindow.palette()
		palette.setColor(QtGui.QPalette.Background, self.BorderCol)
		MainWindow.setPalette(palette)

		self.retranslateUi(MainWindow)

		self.config.read('config.ini')

		self.hostName.setText(self.config.get("CONNECTION", "hostName"))

		try:
			self.portNumber.setValue(self.config.getint("CONNECTION", "port"))
		except ValueError as e:
			print("Skipping port config value...")

		self.userName.setText(self.config.get("CONNECTION", "username"))

		# Connect all of our event hooks
		self.inputBox.returnPressed.connect(self.sendMessage)
		self.connectServer.clicked.connect(self.connectToServer)
		self.startServer.clicked.connect(self.createServer)
		self.disconnect.clicked.connect(self.disconnectFromServer)

	def log(self, text):
		QtWidgets.QApplication.processEvents()
		self.chatLog.append('<span style="color: #FBFCFC;">' + text + '</span>')

	def error(self, text):
		QtWidgets.QApplication.processEvents()
		self.chatLog.append('<span style="color: #E74C3C;">' + text + '</span>')

	def append(self, text):
		QtWidgets.QApplication.processEvents()
		self.chatLog.append('<span class="message">' + text + '</span>')

	def initialize(self):
		"""Executes after a connection is established"""
		self.setAllowInput(True)
		self.inputBox.setFocus(QtCore.Qt.OtherFocusReason)

	def sendMessage(self):
		"""Sends whatever is currently in the inputBox as a message to the host"""
		if (self.client):
			self.client.sendMessage(self.inputBox.text())

		self.inputBox.clear()

		# Due to some celestial reason, I have to call this or the chatbox won't update
		QtWidgets.QApplication.processEvents()

	def setAllowInput(self, bAllow: bool):
		if (bAllow):
			palette = self.inputBox.palette()
			palette.setColor(QtGui.QPalette.Base, self.EditableColor)
			self.inputBox.setPalette(palette)
			self.inputBox.setEnabled(True)
		else:
			palette = self.inputBox.palette()
			palette.setColor(QtGui.QPalette.Base, self.DockColor)
			self.inputBox.setPalette(palette)
			self.inputBox.setEnabled(False)

	def receive(self, messageInfo):
		"""Called whenever the client receives a data packet

		Appends the username and message to the chatLog

		Args:
			messageInfo: The JSON message data
		"""
		# If the data packet doesn't have a message field, ignore it
		if ('message' not in messageInfo):
			return

		message = messageInfo['message']
		message = html.escape(message)  # Escape any HTML the message contains
		message = self.Markdown(message)  # Parse markdown like discord
		message = message.replace("<p>", "")  # Remove shitty paragraph tags from the markdown parse
		message = message.replace("</p>", "")
		message = message.strip()  # delet spaces

		# Grab the 24hr timestamp and format it
		now = dt.datetime.now()
		hour, minute = now.hour, now.minute
		timestamp = f"{hour:02}:{minute:02}"

		# header contains the formatted username and timestamp on one line
		header = f"<span class=\"username\"><strong>{messageInfo['userName']}</strong></span>" \
			f"<span class=\"timestamp\">  {timestamp}</span><br>"

		# Weird pythonic ternary. Append is currently used for the /shrug command lol
		extra = messageInfo['append'] if 'append' in messageInfo else ''

		# output is the message + whatever appended text came in
		output = f"<span class=\"message\">" \
				 f"{message}{extra}" \
				 f"</span>"

		# Message grouping!
		# If our message history is greater than zero, and the last message was
		# sent by the same user as this new message, just append their message body.
		# Otherwise, insert a line break and append the full username, timestamp, and message.
		if (len(self.history) > 0 and self.history[-1]['userName'] == messageInfo['userName']):
			self.append(output)
		else:
			QtWidgets.QApplication.processEvents()
			self.chatLog.append('<br>' + header + output)

		# Add the unformatted message and username to our history list
		self.history.append({'userName': messageInfo['userName'], 'message': messageInfo['message'] + extra})

	def connectToServer(self):
		"""Connect to a host using whatever info is in the input fields"""
		if (self.client is not None):
			self.error("[ERROR] You are already connected to a session!")

			return

		try:
			self.client = Client(self.userName.text())
			self.client.connect(self.hostName.text(), self.portNumber.value())

			self.log("Connected")

			self.client.signal.connect(self.receive)  # Call self.receive when the client thread gets a message
			self.client.onDeath.connect(self.disconnectFromServer)
			self.kill.connect(self.client.disconnect)  # Disconnect our client socket when we fire the kill signal

			self.client.start()  # Start the client thread

			self.initialize()
		except:  # Bad practice but I give zero fucks because I don't care about specific errors
			self.client = None
			self.error("[ERROR] Critical error/host unresponsive, connection aborted")

	def createServer(self):
		"""Attempts to establish a server and join it using a client"""
		if (self.client is None and self.server is None):
			try:
				host = self.hostName.text()

				self.server = Server(host, self.portNumber.value())
				self.client = Client(self.userName.text())
				self.client.connect(host if host != '' else 'localhost', self.portNumber.value())

				self.log("Connected. You are the session host.")

				# Connect signals. See `connect_to_server` for more.
				self.client.signal.connect(self.receive)
				self.client.onDeath.connect(self.disconnectFromServer)
				self.kill.connect(self.client.disconnect)
				self.kill.connect(self.server.socket.close)

				self.client.start()

				self.initialize()
			except:  # ECKS-DEE
				self.server = None
				self.client = None

				self.error("[ERROR] Could not start server, aborting...")
		else:
			self.error("[ERROR] You are already connected to a session!")

	def disconnectFromServer(self):
		"""Disconnects from the server. If it is a listen server it will be shutdown."""
		action = False

		# Broadcast the kill signal, disconnecting our client and server
		self.kill.emit()

		if (self.client):
			self.client = None
			action = True

		if (self.server):
			self.server = None
			action = True

		if (action):
			self.log("Disconnected from session.")

		self.setAllowInput(False)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Biscord"))
		self.inputBox.setPlaceholderText(_translate("MainWindow", "Say something nice..."))
		self.hostName.setPlaceholderText(_translate("MainWindow", "Host name"))
		self.userName.setPlaceholderText(_translate("MainWindow", "Username"))
		self.connectServer.setToolTip(_translate("MainWindow", "Connect to the host"))
		self.startServer.setToolTip(_translate("MainWindow", "Start a server with this info"))
		self.disconnect.setToolTip(_translate("MainWindow", "Disconnect from the session"))

		QtGui.QFontDatabase.addApplicationFont(":fonts/text-regular")
		QtGui.QFontDatabase.addApplicationFont(":fonts/text-bold")
		QtGui.QFontDatabase.addApplicationFont(":fonts/text-med")

		with open("sheet.css", "r") as file:
			document = self.chatLog.document()
			document.setDefaultStyleSheet(file.read())
			self.chatLog.setDocument(document)

		with open("stylesheet.css", "r") as file:
			MainWindow.setStyleSheet(file.read())

	def closeEvent(self, event):
		self.config.set("CONNECTION", "hostname", self.hostName.text())
		self.config.set("CONNECTION", "port", str(self.portNumber.value()))
		self.config.set("CONNECTION", "username", self.userName.text())

		with open("config.ini", "w+") as file:
			self.config.write(file)



import resource_rc
