# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowfWqlrO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import icons_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(935, 750)
        MainWindow.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background:  rgb(154, 148, 196);\n"
"    height: 5px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background:  rgb(154, 148, 196);\n"
"    width: 5px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"color: #fff;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 930, 807))
        self.scrollAreaWidgetContents.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.main_container = QFrame(self.scrollAreaWidgetContents)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setMinimumSize(QSize(0, 0))
        self.main_container.setMaximumSize(QSize(16777215, 16777215))
        self.main_container.setStyleSheet(u"")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.main_container)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.main_container)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 192))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1072, 187))
        self.scrollAreaWidgetContents_5.setMaximumSize(QSize(16777215, 665))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.weather_forecast_frame = QFrame(self.scrollAreaWidgetContents_5)
        self.weather_forecast_frame.setObjectName(u"weather_forecast_frame")
        self.weather_forecast_frame.setStyleSheet(u"QFrame{border-top: 2px solid rgb(154, 148, 196)}")
        self.weather_forecast_frame.setFrameShape(QFrame.StyledPanel)
        self.weather_forecast_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.weather_forecast_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_8 = QFrame(self.weather_forecast_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.forecast_temp1 = QLabel(self.frame_8)
        self.forecast_temp1.setObjectName(u"forecast_temp1")
        self.forecast_temp1.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"Adobe Caslon Pro")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.forecast_temp1.setFont(font)
        self.forecast_temp1.setStyleSheet(u"color: rgb(173, 167, 220);border: none;")

        self.gridLayout_7.addWidget(self.forecast_temp1, 1, 1, 1, 1)

        self.forecast_icon1 = QLabel(self.frame_8)
        self.forecast_icon1.setObjectName(u"forecast_icon1")
        self.forecast_icon1.setMinimumSize(QSize(50, 50))
        self.forecast_icon1.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setPointSize(2)
        self.forecast_icon1.setFont(font1)
        self.forecast_icon1.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon1.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon1.setScaledContents(True)

        self.gridLayout_7.addWidget(self.forecast_icon1, 1, 0, 1, 1)

        self.forecast_time1 = QLabel(self.frame_8)
        self.forecast_time1.setObjectName(u"forecast_time1")
        self.forecast_time1.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamily(u"Adobe Caslon Pro")
        font2.setPointSize(12)
        self.forecast_time1.setFont(font2)
        self.forecast_time1.setStyleSheet(u"border: none;")
        self.forecast_time1.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.forecast_time1, 0, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.weather_forecast_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_9)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.forecast_temp2 = QLabel(self.frame_9)
        self.forecast_temp2.setObjectName(u"forecast_temp2")
        self.forecast_temp2.setMinimumSize(QSize(0, 30))
        self.forecast_temp2.setFont(font)
        self.forecast_temp2.setStyleSheet(u"color: rgb(173, 167, 220);border: none;")

        self.gridLayout_8.addWidget(self.forecast_temp2, 1, 1, 1, 1)

        self.forecast_icon2 = QLabel(self.frame_9)
        self.forecast_icon2.setObjectName(u"forecast_icon2")
        self.forecast_icon2.setMinimumSize(QSize(50, 50))
        self.forecast_icon2.setMaximumSize(QSize(50, 50))
        self.forecast_icon2.setFont(font1)
        self.forecast_icon2.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon2.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon2.setScaledContents(True)

        self.gridLayout_8.addWidget(self.forecast_icon2, 1, 0, 1, 1)

        self.forecast_time2 = QLabel(self.frame_9)
        self.forecast_time2.setObjectName(u"forecast_time2")
        self.forecast_time2.setMinimumSize(QSize(0, 30))
        self.forecast_time2.setFont(font2)
        self.forecast_time2.setStyleSheet(u"border: none;")
        self.forecast_time2.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.forecast_time2, 0, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.weather_forecast_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.forecast_temp3 = QLabel(self.frame_10)
        self.forecast_temp3.setObjectName(u"forecast_temp3")
        self.forecast_temp3.setMinimumSize(QSize(0, 30))
        self.forecast_temp3.setFont(font)
        self.forecast_temp3.setStyleSheet(u"color: rgb(173, 167, 220);border: none;")

        self.gridLayout_9.addWidget(self.forecast_temp3, 1, 1, 1, 1)

        self.forecast_icon3 = QLabel(self.frame_10)
        self.forecast_icon3.setObjectName(u"forecast_icon3")
        self.forecast_icon3.setMinimumSize(QSize(50, 50))
        self.forecast_icon3.setMaximumSize(QSize(50, 50))
        self.forecast_icon3.setFont(font1)
        self.forecast_icon3.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon3.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon3.setScaledContents(True)

        self.gridLayout_9.addWidget(self.forecast_icon3, 1, 0, 1, 1)

        self.forecast_time3 = QLabel(self.frame_10)
        self.forecast_time3.setObjectName(u"forecast_time3")
        self.forecast_time3.setMinimumSize(QSize(0, 30))
        self.forecast_time3.setFont(font2)
        self.forecast_time3.setStyleSheet(u"border: none;")
        self.forecast_time3.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.forecast_time3, 0, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.weather_forecast_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_11)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.forecast_icon4 = QLabel(self.frame_11)
        self.forecast_icon4.setObjectName(u"forecast_icon4")
        self.forecast_icon4.setMinimumSize(QSize(50, 50))
        self.forecast_icon4.setMaximumSize(QSize(50, 50))
        self.forecast_icon4.setFont(font1)
        self.forecast_icon4.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon4.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon4.setScaledContents(True)

        self.gridLayout_10.addWidget(self.forecast_icon4, 1, 0, 1, 1)

        self.forecast_temp4 = QLabel(self.frame_11)
        self.forecast_temp4.setObjectName(u"forecast_temp4")
        self.forecast_temp4.setMinimumSize(QSize(0, 30))
        self.forecast_temp4.setFont(font)
        self.forecast_temp4.setStyleSheet(u"color: rgb(173, 167, 220);border: none;")

        self.gridLayout_10.addWidget(self.forecast_temp4, 1, 1, 1, 1)

        self.forecast_time4 = QLabel(self.frame_11)
        self.forecast_time4.setObjectName(u"forecast_time4")
        self.forecast_time4.setMinimumSize(QSize(0, 30))
        self.forecast_time4.setFont(font2)
        self.forecast_time4.setStyleSheet(u"border: none;")
        self.forecast_time4.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.forecast_time4, 0, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.weather_forecast_frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"padding: 10px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_12)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.forecast_temp5 = QLabel(self.frame_12)
        self.forecast_temp5.setObjectName(u"forecast_temp5")
        self.forecast_temp5.setMinimumSize(QSize(0, 30))
        self.forecast_temp5.setFont(font)
        self.forecast_temp5.setStyleSheet(u"color: rgb(173, 167, 220);\n"
"border: none;")

        self.gridLayout_11.addWidget(self.forecast_temp5, 1, 1, 1, 1)

        self.forecast_icon5 = QLabel(self.frame_12)
        self.forecast_icon5.setObjectName(u"forecast_icon5")
        self.forecast_icon5.setMinimumSize(QSize(50, 50))
        self.forecast_icon5.setMaximumSize(QSize(50, 50))
        self.forecast_icon5.setFont(font1)
        self.forecast_icon5.setStyleSheet(u"border: none;\n"
"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 25px;\n"
"color: rgb(252, 191, 130);")
        self.forecast_icon5.setPixmap(QPixmap(u":/weather/icons/weather/png/030-weather app.png"))
        self.forecast_icon5.setScaledContents(True)

        self.gridLayout_11.addWidget(self.forecast_icon5, 1, 0, 1, 1)

        self.forecast_time5 = QLabel(self.frame_12)
        self.forecast_time5.setObjectName(u"forecast_time5")
        self.forecast_time5.setMinimumSize(QSize(0, 30))
        self.forecast_time5.setFont(font2)
        self.forecast_time5.setStyleSheet(u"border: none;")

        self.gridLayout_11.addWidget(self.forecast_time5, 0, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_12)


        self.verticalLayout.addWidget(self.weather_forecast_frame, 0, Qt.AlignTop)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_4.addWidget(self.scrollArea_2, 8, 0, 1, 1)

        self.label_7 = QLabel(self.main_container)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setFamily(u"Adobe Garamond Pro Bold")
        font3.setPointSize(12)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"border: none;\n"
