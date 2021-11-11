from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import cv2 as cv
from Traitement import *

class Ui_MainWindow(object):
    def __init__(self):
        self.tr = Traitement()
        self.path = ""
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(287, 295)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.bernoulli_result = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bernoulli_result.setFont(font)
        self.bernoulli_result.setText("")
        self.bernoulli_result.setObjectName("bernoulli_result")
        self.gridLayout.addWidget(self.bernoulli_result, 2, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 1, 2)
        self.gaussian = QtWidgets.QPushButton(self.centralwidget)
        self.gaussian.setObjectName("gaussian")
        self.gridLayout.addWidget(self.gaussian, 0, 2, 2, 1)
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setText("")
        self.img.setObjectName("img")
        self.gridLayout.addWidget(self.img, 1, 0, 3, 2)
        self.multi = QtWidgets.QPushButton(self.centralwidget)
        self.multi.setObjectName("multi")
        self.gridLayout.addWidget(self.multi, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 2)
        self.gussian_l_rate = QtWidgets.QLabel(self.centralwidget)
        self.gussian_l_rate.setText("")
        self.gussian_l_rate.setObjectName("gussian_l_rate")
        self.gridLayout.addWidget(self.gussian_l_rate, 6, 1, 1, 1)
        self.bernoulli_l_rate = QtWidgets.QLabel(self.centralwidget)
        self.bernoulli_l_rate.setText("")
        self.bernoulli_l_rate.setObjectName("bernoulli_l_rate")
        self.gridLayout.addWidget(self.bernoulli_l_rate, 7, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 0, 1, 1)
        self.multi_t_rate = QtWidgets.QLabel(self.centralwidget)
        self.multi_t_rate.setText("")
        self.multi_t_rate.setObjectName("multi_t_rate")
        self.gridLayout.addWidget(self.multi_t_rate, 8, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)
        self.multi_l_rate = QtWidgets.QLabel(self.centralwidget)
        self.multi_l_rate.setText("")
        self.multi_l_rate.setObjectName("multi_l_rate")
        self.gridLayout.addWidget(self.multi_l_rate, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 0, 1, 1)
        self.bernoulli_t_rate = QtWidgets.QLabel(self.centralwidget)
        self.bernoulli_t_rate.setText("")
        self.bernoulli_t_rate.setObjectName("bernoulli_t_rate")
        self.gridLayout.addWidget(self.bernoulli_t_rate, 7, 3, 1, 1)
        self.multi_result = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.multi_result.setFont(font)
        self.multi_result.setText("")
        self.multi_result.setObjectName("multi_result")
        self.gridLayout.addWidget(self.multi_result, 3, 3, 1, 1)
        self.gussian_t_rate = QtWidgets.QLabel(self.centralwidget)
        self.gussian_t_rate.setText("")
        self.gussian_t_rate.setObjectName("gussian_t_rate")
        self.gridLayout.addWidget(self.gussian_t_rate, 6, 3, 1, 1)
        self.gussian_result = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.gussian_result.setFont(font)
        self.gussian_result.setText("")
        self.gussian_result.setObjectName("gussian_result")
        self.gridLayout.addWidget(self.gussian_result, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 287, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Letters Recognition"))
        self.gaussian.setText(_translate("MainWindow", "Gaussian"))
        self.multi.setText(_translate("MainWindow", "Bernoulli"))
        self.label_5.setText(_translate("MainWindow", "test_success_rate"))
        self.label_4.setText(_translate("MainWindow", "learning_success_rate"))
        self.label_2.setText(_translate("MainWindow", "BernoulliNB"))
        self.label_3.setText(_translate("MainWindow", "MultinomialNB"))
        self.pushButton_2.setText(_translate("MainWindow", "Multinomial"))
        self.label.setText(_translate("MainWindow", "GaussianNB"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

        self.actionOpen.triggered.connect(self.openImg)
        self.gaussian.clicked.connect(self.gaussian_recognize)
        self.multi.clicked.connect(self.bernoulli_recognize)
        self.pushButton_2.clicked.connect(self.multinomial_recognize)
    

    #openImg() fonction pour ouvrir les images dans l'interface graphique
    def openImg(self):
        pathx = QFileDialog.getOpenFileName()[0]
        self.path = pathx
        pixmap = QtGui.QPixmap(pathx)
        pixmap4 = pixmap.scaled(351, 341, QtCore.Qt.KeepAspectRatio)
        self.img.setPixmap(QtGui.QPixmap(pixmap4))

    #afficher le taux de succes d'apprentissage sur nos exemples du test
    def multinomial_rateOfSuccess(self, testSuccesRate, learnSuccesRate):
        self.multi_t_rate.setText(str(testSuccesRate))
        self.multi_l_rate.setText(str(learnSuccesRate))
    
    def gaussian_rateOfSuccess(self, testSuccesRate, learnSuccesRate):
        self.gussian_t_rate.setText(str(testSuccesRate))
        self.gussian_l_rate.setText(str(learnSuccesRate))

    def bernoulli_rateOfSuccess(self, testSuccesRate, learnSuccesRate):
        self.bernoulli_t_rate.setText(str(testSuccesRate))
        self.bernoulli_l_rate.setText(str(learnSuccesRate))

    #traiter l'image choisie
    def gaussian_recognize(self):
        img = cv.imread(self.path)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.threshold(img,127,1,cv.THRESH_BINARY)[1]
        img = img.flatten()
        result = self.tr.gaussianNB.predict([img])
        self.gussian_result.setText(' '+result[0])
        return result

    def bernoulli_recognize(self):
        img = cv.imread(self.path)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.threshold(img,127,1,cv.THRESH_BINARY)[1]
        img = img.flatten()
        result = self.tr.bernoulliNB.predict([img])
        self.bernoulli_result.setText(' '+result[0])
        return result

    def multinomial_recognize(self):
        img = cv.imread(self.path)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = cv.threshold(img,127,1,cv.THRESH_BINARY)[1]
        img = img.flatten()
        result = self.tr.multinomialNB.predict([img])
        self.multi_result.setText(' '+result[0])
        return result

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.tr.gaussian_learning()
    ui.tr.bernoulli_learning()
    ui.tr.multinomial_learning()
    ui.setupUi(MainWindow)
    ui.gaussian_rateOfSuccess(ui.tr.gaussian_test_success_rate(), ui.tr.gaussian_learning_success_rate())
    ui.bernoulli_rateOfSuccess(ui.tr.bernoulli_test_success_rate(), ui.tr.bernoulli_learning_success_rate())
    ui.multinomial_rateOfSuccess(ui.tr.multinomial_test_success_rate(), ui.tr.multinomial_learning_success_rate())
    MainWindow.show()
    sys.exit(app.exec_())
