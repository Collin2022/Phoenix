# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'active.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit, QMessageBox, 
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.licenseEntry = QTextEdit(self.centralwidget)
        self.licenseEntry.setObjectName(u"licenseEntry")
        self.licenseEntry.setGeometry(QRect(0, 110, 801, 231))
        self.active = QPushButton(self.centralwidget)
        self.active.setObjectName(u"active")
        self.active.setGeometry(QRect(350, 380, 92, 28))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 201, 19))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 671, 19))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.active.setText(QCoreApplication.translate("MainWindow", u"\u6fc0\u6d3b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6fc0\u6d3b\u79d8\u94a5", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4f8b\uff1a--LICENSE--   XXXX-XXXX-XXXX-XXXX  XXXX-XXXX-XXXX-XXXX XXXX-XXXX-XXXX-XXXX", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication()
    window = Ui_MainWindow()
    window.show()
    app.exec()