"color: rgb(252, 192, 125)")

        self.gridLayout_4.addWidget(self.label_7, 7, 0, 1, 1)

        self.progressBar = QProgressBar(self.main_container)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setMinimumSize(QSize(0, 10))
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	color: rgb(255, 0, 0)\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.494, stop:0 rgba(252, 192, 125, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius: 5px;\n"
"}")
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)

        self.gridLayout_4.addWidget(self.progressBar, 4, 0, 1, 1)

        self.top_frame_2 = QFrame(self.main_container)
        self.top_frame_2.setObjectName(u"top_frame_2")
        self.top_frame_2.setMinimumSize(QSize(0, 62))
        self.top_frame_2.setMaximumSize(QSize(16777215, 62))
        self.top_frame_2.setStyleSheet(u"")
        self.top_frame_2.setFrameShape(QFrame.StyledPanel)
        self.top_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.top_frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.top_frame_2)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setFamily(u"Open Sans Extrabold")
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"color: rgb(252, 192, 125)")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1, Qt.AlignTop)

        self.weather_location = QLabel(self.top_frame_2)
        self.weather_location.setObjectName(u"weather_location")
        font5 = QFont()
        font5.setFamily(u"Adobe Kaiti Std R")
        font5.setPointSize(13)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.weather_location.setFont(font5)
        self.weather_location.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.weather_location, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.top_frame_2, 3, 0, 1, 1)

        self.label_18 = QLabel(self.main_container)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"border: none;\n"
