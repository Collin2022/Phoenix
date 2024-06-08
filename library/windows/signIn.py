# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signIn.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(346, 192)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 331, 80))
        self.layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.label = QVBoxLayout()
        self.label.setObjectName(u"label")
        self.usernameLabel = QLabel(self.horizontalLayoutWidget)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.label.addWidget(self.usernameLabel)

        self.passwordLabel = QLabel(self.horizontalLayoutWidget)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.label.addWidget(self.passwordLabel)


        self.layout.addLayout(self.label)

        self.entry = QVBoxLayout()
        self.entry.setObjectName(u"entry")
        self.usernameEntry = QLineEdit(self.horizontalLayoutWidget)
        self.usernameEntry.setObjectName(u"usernameEntry")

        self.entry.addWidget(self.usernameEntry)

        self.passwordEntry = QLineEdit(self.horizontalLayoutWidget)
        self.passwordEntry.setObjectName(u"passwordEntry")

        self.entry.addWidget(self.passwordEntry)


        self.layout.addLayout(self.entry)

        self.button = QPushButton(self.centralwidget)
        self.button.setObjectName(u"button")
        self.button.setGeometry(QRect(110, 90, 92, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 346, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.button.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
    # retranslateUi

