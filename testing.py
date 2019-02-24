

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from TYHOmain import Ui_MainWindow

class MyFirstGuiProgram(Ui_MainWindow):
	def __init__(self, dialog):
		Ui_MainWindow.__init__(self)
		self.setupUi(dialog)

		# Connect "add" button with a custom function (addInputTextToListbox)
		self.pushButton.clicked.connect(self.buttonPress)

	def buttonPress(self):
		print("button press")

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = MyFirstGuiProgram(dialog)

	dialog.show()
	sys.exit(app.exec_())