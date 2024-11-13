# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 741, 491))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 3, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")

        self.gridLayout.addWidget(self.plainTextEdit_2, 2, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.plainTextEdit_5 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setMinimumSize(QSize(0, 70))

        self.gridLayout.addWidget(self.plainTextEdit_5, 4, 4, 1, 1, Qt.AlignVCenter)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 6, 4, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.plainTextEdit_4 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")

        self.gridLayout.addWidget(self.plainTextEdit_4, 2, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.plainTextEdit_1 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_1.setObjectName(u"plainTextEdit_1")

        self.gridLayout.addWidget(self.plainTextEdit_1, 4, 1, 1, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.gridLayout.addWidget(self.plainTextEdit_3, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 4, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Nombre", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Apellido", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Correo", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Agregar Propietario", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Tel/Cel", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Documento Identidad", None))
    # retranslateUi

