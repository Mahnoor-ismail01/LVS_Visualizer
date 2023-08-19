# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 141, 551))
        self.listWidget.setStyleSheet("background-color: rgb(94, 92, 100);")
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 60, 131, 41))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.hide()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 0, 171, 551))
        self.label.setStyleSheet("background-color: rgb(202, 186, 205);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 130, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.hide()
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 200, 131, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 141, 31))
        self.label_2.setStyleSheet("color: rgb(11, 3, 20);\n"
"background-color: rgb(202, 186, 205);\n"
"font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 0, 171, 31))
        self.label_3.setStyleSheet("background-color: rgb(94, 92, 100);\n"
"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 60, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.browseConnect()
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 90, 101, 17))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 160, 101, 16))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 130, 91, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(30, 200, 91, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 230, 101, 16))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 270, 91, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 300, 101, 16))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 370, 101, 16))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 340, 91, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 470, 91, 41))
        self.pushButton_9.setStyleSheet("background-color: rgb(202, 186, 205);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(310, 0, 491, 551))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(140, 68, 20, 31))
        self.line.setStyleSheet("\n"
"color: rgb(53, 132, 228);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 40, 16, 451))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(140, 130, 20, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(140, 200, 16, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label.raise_()
        self.listWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.pushButton_3.raise_()
        self.pushButton_6.raise_()
        self.label_9.raise_()
        self.pushButton_7.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.treeWidget.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def browseConnect(self):
        self.pushButton_2.clicked.connect(self.browse_file)
    def browse_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)", options=options)

        if file_path:
            print("Selected File:", file_path)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Netlist"))
        self.pushButton_4.setText(_translate("MainWindow", "Schematic"))
        self.pushButton_5.setText(_translate("MainWindow", "Cross Reference"))
        self.label_2.setText(_translate("MainWindow", "          Input Tab"))
        self.label_3.setText(_translate("MainWindow", "              View Tab"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.label_5.setText(_translate("MainWindow", "Input File 01"))
        self.label_7.setText(_translate("MainWindow", "Input File 01"))
        self.pushButton_3.setText(_translate("MainWindow", "Browse"))
        self.pushButton_6.setText(_translate("MainWindow", "Browse"))
        self.label_9.setText(_translate("MainWindow", "Input File 01"))
        self.pushButton_7.setText(_translate("MainWindow", "Browse"))
        self.label_11.setText(_translate("MainWindow", "Input File 01"))
        self.label_12.setText(_translate("MainWindow", "Input File 01"))
        self.pushButton_8.setText(_translate("MainWindow", "Browse"))
        self.pushButton_9.setText(_translate("MainWindow", "START >>"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
