# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inquier_weather.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cmb_theme = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_theme.setObjectName("cmb_theme")
        self.horizontalLayout_2.addWidget(self.cmb_theme)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.cmb_province = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_province.setObjectName("cmb_province")
        self.horizontalLayout.addWidget(self.cmb_province)
        self.cmb_city = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_city.setObjectName("cmb_city")
        self.horizontalLayout.addWidget(self.cmb_city)
        self.cmb_county = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_county.setObjectName("cmb_county")
        self.horizontalLayout.addWidget(self.cmb_county)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.txt_info_dis = QtWidgets.QTextBrowser(self.centralwidget)
        self.txt_info_dis.setObjectName("txt_info_dis")
        self.verticalLayout.addWidget(self.txt_info_dis)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check.setObjectName("btn_check")
        self.gridLayout.addWidget(self.btn_check, 0, 0, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "查询城市天气"))
        self.label_2.setText(_translate("MainWindow", "Theme"))
        self.radioButton_2.setText(_translate("MainWindow", "省份"))
        self.btn_check.setText(_translate("MainWindow", "查询"))
        self.btn_clear.setText(_translate("MainWindow", "清空"))

