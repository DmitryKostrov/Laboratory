from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(400, 241)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(9, 9, 381, 221))
        self.frame.setStyleSheet("QFrame \n"
        "{\n"
        "    border-radius: 10px;\n"
        "    background-color: rgb(60, 56, 72);\n"
        "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt = QtWidgets.QPushButton(self.frame)
        self.bt.setGeometry(QtCore.QRect(120, 160, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bt.setFont(font)
        self.bt.setMouseTracking(False)
        self.bt.setStyleSheet("QPushButton{\n"
        "    border-radius: 15px;\n"
        "    background-color: rgb(255, 255, 255);\n"
        "    color: black;\n"
        "}")
        self.bt.setObjectName("bt")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(40, 90, 301, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
        "    background-color: rgb(124, 113, 116);\n"
        "    border-radius: 10px;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QProgressBar::chunk{\n"
        "    border-radius: 10px;\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, x2:0, stop:0\n"
        "rgba(201, 87, 149, 255), stop:1 rgba(179, 65, 244,255));\n"
        "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(218, 30, 204, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 40, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStatusTip("")
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lb_info = QtWidgets.QLabel(self.frame)
        self.lb_info.setGeometry(QtCore.QRect(80, 130, 231, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(10)
        self.lb_info.setFont(font)
        self.lb_info.setStyleSheet("color: rgb(255, 255, 255);")
        self.lb_info.setText("")
        self.lb_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_info.setObjectName("lb_info")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bt.setText(_translate("Form", "ЗАПУСТИТЬ"))
        self.label.setText(_translate("Form", "PROGRESS BAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
