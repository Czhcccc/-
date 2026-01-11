# -*- coding: utf-8 -*-

# 表单实现从ui文件 'LoginUi.ui' 生成
#
# 创建者: PyQt5 UI代码生成器 5.15.10
#
# 警告: 当再次运行pyuic5时，对该文件的任何手动更改都将丢失。
# 除非您知道自己在做什么，否则不要编辑此文件。


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(70, 50, 331, 481))
        self.frame.setStyleSheet("#frame{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"border-radius:20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 50, 301, 191))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"Algerian\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 380, 261, 91))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"幼圆\";")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(400, 50, 321, 481))
        self.frame_2.setStyleSheet("#frame_2{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(250, 10, 93, 28))
        self.pushButton.setStyleSheet("QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"padding-bottom:5px;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/return.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(10, 40, 301, 371))
        self.frame_3.setMinimumSize(QtCore.QSize(301, 371))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget_2.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255,0);\n"
"    border:none;\n"
"    border-bottom:1px solid black;\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:7px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.Login = QtWidgets.QWidget()
        self.Login.setObjectName("Login")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Login)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_L_account = QtWidgets.QLineEdit(self.Login)
        self.line_L_account.setMinimumSize(QtCore.QSize(0, 35))
        self.line_L_account.setObjectName("line_L_account")
        self.verticalLayout_4.addWidget(self.line_L_account)
        self.line_L_password = QtWidgets.QLineEdit(self.Login)
        self.line_L_password.setMinimumSize(QtCore.QSize(0, 35))
        self.line_L_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_L_password.setObjectName("line_L_password")
        self.verticalLayout_4.addWidget(self.line_L_password)
        self.button_L_sure = QtWidgets.QPushButton(self.Login)
        self.button_L_sure.setMinimumSize(QtCore.QSize(0, 40))
        self.button_L_sure.setObjectName("button_L_sure")
        self.verticalLayout_4.addWidget(self.button_L_sure)
        self.stackedWidget_2.addWidget(self.Login)
        self.Register = QtWidgets.QWidget()
        self.Register.setObjectName("Register")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Register)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_R_account = QtWidgets.QLineEdit(self.Register)
        self.lineEdit_R_account.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_R_account.setObjectName("lineEdit_R_account")
        self.verticalLayout_5.addWidget(self.lineEdit_R_account)
        self.lineEdit_R_password1 = QtWidgets.QLineEdit(self.Register)
        self.lineEdit_R_password1.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_R_password1.setObjectName("lineEdit_R_password1")
        self.verticalLayout_5.addWidget(self.lineEdit_R_password1)
        self.lineEdit_R_password2 = QtWidgets.QLineEdit(self.Register)
        self.lineEdit_R_password2.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEdit_R_password2.setObjectName("lineEdit_R_password2")
        self.verticalLayout_5.addWidget(self.lineEdit_R_password2)
        self.pushButton_R_sure = QtWidgets.QPushButton(self.Register)
        self.pushButton_R_sure.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_R_sure.setObjectName("pushButton_R_sure")
        self.verticalLayout_5.addWidget(self.pushButton_R_sure)
        self.stackedWidget_2.addWidget(self.Register)
        self.horizontalLayout_2.addWidget(self.stackedWidget_2)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("QPushButton{\n"
"border:none;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-top:5px;\n"
"padding-left:5px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Login = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Login.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/login.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Login.setIcon(icon1)
        self.pushButton_Login.setObjectName("pushButton_Login")
        self.horizontalLayout.addWidget(self.pushButton_Login)
        self.pushButton_Register = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_Register.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/register.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Register.setIcon(icon2)
        self.pushButton_Register.setObjectName("pushButton_Register")
        self.horizontalLayout.addWidget(self.pushButton_Register)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_5)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        self.stackedWidget_2.setCurrentIndex(0)
        self.pushButton.clicked.connect(LoginWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.label.setText(_translate("LoginWindow", "Welcome to HopeBox"))
        self.label_2.setText(_translate("LoginWindow", "感谢支持！"))
        self.line_L_account.setPlaceholderText(_translate("LoginWindow", "账号："))
        self.line_L_password.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.button_L_sure.setText(_translate("LoginWindow", "确认"))
        self.lineEdit_R_account.setPlaceholderText(_translate("LoginWindow", "账号："))
        self.lineEdit_R_password1.setPlaceholderText(_translate("LoginWindow", "密码："))
        self.lineEdit_R_password2.setPlaceholderText(_translate("LoginWindow", "再次确认密码："))
        self.pushButton_R_sure.setText(_translate("LoginWindow", "注册"))
import res_rc
