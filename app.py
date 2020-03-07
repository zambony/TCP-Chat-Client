from PyQt5 import QtCore, QtGui, QtWidgets, uic
from chat import ChatClient
import sys

UI_FILE = "chat.ui"

PANEL, QtBaseClass = uic.loadUiType(UI_FILE)


class App(QtBaseClass):
	def __init__(self):
		super().__init__()
		self.ui = ChatClient()
		self.ui.setupUi(self)
		self.show()

	def closeEvent(self, event):
		self.ui.closeEvent(event)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	dockIcon = QtGui.QIcon()
	dockIcon.addPixmap(QtGui.QPixmap(":/icons/biscord"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	app.setWindowIcon(dockIcon)
	program = App()
	program.show()

	sys.exit(app.exec_())