"color: rgb(252, 192, 125)")

        self.gridLayout_4.addWidget(self.label_18, 1, 0, 1, 1)

        self.header_frame = QFrame(self.main_container)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"	background-color: rgb(27, 29, 35);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_20 = QLabel(self.header_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(80, 80))
        self.label_20.setMaximumSize(QSize(80, 80))
        font6 = QFont()
        font6.setPointSize(12)
        self.label_20.setFont(font6)
        self.label_20.setPixmap(QPixmap(u":/weather/icons/weather/png/028-wind vane.png"))
        self.label_20.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_20, 0, Qt.AlignHCenter)

        self.label_19 = QLabel(self.header_frame)
        self.label_19.setObjectName(u"label_19")
        font7 = QFont()
        font7.setFamily(u"Adobe Garamond Pro Bold")
        font7.setPointSize(25)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_19.setFont(font7)
        self.label_19.setStyleSheet(u"border: none;\n"
"color: rgb(252, 192, 125)")

        self.horizontalLayout_3.addWidget(self.label_19)


        self.gridLayout_4.addWidget(self.header_frame, 0, 0, 1, 1)

        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(882, 62))
        self.top_frame.setMaximumSize(QSize(16777215, 62))
        self.top_frame.setStyleSheet(u"border-bottom: 2px solid rgb(154, 148, 196)")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.top_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.countries_list = QComboBox(self.top_frame)
        self.countries_list.setObjectName(u"countries_list")
        font8 = QFont()
        font8.setFamily(u"Sitka Banner")
        font8.setPointSize(14)
        self.countries_list.setFont(font8)
        self.countries_list.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(103, 103, 103);\n"
"border-radius: 10px;\n"
"color: rgb(252, 191, 130);")

        self.gridLayout.addWidget(self.countries_list, 1, 3, 1, 1)

        self.continents_list = QComboBox(self.top_frame)
        self.continents_list.setObjectName(u"continents_list")
        self.continents_list.setFont(font8)
        self.continents_list.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(103, 103, 103);\n"
