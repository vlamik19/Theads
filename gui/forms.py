from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from lib.threads import Threads


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = loadUi('MainWindow.ui')
        self._ui.pushButton.clicked.connect(self.on_click)

    def open(self):
        self._ui.show()

    def on_click(self):
        path = self._ui.lineEdit.text()
        if path != '':
            threads = Threads(path)
            threads.start()
            QMessageBox.information(self, 'Сообщения', 'Приложение запущено!')
        else:
            QMessageBox.warning(self, 'Предупреждение', 'Пустое поле ввода')




