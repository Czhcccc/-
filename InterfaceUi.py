from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 140, 860, 590))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(860, 590))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("#frame_6{\n"
"    background-color: rgb(85, 170, 127);\n"
"    border-bottom-left-radius:20px;\n"
"}\n"
"QPushButton{\n"
"    border:none;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 12pt \"幼圆\";\n"
"}\n"
"QPushButton:hover{\n"
"    color: rgba(0, 0, 0, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-bottom:5px;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_home = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_home.setObjectName("pushButton_home")
        self.verticalLayout_2.addWidget(self.pushButton_home)
        self.pushButton_module = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_module.setObjectName("pushButton_module")
        self.verticalLayout_2.addWidget(self.pushButton_module)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton_my = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_my.setObjectName("pushButton_my")
        self.verticalLayout_2.addWidget(self.pushButton_my)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setStyleSheet("#frame_7{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border-bottom-right-radius:20px;\n"
"}")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_7)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.frame_8 = QtWidgets.QFrame(self.page_home)
        self.frame_8.setGeometry(QtCore.QRect(30, 40, 581, 481))
        self.frame_8.setMinimumSize(QtCore.QSize(480, 270))
        self.frame_8.setStyleSheet("QPushButton{\n"
"    border:2px solid black;\n"
"    border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(221, 221, 221);\n"
"}")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_MAX = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_MAX.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_MAX.setObjectName("pushButton_MAX")
        self.verticalLayout_4.addWidget(self.pushButton_MAX)
        self.pushButton_Moral = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_Moral.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Moral.setObjectName("pushButton_Moral")
        self.verticalLayout_4.addWidget(self.pushButton_Moral)
        self.pushButton_Outline = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_Outline.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Outline.setObjectName("pushButton_Outline")
        self.verticalLayout_4.addWidget(self.pushButton_Outline)
        self.pushButton_Mao = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_Mao.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Mao.setObjectName("pushButton_Mao")
        self.verticalLayout_4.addWidget(self.pushButton_Mao)
        self.pushButton_Xi = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_Xi.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_Xi.setObjectName("pushButton_Xi")
        self.verticalLayout_4.addWidget(self.pushButton_Xi)
        self.stackedWidget.addWidget(self.page_home)
        self.page_my = QtWidgets.QWidget()
        self.page_my.setObjectName("page_my")
        self.frame_9 = QtWidgets.QFrame(self.page_my)
        self.frame_9.setGeometry(QtCore.QRect(80, 80, 480, 391))
        self.frame_9.setMinimumSize(QtCore.QSize(480, 270))
        self.frame_9.setStyleSheet("QPushButton{\n"
"    border:2px solid black;\n"
"    border-radius:7px;\n"
"    color:rgb(255,255,255);\n"
"    background-color:rgb(0,0,0);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(221, 221, 221);\n"
"}\n"
"QLineEdit{\n"
"    background-color:rgba(255,255,255,0);\n"
"    border:none;\n"
"    border-bottom:1px solid black;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_M_pass_1 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_M_pass_1.setText("")
        self.lineEdit_M_pass_1.setObjectName("lineEdit_M_pass_1")
        self.verticalLayout_5.addWidget(self.lineEdit_M_pass_1)
        self.lineEdit_M_pass_2 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_M_pass_2.setObjectName("lineEdit_M_pass_2")
        self.verticalLayout_5.addWidget(self.lineEdit_M_pass_2)
        self.pushButton_M_sure = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_M_sure.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_M_sure.setObjectName("pushButton_M_sure")
        self.verticalLayout_5.addWidget(self.pushButton_M_sure)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_9)
        self.stackedWidget_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(190, 10, 72, 15))
        self.label.setObjectName("label")
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 91, 16))
        self.label_2.setObjectName("label_2")
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.verticalLayout_5.addWidget(self.stackedWidget_2)
        self.stackedWidget.addWidget(self.page_my)
        self.page_unit = QtWidgets.QWidget()
        self.page_unit.setStyleSheet("QPushButton{\n"
"    border:2px solid black;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(221, 221, 221);\n"
"     padding-bottom:5px;\n"
"    padding-left:5px;\n"
"}")
        self.page_unit.setObjectName("page_unit")
        self.frame_11 = QtWidgets.QFrame(self.page_unit)
        self.frame_11.setGeometry(QtCore.QRect(40, 20, 571, 541))
        self.frame_11.setMinimumSize(QtCore.QSize(571, 541))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame_11)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 551, 531))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_fir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_fir.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_fir.setObjectName("pushButton_fir")
        self.gridLayout.addWidget(self.pushButton_fir, 0, 0, 1, 1)
        self.pushButton_fif = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_fif.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_fif.setObjectName("pushButton_fif")
        self.gridLayout.addWidget(self.pushButton_fif, 2, 0, 1, 1)
        self.pushButton_six = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_six.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_six.setObjectName("pushButton_six")
        self.gridLayout.addWidget(self.pushButton_six, 2, 1, 1, 1)
        self.pushButton_eig = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_eig.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_eig.setObjectName("pushButton_eig")
        self.gridLayout.addWidget(self.pushButton_eig, 3, 1, 1, 1)
        self.pushButton_sev = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_sev.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_sev.setObjectName("pushButton_sev")
        self.gridLayout.addWidget(self.pushButton_sev, 3, 0, 1, 1)
        self.pushButton_sec = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_sec.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_sec.setObjectName("pushButton_sec")
        self.gridLayout.addWidget(self.pushButton_sec, 0, 1, 1, 1)
        self.pushButton_fou = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_fou.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_fou.setObjectName("pushButton_fou")
        self.gridLayout.addWidget(self.pushButton_fou, 1, 1, 1, 1)
        self.pushButton_thi = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_thi.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_thi.setObjectName("pushButton_thi")
        self.gridLayout.addWidget(self.pushButton_thi, 1, 0, 1, 1)
        self.pushButton_nin = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_nin.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_nin.setObjectName("pushButton_nin")
        self.gridLayout.addWidget(self.pushButton_nin, 4, 0, 1, 1)
        self.pushButton_ten = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_ten.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_ten.setObjectName("pushButton_ten")
        self.gridLayout.addWidget(self.pushButton_ten, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_unit)
        self.page_module = QtWidgets.QWidget()
        self.page_module.setObjectName("page_module")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.page_module)
        self.stackedWidget_3.setGeometry(QtCore.QRect(10, 10, 621, 551))
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_module_2 = QtWidgets.QWidget()
        self.page_module_2.setObjectName("page_module_2")
        self.frame_10 = QtWidgets.QFrame(self.page_module_2)
        self.frame_10.setGeometry(QtCore.QRect(0, 0, 591, 531))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_import = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_import.setObjectName("pushButton_import")
        self.verticalLayout_6.addWidget(self.pushButton_import)
        self.pushButton_statistics = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_statistics.setObjectName("pushButton_statistics")
        self.verticalLayout_6.addWidget(self.pushButton_statistics)
        self.pushButton_wrong = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_wrong.setObjectName("pushButton_wrong")
        self.verticalLayout_6.addWidget(self.pushButton_wrong)
        self.stackedWidget_3.addWidget(self.page_module_2)
        self.page_import = QtWidgets.QWidget()
        self.page_import.setObjectName("page_import")
        self.frame_17 = QtWidgets.QFrame(self.page_import)
        self.frame_17.setGeometry(QtCore.QRect(20, 10, 591, 491))
        self.frame_17.setMinimumSize(QtCore.QSize(0, 491))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.pushButton_import_return = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_import_return.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_import_return.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"border:1px solid black;\n"
