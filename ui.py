# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 566)
        MainWindow.setMinimumSize(QtCore.QSize(990, 566))
        MainWindow.setMaximumSize(QtCore.QSize(990, 566))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_show_camera = QtWidgets.QLabel(self.centralwidget)
        self.label_show_camera.setGeometry(QtCore.QRect(20, 30, 640, 480))
        self.label_show_camera.setStyleSheet("border-width:2px;\n"
                                                "border-style:solid;\n"
                                                "border-color: black;\n"
                                                "background: gray;\n"
                                                "font-weight: 800;")
        self.label_show_camera.setObjectName("label_show_camera")
        self.answer = QtWidgets.QLabel(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(690, 30, 271, 331))
        self.answer.setStyleSheet("border-width:1px;\n"
                                    "border-style:solid;\n"
                                    "border-color: black;\n"
                                    "background: white;")
        self.answer.setText("")
        self.answer.setObjectName("answer")
        self.button_open_camera = QtWidgets.QPushButton(self.centralwidget)
        self.button_open_camera.setGeometry(QtCore.QRect(730, 390, 201, 51))
        self.button_open_camera.setStyleSheet("")
        self.button_open_camera.setObjectName("button_open_camera")
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(730, 450, 201, 51))
        self.button_close.setObjectName("button_close")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????"))
        self.label_show_camera.setText(_translate("MainWindow", "video"))
        self.button_open_camera.setText(_translate("MainWindow", "???????????????"))
        self.button_close.setText(_translate("MainWindow", "??????"))

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())