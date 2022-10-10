# -*- coding: utf-8 -*-


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from windows import qrc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(482, 705)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 18pt \"Agency FB\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(1000000, 25))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font: 14pt \"Agency FB\";")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.splitter.addWidget(self.widget)

        self.verticalLayout_2.addWidget(self.splitter)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        icon = QIcon()
        icon.addFile(u":/qrc/admire.jpg", QSize(), QIcon.Normal, QIcon.On)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(303, 427))
        self.toolButton.setAutoRepeatDelay(106)
        self.toolButton.setAutoRepeatInterval(107)

        self.verticalLayout_2.addWidget(self.toolButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 482, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu_2.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"打赏", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6253\u8d4f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8d60\u4eba\u73ab\u7470\uff0c\u624b\u7559\u4f59\u9999", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5236\u4f5c\u4e0d\u6613", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8c22\u8c22", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))

    # retranslateUi