"background-color: rgb(85, 170, 127);\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{background-color: rgb(85, 255, 127)}")
        self.pushButton_import_return.setObjectName("pushButton_import_return")
        self.verticalLayout_13.addWidget(self.pushButton_import_return)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_13.addWidget(self.pushButton_5)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_13.addWidget(self.lineEdit)
        self.label_9 = QtWidgets.QLabel(self.frame_17)
        self.label_9.setMinimumSize(QtCore.QSize(0, 50))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_13.addWidget(self.pushButton_9)
        self.stackedWidget_3.addWidget(self.page_import)
        self.page_statistics = QtWidgets.QWidget()
        self.page_statistics.setObjectName("page_statistics")
        self.frame_25 = QtWidgets.QFrame(self.page_statistics)
        self.frame_25.setGeometry(QtCore.QRect(0, 20, 601, 531))
        self.frame_25.setMinimumSize(QtCore.QSize(601, 531))
        self.frame_25.setStyleSheet("/* 数据统计页面主容器 */\n"
"#frame_25 {\n"
"    background-color: white;\n"
"}\n"
"\n"
"/* 数据卡片通用样式 */\n"
"QFrame#frame_29,\n"
"QFrame#frame_30, \n"
"QFrame#frame_31,\n"
"QFrame#frame_32 {\n"
"    border-radius: 10px;\n"
"    padding: 15px;\n"
"    margin: 5px;\n"
"    border: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"/* 各个数据卡片的背景色 */\n"
"QFrame#frame_29 {\n"
"    background-color: #e3f2fd;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #e3f2fd, stop:1 #bbdefb);\n"
"}\n"
"\n"
"QFrame#frame_30 {\n"
"    background-color: #e8f5e8;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #e8f5e8, stop:1 #c8e6c9);\n"
"}\n"
"\n"
"QFrame#frame_31 {\n"
"    background-color: #ffebee;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #ffebee, stop:1 #ffcdd2);\n"
"}\n"
"\n"
"QFrame#frame_32 {\n"
"    background-color: #fff3e0;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 #fff3e0, stop:1 #ffecb3);\n"
"}\n"
"\n"
"/* 数据卡片内的标签样式 */\n"
"QFrame#frame_29 QLabel,\n"
"QFrame#frame_30 QLabel,\n"
"QFrame#frame_31 QLabel, \n"
"QFrame#frame_32 QLabel {\n"
"    font-family: \"幼圆\";\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* 图表区域样式 */\n"
"QTextEdit#textEdit_chart {\n"
"    background-color: #f8f9fa;\n"
"    border: 1px solid #dee2e6;\n"
"    border-radius: 8px;\n"
"    font-family: \"幼圆\";\n"
"    font-size: 12px;\n"
"    padding: 10px;\n"
"    color: #495057;\n"
"}\n"
"\n"
"/* 返回按钮样式 */\n"
"QPushButton#pushButton_statistics_return {\n"
"    background-color: #55aa7f;\n"
"    border: 1px solid #55aa7f;\n"
"    border-radius: 20px;\n"
"    color: white;\n"
"    font-family: \"幼圆\";\n"
"    font-size: 14px;\n"
"    padding: 8px 16px;\n"
"}\n"
"\n"
"QPushButton#pushButton_statistics_return:hover {\n"
"    background-color: #55ff7f;\n"
"    border-color: #55ff7f;\n"
"}\n"
"\n"
"QPushButton#pushButton_statistics_return:pressed {\n"
"    background-color: #459a6f;\n"
"    border-color: #459a6f;\n"
"}\n"
"\n"
"/* 标题样式 */\n"
"QLabel#label_statistics_title {\n"
"    font-family: \"幼圆\";\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #333333;\n"
"    background: transparent;\n"
"}\n"
"\n"
"/* 图表标题样式 */\n"
"QLabel#label_16 {\n"
"    font-family: \"幼圆\";\n"
"    font-size: 14px;\n"
"    color: #333333;\n"
"    background: transparent;\n"
"}")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.pushButton_statistics_return = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_statistics_return.setGeometry(QtCore.QRect(10, 0, 121, 41))
        self.pushButton_statistics_return.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"border:1px solid black;\n"
