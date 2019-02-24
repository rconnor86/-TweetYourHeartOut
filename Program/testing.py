

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from newmain import Ui_MainWindow
import Authentication
import tweepy
import analytics
import nnInterface

auth = tweepy.OAuthHandler('gvracgdHjxGXcGHPlkI9e2ER5', 'tslCrlX8fWeaaeyu2l9PkgxrpfAE745qk2R47fEYpNCANwOZ2V')

class MyFirstGuiProgram(Ui_MainWindow):
	def __init__(self, dialog):
		Ui_MainWindow.__init__(self)
		self.setupUi(dialog)

		# Connect "add" button with a custom function (addInputTextToListbox)
		self.pushButton.clicked.connect(self.buttonpress1)
		self.pushButton_2.clicked.connect(self.buttonpress2)

	def buttonpress1(self):
		Authentication.authWindow(auth)

	def buttonpress2(self):
		pin = self.lineEdit.text()
		numTweets = self.lineEdit_2.text()
		pin = str(pin)
		numTweets = int(numTweets)
		print(pin)
		print(numTweets)
		Authentication.authenticate_and_scrape(pin, numTweets, auth)
		sentiment, preds = nnInterface.runNextwork("C:/Users/bribr/OneDrive - Washington State University (email.wsu.edu)/Downloads/#TweetYourHeartOut/-TweetYourHeartOut/Program/results2.csv", 1)
		print("Most common sentiment is ", sentiment)
		analytics.plotBarGraph(preds)
		analytics.plotPieChart(preds)


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = MyFirstGuiProgram(dialog)

	dialog.show()
	sys.exit(app.exec_())