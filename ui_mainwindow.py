# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 600)
        MainWindow.setMinimumSize(QSize(1400, 600))
        MainWindow.setMaximumSize(QSize(1400, 600))
        self.ActionOpenFile = QAction(MainWindow)
        self.ActionOpenFile.setObjectName(u"ActionOpenFile")
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.gridLayout = QGridLayout(self.CentralWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.WidgetImage = QGraphicsView(self.CentralWidget)
        self.WidgetImage.setObjectName(u"WidgetImage")
        self.WidgetImage.setMinimumSize(QSize(512, 512))
        self.WidgetImage.setMaximumSize(QSize(512, 512))

        self.gridLayout.addWidget(self.WidgetImage, 0, 0, 1, 1)

        self.WidgetMask = QGraphicsView(self.CentralWidget)
        self.WidgetMask.setObjectName(u"WidgetMask")
        self.WidgetMask.setMinimumSize(QSize(512, 512))
        self.WidgetMask.setMaximumSize(QSize(512, 512))

        self.gridLayout.addWidget(self.WidgetMask, 0, 1, 1, 1)

        self.WidgetProbability = QLabel(self.CentralWidget)
        self.WidgetProbability.setObjectName(u"WidgetProbability")
        self.WidgetProbability.setMinimumSize(QSize(256, 512))
        self.WidgetProbability.setMaximumSize(QSize(256, 512))

        self.gridLayout.addWidget(self.WidgetProbability, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.CentralWidget)
        self.MenuBar = QMenuBar(MainWindow)
        self.MenuBar.setObjectName(u"MenuBar")
        self.MenuBar.setGeometry(QRect(0, 0, 1400, 33))
        self.MenuFile = QMenu(self.MenuBar)
        self.MenuFile.setObjectName(u"MenuFile")
        MainWindow.setMenuBar(self.MenuBar)

        self.MenuBar.addAction(self.MenuFile.menuAction())
        self.MenuFile.addAction(self.ActionOpenFile)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Brain Cancer Detection", None))
        self.ActionOpenFile.setText(QCoreApplication.translate("MainWindow", u"Open File...", None))
        self.WidgetProbability.setText("")
        self.MenuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

