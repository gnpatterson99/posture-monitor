# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imageMain.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)
import icons.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1102, 1213)
        MainWindow.setMinimumSize(QSize(25, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonAreaWidget = QWidget(self.centralwidget)
        self.buttonAreaWidget.setObjectName(u"buttonAreaWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAreaWidget.sizePolicy().hasHeightForWidth())
        self.buttonAreaWidget.setSizePolicy(sizePolicy)
        self.buttonAreaWidget.setMinimumSize(QSize(100, 0))
        self.verticalLayout = QVBoxLayout(self.buttonAreaWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_up = QPushButton(self.buttonAreaWidget)
        self.pb_up.setObjectName(u"pb_up")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.pb_up.setIcon(icon)

        self.verticalLayout.addWidget(self.pb_up)

        self.pb_down = QPushButton(self.buttonAreaWidget)
        self.pb_down.setObjectName(u"pb_down")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoDown))
        self.pb_down.setIcon(icon1)

        self.verticalLayout.addWidget(self.pb_down)

        self.pb_right = QPushButton(self.buttonAreaWidget)
        self.pb_right.setObjectName(u"pb_right")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.pb_right.setIcon(icon2)

        self.verticalLayout.addWidget(self.pb_right)

        self.pb_left = QPushButton(self.buttonAreaWidget)
        self.pb_left.setObjectName(u"pb_left")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.pb_left.setIcon(icon3)

        self.verticalLayout.addWidget(self.pb_left)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pb_set_date = QPushButton(self.buttonAreaWidget)
        self.pb_set_date.setObjectName(u"pb_set_date")

        self.verticalLayout.addWidget(self.pb_set_date)

        self.dateEdit = QDateEdit(self.buttonAreaWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumDateTime(QDateTime(QDate(2026, 1, 1), QTime(4, 56, 0)))
        self.dateEdit.setMinimumDate(QDate(2026, 1, 1))
        self.dateEdit.setCurrentSection(QDateTimeEdit.Section.DaySection)
        self.dateEdit.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.dateEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pb_exit = QPushButton(self.buttonAreaWidget)
        self.pb_exit.setObjectName(u"pb_exit")

        self.verticalLayout.addWidget(self.pb_exit)


        self.horizontalLayout.addWidget(self.buttonAreaWidget)

        self.displayAreaWidget = QWidget(self.centralwidget)
        self.displayAreaWidget.setObjectName(u"displayAreaWidget")
        self.lw_image = QLabel(self.displayAreaWidget)
        self.lw_image.setObjectName(u"lw_image")
        self.lw_image.setGeometry(QRect(0, 0, 751, 1121))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lw_image.sizePolicy().hasHeightForWidth())
        self.lw_image.setSizePolicy(sizePolicy1)
        self.lw_image.setPixmap(QPixmap(u":/buttons/sampleimage.png"))
        self.lw_image.setScaledContents(False)

        self.horizontalLayout.addWidget(self.displayAreaWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1102, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pb_up.setText("")
        self.pb_down.setText("")
        self.pb_right.setText("")
        self.pb_left.setText("")
        self.pb_set_date.setText(QCoreApplication.translate("MainWindow", u"Set Date", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"MM/dd/yyyy", None))
        self.pb_exit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.lw_image.setText("")
    # retranslateUi

