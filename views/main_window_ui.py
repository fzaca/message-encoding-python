# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setGeometry(QRect(0, 0, 431, 258))
        self.message_input = QTextEdit(self.centralwidget)
        self.message_input.setObjectName(u"message_input")
        self.message_input.setGeometry(QRect(20, 20, 200, 200))
        self.message_label = QLabel(self.centralwidget)
        self.message_label.setObjectName(u"message_label")
        self.message_label.setGeometry(QRect(20, 0, 200, 16))
        self.key_input = QTextEdit(self.centralwidget)
        self.key_input.setObjectName(u"key_input")
        self.key_input.setGeometry(QRect(230, 20, 200, 200))
        self.key_label = QLabel(self.centralwidget)
        self.key_label.setObjectName(u"key_label")
        self.key_label.setGeometry(QRect(230, 0, 200, 16))
        self.encrypt_button = QPushButton(self.centralwidget)
        self.encrypt_button.setObjectName(u"encrypt_button")
        self.encrypt_button.setGeometry(QRect(20, 230, 93, 28))
        self.decrypt_button = QPushButton(self.centralwidget)
        self.decrypt_button.setObjectName(u"decrypt_button")
        self.decrypt_button.setGeometry(QRect(120, 230, 93, 28))
        self.algorithm_combobox = QComboBox(self.centralwidget)
        self.algorithm_combobox.addItem("")
        self.algorithm_combobox.addItem("")
        self.algorithm_combobox.addItem("")
        self.algorithm_combobox.setObjectName(u"algorithm_combobox")
        self.algorithm_combobox.setGeometry(QRect(240, 230, 191, 26))
        self.algorithm_combobox.setEditable(False)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Encriptador/Desencriptador", None))
        self.message_label.setText(QCoreApplication.translate("MainWindow", u"Mensaje:", None))
        self.key_label.setText(QCoreApplication.translate("MainWindow", u"Clave:", None))
        self.encrypt_button.setText(QCoreApplication.translate("MainWindow", u"Encriptar", None))
        self.decrypt_button.setText(QCoreApplication.translate("MainWindow", u"Desencriptar", None))
        self.algorithm_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Algoritmo 1", None))
        self.algorithm_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Algoritmo 2", None))
        self.algorithm_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Algoritmo 3", None))

    # retranslateUi

