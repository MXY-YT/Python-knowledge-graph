# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(670, 341)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 75 16pt \"Arial\";")

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter | Qt.AlignVCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"Agency FB\";")

        self.verticalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt \"Agency FB\";")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 12pt \"Agency FB\";")

        self.verticalLayout.addWidget(self.label_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 670, 26))

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"关于", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"                          \u4e00\u5207\u89e3\u91ca\u6743\u5f52\u6d1b\u5c18\u4e91\u5929\u6240\u6709\uff0c\u82e5\u6709\u96f7\u540c\uff0c\u7eaf\u5c5e\u5de7\u5408\u3002",
                                                      None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"                                                             Email: 1578770127@qq.com",
                                                        None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"                                                                         \u611f\u8c22\u5927\u5bb6",
                                                        None))

    # retranslateUi
