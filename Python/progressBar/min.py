import sys
import time
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from main import*

class ProgressHandler(QtCore.QThread):
    mysignle = QtCore.pyqtSignal(list)

    def run(self):
        for step in range(0, 101):
            self.mysignle.emit(["progress_increment", step])
            time.sleep(0.03)

class Interface(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Создание экземпляра класса с потоком и его обработчиком
        self.handler = ProgressHandler()
        self.handler.mysignle.connect(self.signal_handler)

        # Удаление Windows рамки и создание обработчика кнопки
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.bt.clicked.connect(lambda: self.ui.progressBar.setValue(0))
        self.ui.bt.clicked.connect(lambda: self.handler.start())

    def signal_handler(self, value):
        fake_data = [
            "Loading resources", "Authentication in progress", "Key verification", "Creating an active session"
        ]
        if value[1] == 100:
            self.ui.lb_info.setText("Progress completed successfully")
            return

        if value[0] == "progress_increment":
            current_value = self.ui.progressBar.value()
            self.ui.progressBar.setValue(current_value + 1)

            if value[1] % 25 == 0:
                random_data = random.choice(fake_data)
                self.ui.lb_info.setText(random_data)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Interface()
    win.show()
    sys.exit(app.exec_())