"background-color: rgb(85, 170, 127);\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{background-color: rgb(85, 255, 127)}")
        self.pushButton_statistics_return.setObjectName("pushButton_statistics_return")
        self.label_statistics_title = QtWidgets.QLabel(self.frame_25)
        self.label_statistics_title.setGeometry(QtCore.QRect(200, 0, 231, 51))
        self.label_statistics_title.setStyleSheet("font: 18pt \"幼圆\";")
        self.label_statistics_title.setObjectName("label_statistics_title")
        self.frame_26 = QtWidgets.QFrame(self.frame_25)
        self.frame_26.setGeometry(QtCore.QRect(10, 50, 591, 481))
        self.frame_26.setMinimumSize(QtCore.QSize(591, 481))
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_26)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_27 = QtWidgets.QFrame(self.frame_26)
        self.frame_27.setMinimumSize(QtCore.QSize(295, 479))
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_29 = QtWidgets.QFrame(self.frame_27)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_total_count = QtWidgets.QLabel(self.frame_29)
        self.label_total_count.setObjectName("label_total_count")
        self.horizontalLayout_10.addWidget(self.label_total_count)
        self.verticalLayout_8.addWidget(self.frame_29)
        self.frame_30 = QtWidgets.QFrame(self.frame_27)
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_accuracy_rate = QtWidgets.QLabel(self.frame_30)
        self.label_accuracy_rate.setObjectName("label_accuracy_rate")
        self.horizontalLayout_9.addWidget(self.label_accuracy_rate)
        self.verticalLayout_8.addWidget(self.frame_30)
        self.frame_31 = QtWidgets.QFrame(self.frame_27)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_wrong_count = QtWidgets.QLabel(self.frame_31)
        self.label_wrong_count.setObjectName("label_wrong_count")
        self.horizontalLayout_8.addWidget(self.label_wrong_count)
        self.verticalLayout_8.addWidget(self.frame_31)
        self.frame_32 = QtWidgets.QFrame(self.frame_27)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_32)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_time_count = QtWidgets.QLabel(self.frame_32)
        self.label_time_count.setObjectName("label_time_count")
        self.horizontalLayout_7.addWidget(self.label_time_count)
        self.verticalLayout_8.addWidget(self.frame_32)
        self.horizontalLayout_6.addWidget(self.frame_27)
        self.frame_28 = QtWidgets.QFrame(self.frame_26)
        self.frame_28.setMinimumSize(QtCore.QSize(294, 479))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.label_16 = QtWidgets.QLabel(self.frame_28)
        self.label_16.setGeometry(QtCore.QRect(60, 10, 151, 41))
        self.label_16.setObjectName("label_16")
        self.textEdit_chart = QtWidgets.QTextEdit(self.frame_28)
        self.textEdit_chart.setGeometry(QtCore.QRect(0, 60, 291, 421))
        self.textEdit_chart.setObjectName("textEdit_chart")
        self.horizontalLayout_6.addWidget(self.frame_28)
        self.stackedWidget_3.addWidget(self.page_statistics)
        self.page_wrong = QtWidgets.QWidget()
        self.page_wrong.setObjectName("page_wrong")
        self.frame_18 = QtWidgets.QFrame(self.page_wrong)
        self.frame_18.setGeometry(QtCore.QRect(10, 80, 611, 481))
        self.frame_18.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_18.setMaximumSize(QtCore.QSize(611, 541))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_19 = QtWidgets.QFrame(self.frame_18)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.listWidget_wrong = QtWidgets.QListWidget(self.frame_19)
        self.listWidget_wrong.setGeometry(QtCore.QRect(10, 10, 251, 461))
        self.listWidget_wrong.setStyleSheet("font: 20pt \"幼圆\";")
        self.listWidget_wrong.setIconSize(QtCore.QSize(24, 24))
        self.listWidget_wrong.setObjectName("listWidget_wrong")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_wrong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_wrong.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_wrong.addItem(item)
        self.stackedWidget_wrong = QtWidgets.QStackedWidget(self.frame_19)
        self.stackedWidget_wrong.setGeometry(QtCore.QRect(270, 0, 331, 511))
        self.stackedWidget_wrong.setObjectName("stackedWidget_wrong")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.frame_21 = QtWidgets.QFrame(self.page_6)
        self.frame_21.setGeometry(QtCore.QRect(50, 0, 251, 539))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.label_6 = QtWidgets.QLabel(self.frame_21)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 241, 101))
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_21)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 110, 251, 421))
        self.textEdit_2.setObjectName("textEdit_2")
        self.stackedWidget_wrong.addWidget(self.page_6)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.frame_22 = QtWidgets.QFrame(self.page_8)
        self.frame_22.setGeometry(QtCore.QRect(40, 0, 251, 539))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.label_7 = QtWidgets.QLabel(self.frame_22)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 221, 101))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_22)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 120, 261, 421))
        self.textEdit_3.setObjectName("textEdit_3")
        self.stackedWidget_wrong.addWidget(self.page_8)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.frame_20 = QtWidgets.QFrame(self.page_5)
        self.frame_20.setGeometry(QtCore.QRect(38, 0, 251, 539))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.label_4 = QtWidgets.QLabel(self.frame_20)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 241, 71))
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.frame_20)
        self.textEdit.setGeometry(QtCore.QRect(0, 60, 261, 421))
        self.textEdit.setObjectName("textEdit")
        self.stackedWidget_wrong.addWidget(self.page_5)
        self.horizontalLayout_5.addWidget(self.frame_19)
        self.frame_24 = QtWidgets.QFrame(self.page_wrong)
        self.frame_24.setGeometry(QtCore.QRect(10, 29, 601, 51))
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.pushButton_wrong_return = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_wrong_return.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.pushButton_wrong_return.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"border:1px solid black;\n"
"background-color: rgb(85, 170, 127);\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{background-color: rgb(85, 255, 127)}")
        self.pushButton_wrong_return.setObjectName("pushButton_wrong_return")
        self.label_11 = QtWidgets.QLabel(self.frame_24)
        self.label_11.setGeometry(QtCore.QRect(250, 10, 111, 31))
        self.label_11.setStyleSheet("font: 14pt \"幼圆\";")
        self.label_11.setObjectName("label_11")
        self.stackedWidget_3.addWidget(self.page_wrong)
        self.stackedWidget.addWidget(self.page_module)
        self.page_practice1 = QtWidgets.QWidget()
        self.page_practice1.setObjectName("page_practice1")
        self.frame_12 = QtWidgets.QFrame(self.page_practice1)
        self.frame_12.setGeometry(QtCore.QRect(10, 0, 441, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.frame_12)
        self.label_3.setMaximumSize(QtCore.QSize(441, 100))
        self.label_3.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.radioButton = QtWidgets.QRadioButton(self.frame_12)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_7.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_12)
        self.radioButton_2.setStyleSheet("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_7.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_12)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_7.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_12)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_7.addWidget(self.radioButton_4)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_7.addWidget(self.pushButton_18)
        self.pushButton_show_answer1 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_show_answer1.setObjectName("pushButton_show_answer1")
        self.verticalLayout_7.addWidget(self.pushButton_show_answer1)
        self.pushButton_next1 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_next1.setObjectName("pushButton_next1")
        self.verticalLayout_7.addWidget(self.pushButton_next1)
        self.frame_13 = QtWidgets.QFrame(self.page_practice1)
        self.frame_13.setGeometry(QtCore.QRect(450, 10, 191, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.textEdit_answer = QtWidgets.QTextEdit(self.frame_13)
        self.textEdit_answer.setEnabled(True)
        self.textEdit_answer.setGeometry(QtCore.QRect(0, 0, 181, 561))
        self.textEdit_answer.setStyleSheet("#textEdit_answer{\n"
"    visibility: hidden !important;\n"
"}")
        self.textEdit_answer.setReadOnly(False)
        self.textEdit_answer.setPlaceholderText("")
        self.textEdit_answer.setObjectName("textEdit_answer")
        self.stackedWidget.addWidget(self.page_practice1)
        self.page_practice2 = QtWidgets.QWidget()
        self.page_practice2.setObjectName("page_practice2")
        self.frame_14 = QtWidgets.QFrame(self.page_practice2)
        self.frame_14.setGeometry(QtCore.QRect(0, 0, 441, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_14)
        self.label_5.setMaximumSize(QtCore.QSize(441, 100))
        self.label_5.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.radioButton_9 = QtWidgets.QRadioButton(self.frame_14)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout_9.addWidget(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(self.frame_14)
        self.radioButton_10.setStyleSheet("")
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout_9.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.frame_14)
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout_9.addWidget(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.frame_14)
        self.radioButton_12.setObjectName("radioButton_12")
        self.verticalLayout_9.addWidget(self.radioButton_12)
        self.pushButton_last2 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_last2.setObjectName("pushButton_last2")
        self.verticalLayout_9.addWidget(self.pushButton_last2)
        self.pushButton_show_answer2 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_show_answer2.setObjectName("pushButton_show_answer2")
        self.verticalLayout_9.addWidget(self.pushButton_show_answer2)
        self.pushButton_next2 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_next2.setObjectName("pushButton_next2")
        self.verticalLayout_9.addWidget(self.pushButton_next2)
        self.frame_15 = QtWidgets.QFrame(self.page_practice2)
        self.frame_15.setGeometry(QtCore.QRect(440, 0, 191, 571))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.textEdit_answer2 = QtWidgets.QTextEdit(self.frame_15)
        self.textEdit_answer2.setGeometry(QtCore.QRect(10, 10, 181, 561))
        self.textEdit_answer2.setObjectName("textEdit_answer2")
        self.stackedWidget.addWidget(self.page_practice2)
        self.page_practice3 = QtWidgets.QWidget()
        self.page_practice3.setObjectName("page_practice3")
        self.frame_16 = QtWidgets.QFrame(self.page_practice3)
        self.frame_16.setGeometry(QtCore.QRect(10, 10, 621, 571))
        self.frame_16.setMinimumSize(QtCore.QSize(621, 540))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.frame_16)
        self.label_8.setMinimumSize(QtCore.QSize(0, 100))
        self.label_8.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_12.addWidget(self.label_8)
        self.pushButton_last3 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_last3.setObjectName("pushButton_last3")
        self.verticalLayout_12.addWidget(self.pushButton_last3)
        self.pushButton_show_answer3 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_show_answer3.setObjectName("pushButton_show_answer3")
        self.verticalLayout_12.addWidget(self.pushButton_show_answer3)
        self.pushButton_next3 = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_next3.setObjectName("pushButton_next3")
        self.verticalLayout_12.addWidget(self.pushButton_next3)
        self.textEdit_answer3 = QtWidgets.QTextEdit(self.frame_16)
        self.textEdit_answer3.setObjectName("textEdit_answer3")
        self.verticalLayout_12.addWidget(self.textEdit_answer3)
        self.stackedWidget.addWidget(self.page_practice3)
        self.page_finish = QtWidgets.QWidget()
        self.page_finish.setObjectName("page_finish")
        self.frame_23 = QtWidgets.QFrame(self.page_finish)
        self.frame_23.setGeometry(QtCore.QRect(60, 70, 511, 441))
        self.frame_23.setMinimumSize(QtCore.QSize(511, 441))
        self.frame_23.setStyleSheet("")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.label_10 = QtWidgets.QLabel(self.frame_23)
        self.label_10.setGeometry(QtCore.QRect(50, 140, 421, 101))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(26)
        self.label_10.setFont(font)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.pushButton_finish_return = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_finish_return.setGeometry(QtCore.QRect(190, 280, 131, 41))
        self.pushButton_finish_return.setStyleSheet("QPushButton{\n"
"border-radius:5px;\n"
"border:1px solid black;\n"
"background-color: rgb(85, 170, 127);\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover{background-color: rgb(85, 255, 127)}")
        self.pushButton_finish_return.setObjectName("pushButton_finish_return")
        self.stackedWidget.addWidget(self.page_finish)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(90, 90, 858, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:20px;\n"
"border-top-right-radius:20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setStyleSheet("border:none;\n"
"font: 12pt \"幼圆\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/设计刷题软件 logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom:5px;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_logout = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_logout.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/exit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_logout.setIcon(icon1)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.horizontalLayout_3.addWidget(self.pushButton_logout)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/min.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/return.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.horizontalLayout.addWidget(self.frame_5, 0, QtCore.Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_wrong.setCurrentIndex(2)
        self.pushButton_4.clicked.connect(MainWindow.close) # type: ignore
        self.pushButton_3.clicked.connect(MainWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # --- 调试并确保导入按钮绑定（粘在 setupUi(self) 之后） ---
        try:
                # 列出 ui 中所有包含 pushButton 的属性，帮助定位实际名字
                pushbtn_attrs = [a for a in dir(self.ui) if "pushbutton" in a.lower()]
                print("DEBUG: ui pushButton attributes found:", pushbtn_attrs)

                # 如果确实存在 pushButton_import，就绑定；否则尝试绑定到 confirm_import 作为后备
                if hasattr(self.ui, "pushButton_import"):
                        btn = getattr(self.ui, "pushButton_import")
                        try:
                                btn.clicked.disconnect()
                        except Exception:
                                pass
                        # 优先连接到 _on_import_button（如果你实现了），否则连接 confirm_import
                        handler = getattr(self, "_on_import_button", None) or getattr(self, "confirm_import", None)
                        if handler is not None:
                                btn.clicked.connect(handler)
                                print("DEBUG: Bound import button: pushButton_import ->", handler.__name__)
                        else:
                                print("DEBUG: Found pushButton_import but no handler _on_import_button / confirm_import present")
                else:
                        print("DEBUG: pushButton_import not found on self.ui (check InterfaceUi.py)")
        except Exception as e:
                print("DEBUG: exception during import-button bind:", e)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_home.setText(_translate("MainWindow", "首页"))
        self.pushButton_module.setText(_translate("MainWindow", "功能"))
        self.pushButton_my.setText(_translate("MainWindow", "我的"))
        self.pushButton_MAX.setText(_translate("MainWindow", "马克思主义原理"))
        self.pushButton_Moral.setText(_translate("MainWindow", "思想道德与法治"))
        self.pushButton_Outline.setText(_translate("MainWindow", "中国近代史纲要"))
        self.pushButton_Mao.setText(_translate("MainWindow", "毛泽东思想和中国特色社会主义理论体系概论"))
        self.pushButton_Xi.setText(_translate("MainWindow", "习近平新时代中国特色社会主义思想概论"))
        self.lineEdit_M_pass_1.setPlaceholderText(_translate("MainWindow", "密码："))
        self.lineEdit_M_pass_2.setPlaceholderText(_translate("MainWindow", "确认密码："))
        self.pushButton_M_sure.setText(_translate("MainWindow", "确定"))
        self.label.setText(_translate("MainWindow", "密码非法"))
        self.label_2.setText(_translate("MainWindow", "密码不一致"))
        self.pushButton_fir.setText(_translate("MainWindow", "第一章"))
        self.pushButton_fif.setText(_translate("MainWindow", "第五章"))
        self.pushButton_six.setText(_translate("MainWindow", "第六章"))
        self.pushButton_eig.setText(_translate("MainWindow", "第八章"))
        self.pushButton_sev.setText(_translate("MainWindow", "第七章"))
        self.pushButton_sec.setText(_translate("MainWindow", "第二章"))
        self.pushButton_fou.setText(_translate("MainWindow", "第四章"))
        self.pushButton_thi.setText(_translate("MainWindow", "第三章"))
        self.pushButton_nin.setText(_translate("MainWindow", "第九章"))
        self.pushButton_ten.setText(_translate("MainWindow", "第十章"))
        self.pushButton_import.setText(_translate("MainWindow", "导入题目"))
        self.pushButton_statistics.setText(_translate("MainWindow", "数据统计"))
        self.pushButton_wrong.setText(_translate("MainWindow", "错题本"))
        self.pushButton_import_return.setText(_translate("MainWindow", "返回"))
        self.pushButton_5.setText(_translate("MainWindow", "选择文件"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "文件路径："))
        self.label_9.setText(_translate("MainWindow", "支持pdf格式和word格式"))
        self.pushButton_9.setText(_translate("MainWindow", "确认导入"))
        self.pushButton_statistics_return.setText(_translate("MainWindow", "返回"))
        self.label_statistics_title.setText(_translate("MainWindow", "学习数据统计"))
        self.label_total_count.setText(_translate("MainWindow", "总刷题数"))
        self.label_accuracy_rate.setText(_translate("MainWindow", "正确率"))
        self.label_wrong_count.setText(_translate("MainWindow", "错题数"))
        self.label_time_count.setText(_translate("MainWindow", "学习时长"))
        self.label_16.setText(_translate("MainWindow", "各科目正确率统计"))
        self.textEdit_chart.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'幼圆\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\">📊 各科目正确率统计：</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\">✅ 马克思主义原理: ██████████ 85%</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\">✅ 思想道德与法治: ████████▒▒ 76%</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\">✅ 中国近代史纲要: █████████▒ 82%</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\">✅ 毛泽东思想概论: ██████▒▒▒▒ 65%</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\">✅ 习近平新时代中国特色社会主义思想: ██████████ 90%</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\">📈 趋势分析：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\">• 最近7天正确率上升 5%</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\">• 最强科目：习近平新时代中国特色社会主义思想</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\">• 需加强：毛泽东思想概论</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:9pt; color:#50a14f;\">&quot;&quot;&quot;</span></p></body></html>"))
        self.listWidget_wrong.setSortingEnabled(True)
        __sortingEnabled = self.listWidget_wrong.isSortingEnabled()
        self.listWidget_wrong.setSortingEnabled(False)
        item = self.listWidget_wrong.item(0)
        item.setText(_translate("MainWindow", "1.（ ）是中国特色社会主义最本质的特征和中国特色社会主义制度的最大优势。"))
        item = self.listWidget_wrong.item(1)
        item.setText(_translate("MainWindow", "2.理想按性质可分为科学理想和非科学理想。判断一种理想是否科学、正确的根本标准是（ ）"))
        item = self.listWidget_wrong.item(2)
        item.setText(_translate("MainWindow", "3.社会主义核心价值观中，属于社会层面价值要求的是（ ）。"))
        self.listWidget_wrong.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("MainWindow", "1.（ ）是中国特色社会主义最本质的特征和中国特色社会主义制度的最大优势。"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115; background-color:#ffffff;\">A. 人民民主专政 B. 中国共产党的领导 C. 改革开放 D. 社会主义市场经济体制</span></p>\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">答案：B</span></p>\n"
"<p style=\" margin-top:4px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">解析：</span><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\"> 本题考查的是中国特色社会主义的核心领导力量。中国共产党的领导是中国特色社会主义最本质的特征，这是由我们国家的性质和党的先进性决定的。其他选项都是中国特色社会主义的重要内容，但都不是最本质的特征和最大优势。</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "2.理想按性质可分为科学理想和非科学理想。判断一种理想是否科学、正确的根本标准是（ ）。"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115; background-color:#ffffff;\">A. 是否主观上满足个人的愿望 B. 是否在实践中得到实现 C. 是否反映客观事物发展的规律 D. 是否被社会大多数人所认同</span></p>\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">答案：C</span></p>\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">解析：</span><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\"> 本题考查理想的性质。判断一种理想是否科学，关键在于它是否遵循事物发展的客观规律，是否符合社会发展的前进方向。选项A、B、D都是片面的或主观的判断标准，不能作为根本依据。</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "3.社会主义核心价值观中，属于社会层面价值要求的是（ ）。"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115; background-color:#ffffff;\">A. 富强、民主、文明、和谐 B. 自由、平等、公正、法治 C. 爱国、敬业、诚信、友善 D. 改革、开放、创新、发展</span></p>\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">答案：B 解析：</span><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\"> 本题考查社会主义核心价值观三个层面的具体内容。富强、民主、文明、和谐是国家层面的价值目标；自由、平等、公正、法治是社会层面的价值取向；爱国、敬业、诚信、友善是公民个人层面的价值准则。</span></p></body></html>"))
        self.pushButton_wrong_return.setText(_translate("MainWindow", "返回"))
        self.label_11.setText(_translate("MainWindow", "错题本"))
        self.label_3.setText(_translate("MainWindow", "1.（ ）是中国特色社会主义最本质的特征和中国特色社会主义制度的最大优势"))
        self.radioButton.setText(_translate("MainWindow", "A. 人民民主专政"))
        self.radioButton_2.setText(_translate("MainWindow", "B. 中国共产党的领导"))
        self.radioButton_3.setText(_translate("MainWindow", "C. 改革开放"))
        self.radioButton_4.setText(_translate("MainWindow", "D. 社会主义市场经济体制"))
        self.pushButton_18.setText(_translate("MainWindow", "上一题"))
        self.pushButton_show_answer1.setText(_translate("MainWindow", "提交"))
        self.pushButton_next1.setText(_translate("MainWindow", "下一题"))
        self.textEdit_answer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">答案：B </span></p>\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">解析：</span><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\"> 本题考查的是中国特色社会主义的核心领导力量。中国共产党的领导是中国特色社会主义最本质的特征，这是由我们国家的性质和党的先进性决定的。其他选项都是中国特色社会主义的重要内容，但都不是最本质的特征和最大优势。</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "2.关于理想与现实的关系，下列表述正确的有（ ）。"))
        self.radioButton_9.setText(_translate("MainWindow", "A. 理想与现实是对立统一的"))
        self.radioButton_10.setText(_translate("MainWindow", "B. 现实中包含着理想的因素，理想中也包含着现实的因素"))
        self.radioButton_11.setText(_translate("MainWindow", "C. 理想可以转化为未来的现实"))
        self.radioButton_12.setText(_translate("MainWindow", "D. 理想是完美的，现实是有缺陷的，二者不可调和"))
        self.pushButton_last2.setText(_translate("MainWindow", "上一题"))
        self.pushButton_show_answer2.setText(_translate("MainWindow", "提交"))
        self.pushButton_next2.setText(_translate("MainWindow", "下一题"))
        self.textEdit_answer2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">答案：A, B, C</span></p>\n"
"<p style=\" margin-top:4px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">解析：</span><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\"> 本题考查对理想与现实辩证关系的理解。A、B、C三项准确地描述了理想与现实的辩证统一关系。D项是错误的，它割裂了理想与现实的联系，把二者绝对对立起来，是形而上学的观点。理想源于现实又超越现实，二者在一定条件下可以相互转化。</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "3.如何理解“中国式现代化是全体人民共同富裕的现代化”？请结合所学，谈谈你对这一特征的认识，并简要说明青年学生在这一过程中可以有何作为。"))
        self.pushButton_last3.setText(_translate("MainWindow", "上一题"))
        self.pushButton_show_answer3.setText(_translate("MainWindow", "显示答案"))
        self.pushButton_next3.setText(_translate("MainWindow", "下一题"))
        self.textEdit_answer3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:16px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">1. 对“全体人民共同富裕的现代化”的内涵理解：</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\" style=\" margin-top:16px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">本质内涵：</span><span style=\" font-size:16px;\"> 共同富裕是中国特色社会主义的本质要求，不是少数人的富裕，也不是整齐划一的平均主义。它意味着在高质量发展中，通过合理的制度安排，扩大中等收入群体比重，增加低收入群体收入，调节过高收入，促进社会公平正义，使全体人民共享改革发展成果。</span></li>\n"
"<li style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\" style=\" margin-top:6px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">与西方模式的区别：</span><span style=\" font-size:16px;\"> 西方现代化往往伴随着严重的贫富两极分化。中国式现代化则致力于防止这一现象，强调在做大“蛋糕”的同时分好“蛋糕”，追求的是效率与公平的统一，是实现人的全面发展和社会全面进步的内在要求。</span></li></ul>\n"
"<p style=\" margin-top:16px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">2. “共同富裕”对于中国式现代化的意义：</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\" style=\" margin-top:16px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">政治意义：</span><span style=\" font-size:16px;\"> 体现了党的初心使命和全心全意为人民服务的根本宗旨，能够巩固党的执政基础，确保社会主义现代化建设的正确方向。</span></li>\n"
"<li style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\" style=\" margin-top:6px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">经济意义：</span><span style=\" font-size:16px;\"> 共同富裕能够形成强大的国内市场需求，为经济持续健康发展提供内生动力，构建以国内大循环为主体的新发展格局。</span></li>\n"
"<li style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\" style=\" margin-top:6px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">社会意义：</span><span style=\" font-size:16px;\"> 有效缓解社会矛盾，维护社会和谐稳定，彰显社会主义制度的优越性，是实现中华民族伟大复兴中国梦的必然要求。</span></li></ul>\n"
"<p style=\" margin-top:16px; margin-bottom:16px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; font-weight:600; color:#0f1115;\">3. 青年学生的作为：</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\" style=\" margin-top:16px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">立足本职，锤炼本领：</span><span style=\" font-size:16px;\"> 努力学习科学文化知识和专业技能，提高自身综合素质，未来在各自的岗位上创造财富，成为推动高质量发展的中坚力量，这是实现共同富裕的基础。</span></li>\n"
"<li style=\" font-family:\'quote-cjk-patch\',\'Inter\',\'system-ui\',\'-apple-system\',\'BlinkMacSystemFont\',\'Segoe UI\',\'Roboto\',\'Oxygen\',\'Ubuntu\',\'Cantarell\',\'Open Sans\',\'Helvetica Neue\',\'sans-serif\'; font-size:16px; color:#0f1115;\" style=\" margin-top:6px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; font-weight:600;\">增强责任，投身实践：</span><span style=\" font-size:16px;\"> 关注社会问题，积极参与志愿服务、乡村振兴、社区治理等社会实践，利用所学知识为缩小城乡差距、区域差距贡献力量，培养服务人民、奉献社会的情怀。</span></li></ul></body></html>"))
        self.label_10.setText(_translate("MainWindow", "恭喜你，已经做完了所有的题目！"))
        self.pushButton_finish_return.setText(_translate("MainWindow", "返回首页"))
        self.pushButton.setText(_translate("MainWindow", "HopeBox"))
import res_rc
