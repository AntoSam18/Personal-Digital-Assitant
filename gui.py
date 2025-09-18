from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(912, 619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 911, 591))
        self.label.setPixmap(QtGui.QPixmap("./Downloads/7LP8.gif"))
        self.label.setScaledContents(True)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 410, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setText("RUN")
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 0);")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(800, 410, 91, 41))
        self.pushButton_2.setText("EXIT")
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 321, 81, 81))
        self.label_3.setPixmap(QtGui.QPixmap("./Downloads/projhu.gif"))
        self.label_3.setScaledContents(True)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(410, 10, 221, 51))
        self.textBrowser.setStyleSheet("background: transparent; color: white; font-size: 16px;")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(630, 10, 221, 51))
        self.textBrowser_2.setStyleSheet("background: transparent; color: white; font-size: 16px;")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 912, 21))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
