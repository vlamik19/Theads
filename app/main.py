from gui.forms import MainWindow
from PyQt5.QtWidgets import QApplication
from sys import exit


if __name__ == '__main__':

    app = QApplication([])
    win = MainWindow()
    win.open()
    exit(app.exec())