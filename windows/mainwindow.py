# -*- coding: utf-8 -*-

import time

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from source import search, create
import main


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1175, 725)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(False)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(11)
        self.action.setFont(font)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_3.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 16pt \"Arial\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(8, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -9, 1128, 149))

        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.pushButton_18 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_8.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_8.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_8.addWidget(self.pushButton_20)

        self.horizontalLayout.addLayout(self.verticalLayout_8)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_27 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_11.addWidget(self.pushButton_27)
        self.pushButton_28 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_11.addWidget(self.pushButton_28)
        self.pushButton_29 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_11.addWidget(self.pushButton_29)
        self.horizontalLayout.addLayout(self.verticalLayout_11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_24 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_10.addWidget(self.pushButton_24)
        self.pushButton_25 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_10.addWidget(self.pushButton_25)
        self.pushButton_26 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_10.addWidget(self.pushButton_26)
        self.horizontalLayout.addLayout(self.verticalLayout_10)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pushButton_30 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_12.addWidget(self.pushButton_30)
        self.pushButton_31 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_12.addWidget(self.pushButton_31)
        self.pushButton_32 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_12.addWidget(self.pushButton_32)
        self.horizontalLayout.addLayout(self.verticalLayout_12)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.pushButton_21 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_9.addWidget(self.pushButton_21)
        self.pushButton_22 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_9.addWidget(self.pushButton_22)
        self.pushButton_23 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.verticalLayout_9.addWidget(self.pushButton_23)
        self.horizontalLayout.addLayout(self.verticalLayout_9)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.label_4.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.splitter.addWidget(self.label_4)
        self.lineEdit_2 = QLineEdit(self.splitter)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(12)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        self.lineEdit_2.setMinimumSize(QSize(20, 20))
        self.lineEdit_2.setSizeIncrement(QSize(9, 0))
        self.lineEdit_2.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.splitter.addWidget(self.lineEdit_2)

        self.verticalLayout_2.addWidget(self.splitter)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 14pt \"Agency FB\";")

        self.verticalLayout_2.addWidget(self.label_3)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setStyleSheet(u"font: 14pt \"Agency FB\";")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.pushButton_3.setAutoDefault(True)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.pushButton.setAutoDefault(True)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setSizeIncrement(QSize(8, 0))
        self.commandLinkButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                             "font: 14pt \"Agency FB\";")
        self.commandLinkButton.setAutoDefault(True)
        self.commandLinkButton.setDefault(True)

        self.horizontalLayout_3.addWidget(self.commandLinkButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1175, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.menubar.setFont(font1)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"font: 11pt \"Agency FB\";")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)
        self.menu.addSeparator()
        self.menu.addAction(self.action_3)

        self.retranslateUi(MainWindow)

        self.pushButton_3.setDefault(True)
        self.pushButton.setDefault(True)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"知识图谱", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u6253\u8d4f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"知识图谱操作平台", None))
        self.label.setText(
            QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u5e38\u7528\u5173\u952e\u8bcd:   ", None))

        # 常用关键词导入数据:
        often_data = search.often()

        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))

        self.lineEdit_2.setText("")
        for i in range(18, 33):
            exec("self.pushButton_{}.setText(QCoreApplication.translate"
                 "('MainWindow', u'{}', None))".format(i, often_data[i - 18]))

            # def click():
            #     print(i)
            #
            # exec("print('def click{}():"
            #      "      self.lineEdit_2.setText(self.pushButton_{}.text())')".format(i, i))
            # exec("self.pushButton_{}.clicked.connect(click)".format(i))

        def click18():
            self.lineEdit_2.setText(self.pushButton_18.text())

        def click19():
            self.lineEdit_2.setText(self.pushButton_19.text())

        def click20():
            self.lineEdit_2.setText(self.pushButton_20.text())

        def click21():
            self.lineEdit_2.setText(self.pushButton_21.text())

        def click22():
            self.lineEdit_2.setText(self.pushButton_22.text())

        def click23():
            self.lineEdit_2.setText(self.pushButton_23.text())

        def click24():
            self.lineEdit_2.setText(self.pushButton_24.text())

        def click25():
            self.lineEdit_2.setText(self.pushButton_25.text())

        def click26():
            self.lineEdit_2.setText(self.pushButton_26.text())

        def click27():
            self.lineEdit_2.setText(self.pushButton_27.text())

        def click28():
            self.lineEdit_2.setText(self.pushButton_28.text())

        def click29():
            self.lineEdit_2.setText(self.pushButton_29.text())

        def click30():
            self.lineEdit_2.setText(self.pushButton_30.text())

        def click31():
            self.lineEdit_2.setText(self.pushButton_31.text())

        def click32():
            self.lineEdit_2.setText(self.pushButton_32.text())

        self.label_4.setText(
            QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5e38\u7528\u5173\u952e\u8bcd:   ", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u5904\uff1a", None))

        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"清空搜索框", None))

        def clear():
            self.lineEdit_2.setText("")

        self.pushButton_3.clicked.connect(clear)

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"清空输出框", None))

        def clear1():
            self.textBrowser.setText("")

        self.pushButton.clicked.connect(clear1)
        self.commandLinkButton.setText(
            QCoreApplication.translate("MainWindow", u"                      \u751f\u6210\u56fe\u8c31", None))

        def command():
            i = self.lineEdit_2.text()
            if i == "":
                create.outputWritten(self, " 搜索关键词为空！！！\n")

            else:
                create.outputWritten(self, "当前搜索关键词为:   {}\n".format(i))
                create.outputWritten(self, " 知识图谱正在构建，请不要连续点击生成！！！\n")
                create.create(self, i)

        self.commandLinkButton.clicked.connect(command)

        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))

        self.pushButton_18.clicked.connect(click18)
        self.pushButton_19.clicked.connect(click19)
        self.pushButton_20.clicked.connect(click20)
        self.pushButton_21.clicked.connect(click21)
        self.pushButton_22.clicked.connect(click22)
        self.pushButton_23.clicked.connect(click23)
        self.pushButton_24.clicked.connect(click24)
        self.pushButton_25.clicked.connect(click25)
        self.pushButton_26.clicked.connect(click26)
        self.pushButton_27.clicked.connect(click27)
        self.pushButton_28.clicked.connect(click28)
        self.pushButton_29.clicked.connect(click29)
        self.pushButton_30.clicked.connect(click30)
        self.pushButton_31.clicked.connect(click31)
        self.pushButton_32.clicked.connect(click32)
    # retranslateUi
