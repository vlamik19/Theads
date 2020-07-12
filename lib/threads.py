from threading import Thread
from os import system


class Threads(Thread):

    def __init__(self, window):
        super().__init__()
        self._window = window

    @property
    def window(self):
        return self._window

    def run(self):
        if self._window != '':
            print(f'Запуск потока {self._window}')
            system(self._window)
            print(f'Поток {self._window} завершил свою работу')