"border-radius: 10px;\n"
"color: rgb(252, 191, 130);")

        self.gridLayout.addWidget(self.continents_list, 1, 1, 1, 1)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font8)
        self.label.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(252, 192, 125);\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(self.top_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font8)
        self.label_3.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(252, 192, 125);\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_2 = QLabel(self.top_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font8)
        self.label_2.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(252, 192, 125);\n"
"border-radius: 10px;")

        self.gridLayout.addWidget(self.label_2, 1, 4, 1, 1)

        self.cities_list = QComboBox(self.top_frame)
        self.cities_list.setObjectName(u"cities_list")
        self.cities_list.setFont(font8)
        self.cities_list.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(103, 103, 103);\n"
"border-radius: 10px;\n"
"color: rgb(252, 191, 130);")

        self.gridLayout.addWidget(self.cities_list, 1, 5, 1, 1)


        self.gridLayout_4.addWidget(self.top_frame, 2, 0, 1, 1)

        self.frame = QFrame(self.main_container)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{border-top: 2px solid rgb(154, 148, 196)}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"border: none;\n"
"color: rgb(252, 192, 125)")

        self.verticalLayout_2.addWidget(self.label_5, 0, Qt.AlignLeft|Qt.AlignTop)

        self.middle_frame = QFrame(self.frame)
        self.middle_frame.setObjectName(u"middle_frame")
        self.middle_frame.setStyleSheet(u"border: none;")
        self.middle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.middle_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_6 = QFrame(self.middle_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(200, 200))
        self.frame_6.setMaximumSize(QSize(200, 200))
        self.frame_6.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 100px;\n"
"color: rgb(252, 191, 130);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.current_weather_icon = QLabel(self.frame_6)
        self.current_weather_icon.setObjectName(u"current_weather_icon")
        self.current_weather_icon.setMinimumSize(QSize(100, 100))
        self.current_weather_icon.setMaximumSize(QSize(100, 100))
        self.current_weather_icon.setStyleSheet(u"border: none;\n"
"background: none;")
        self.current_weather_icon.setPixmap(QPixmap(u":/weather/icons/weather/png/027-location.png"))
        self.current_weather_icon.setScaledContents(True)
        self.current_weather_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.current_weather_icon)

        self.current_weather_label = QLabel(self.frame_6)
        self.current_weather_label.setObjectName(u"current_weather_label")
        self.current_weather_label.setFont(font2)
        self.current_weather_label.setStyleSheet(u"border: none;\n"
"padding: 15px;\n"
"background: none;")
        self.current_weather_label.setAlignment(Qt.AlignCenter)
        self.current_weather_label.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.current_weather_label)


        self.horizontalLayout_2.addWidget(self.frame_6, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_3 = QFrame(self.middle_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"padding: 10px;\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(50, 50))
        self.label_12.setMaximumSize(QSize(50, 50))
        self.label_12.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_12.setPixmap(QPixmap(u":/weather/icons/weather/png/031-weather forecast.png"))
        self.label_12.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(50, 50))
        self.label_8.setMaximumSize(QSize(50, 50))
        self.label_8.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_8.setPixmap(QPixmap(u":/weather/icons/weather/png/031-weather forecast.png"))
        self.label_8.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.latitude_label1 = QLabel(self.frame_3)
        self.latitude_label1.setObjectName(u"latitude_label1")
        self.latitude_label1.setMinimumSize(QSize(0, 30))
        self.latitude_label1.setFont(font2)

        self.gridLayout_3.addWidget(self.latitude_label1, 1, 1, 1, 1)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(50, 50))
        self.label_13.setMaximumSize(QSize(50, 50))
        self.label_13.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_13.setPixmap(QPixmap(u":/weather/icons/weather/png/001-cloudy day.png"))
        self.label_13.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)

        self.longitude_label = QLabel(self.frame_3)
        self.longitude_label.setObjectName(u"longitude_label")
        self.longitude_label.setMinimumSize(QSize(0, 30))
        self.longitude_label.setFont(font)
        self.longitude_label.setStyleSheet(u"color: rgb(173, 167, 220);")

        self.gridLayout_3.addWidget(self.longitude_label, 0, 2, 1, 1)

        self.sunrise_label1 = QLabel(self.frame_3)
        self.sunrise_label1.setObjectName(u"sunrise_label1")
        self.sunrise_label1.setMinimumSize(QSize(0, 30))
        self.sunrise_label1.setFont(font2)

        self.gridLayout_3.addWidget(self.sunrise_label1, 2, 1, 1, 1)

        self.current_weather_label_8 = QLabel(self.frame_3)
        self.current_weather_label_8.setObjectName(u"current_weather_label_8")
        self.current_weather_label_8.setMinimumSize(QSize(0, 30))
        self.current_weather_label_8.setFont(font2)

        self.gridLayout_3.addWidget(self.current_weather_label_8, 0, 1, 1, 1)

        self.latitude_label = QLabel(self.frame_3)
        self.latitude_label.setObjectName(u"latitude_label")
        self.latitude_label.setMinimumSize(QSize(0, 30))
        self.latitude_label.setFont(font)
        self.latitude_label.setStyleSheet(u"color: rgb(173, 167, 220);")

        self.gridLayout_3.addWidget(self.latitude_label, 1, 2, 1, 1)

        self.sunrise_label = QLabel(self.frame_3)
        self.sunrise_label.setObjectName(u"sunrise_label")
        self.sunrise_label.setMinimumSize(QSize(0, 30))
        self.sunrise_label.setFont(font)
        self.sunrise_label.setStyleSheet(u"color: rgb(173, 167, 220);")

        self.gridLayout_3.addWidget(self.sunrise_label, 2, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.middle_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"padding: 10px;\n"
"border-radius: 20px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(50, 50))
        font9 = QFont()
        font9.setPointSize(42)
        self.label_9.setFont(font9)
        self.label_9.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_9.setPixmap(QPixmap(u":/weather/icons/weather/png/007-windy.png"))
        self.label_9.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_9, 0, 0, 1, 1)

        self.wind_speed_label1 = QLabel(self.frame_7)
        self.wind_speed_label1.setObjectName(u"wind_speed_label1")
        self.wind_speed_label1.setFont(font2)

        self.gridLayout_6.addWidget(self.wind_speed_label1, 0, 1, 1, 1)

        self.wind_speed_label = QLabel(self.frame_7)
        self.wind_speed_label.setObjectName(u"wind_speed_label")
        self.wind_speed_label.setFont(font)
        self.wind_speed_label.setStyleSheet(u"color: rgb(173, 167, 220);")

        self.gridLayout_6.addWidget(self.wind_speed_label, 0, 2, 1, 1)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(50, 50))
        self.label_10.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_10.setPixmap(QPixmap(u":/weather/icons/weather/png/024-temperature.png"))
        self.label_10.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_10, 1, 0, 1, 1)

        self.current_weather_label_3 = QLabel(self.frame_7)
        self.current_weather_label_3.setObjectName(u"current_weather_label_3")
        self.current_weather_label_3.setFont(font2)

        self.gridLayout_6.addWidget(self.current_weather_label_3, 1, 1, 1, 1)

        self.temperature_label = QLabel(self.frame_7)
        self.temperature_label.setObjectName(u"temperature_label")
        self.temperature_label.setFont(font)
        self.temperature_label.setStyleSheet(u"color: rgb(173, 167, 220);")

        self.gridLayout_6.addWidget(self.temperature_label, 1, 2, 1, 1)

        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(50, 50))
        self.label_11.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_11.setPixmap(QPixmap(u":/weather/icons/weather/png/019-low tide.png"))
        self.label_11.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_11, 2, 0, 1, 1)

        self.current_weather_label_6 = QLabel(self.frame_7)
        self.current_weather_label_6.setObjectName(u"current_weather_label_6")
        self.current_weather_label_6.setFont(font2)

        self.gridLayout_6.addWidget(self.current_weather_label_6, 2, 1, 1, 1)

        self.pressure_label = QLabel(self.frame_7)
        self.pressure_label.setObjectName(u"pressure_label")
        self.pressure_label.setFont(font)
        self.pressure_label.setStyleSheet(u"color: rgb(159, 145, 188);")

        self.gridLayout_6.addWidget(self.pressure_label, 2, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.middle_frame, 0, Qt.AlignTop)


        self.gridLayout_4.addWidget(self.frame, 6, 0, 1, 1)

        self.message_frame = QFrame(self.main_container)
        self.message_frame.setObjectName(u"message_frame")
        self.message_frame.setMinimumSize(QSize(0, 0))
        self.message_frame.setFrameShape(QFrame.StyledPanel)
        self.message_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.message_frame)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.message_label = QLabel(self.message_frame)
        self.message_label.setObjectName(u"message_label")
        font10 = QFont()
        font10.setPointSize(12)
        font10.setItalic(False)
        self.message_label.setFont(font10)
        self.message_label.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.message_label.setScaledContents(True)
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setWordWrap(True)
        self.message_label.setMargin(5)

        self.verticalLayout_5.addWidget(self.message_label)

        self.retryButton = QPushButton(self.message_frame)
        self.retryButton.setObjectName(u"retryButton")
        font11 = QFont()
        font11.setPointSize(12)
        font11.setBold(True)
        font11.setWeight(75)
        self.retryButton.setFont(font11)
        self.retryButton.setStyleSheet(u"padding: 5px;\n"
"border: 1px solid rgb(255, 0, 0);\n"
"background-color:rgb(252, 192, 125);\n"
"border-radius: 10px;")

        self.verticalLayout_5.addWidget(self.retryButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_4.addWidget(self.message_frame, 5, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.main_container)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.forecast_temp1.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon1.setText("")
        self.forecast_time1.setText(QCoreApplication.translate("MainWindow", u"+3 Hours", None))
        self.forecast_temp2.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon2.setText("")
        self.forecast_time2.setText(QCoreApplication.translate("MainWindow", u"+6 Hours", None))
        self.forecast_temp3.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon3.setText("")
        self.forecast_time3.setText(QCoreApplication.translate("MainWindow", u"+9 Hours", None))
        self.forecast_icon4.setText("")
        self.forecast_temp4.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_time4.setText(QCoreApplication.translate("MainWindow", u"+12 Hours", None))
        self.forecast_temp5.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.forecast_icon5.setText("")
        self.forecast_time5.setText(QCoreApplication.translate("MainWindow", u"+15 Hours", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Forecast", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Showing Weather Information For:", None))
        self.weather_location.setText(QCoreApplication.translate("MainWindow", u"Loading weather location", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Select weather location", None))
        self.label_20.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Spinn Design Weather App", None))
        self.continents_list.setCurrentText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Continent", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Select Country", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Select City", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Current Weather:", None))
        self.current_weather_icon.setText("")
        self.current_weather_label.setText(QCoreApplication.translate("MainWindow", u"Please wait.. ", None))
        self.label_12.setText("")
        self.label_8.setText("")
        self.latitude_label1.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.label_13.setText("")
        self.longitude_label.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.sunrise_label1.setText(QCoreApplication.translate("MainWindow", u"Sunrise", None))
        self.current_weather_label_8.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        self.latitude_label.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.sunrise_label.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.label_9.setText("")
        self.wind_speed_label1.setText(QCoreApplication.translate("MainWindow", u"Wind Speed ", None))
        self.wind_speed_label.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.label_10.setText("")
        self.current_weather_label_3.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.temperature_label.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.label_11.setText("")
        self.current_weather_label_6.setText(QCoreApplication.translate("MainWindow", u"Pressure", None))
        self.pressure_label.setText(QCoreApplication.translate("MainWindow", u"Please wait..", None))
        self.message_label.setText(QCoreApplication.translate("MainWindow", u"Weather response messages", None))
        self.retryButton.setText(QCoreApplication.translate("MainWindow", u"Re-try", None))
    # retranslateUi

