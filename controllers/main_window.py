from PySide6.QtWidgets import QWidget

from views.main_window_ui import MainWindow

class MainWindowForm(QWidget, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def hello(self):
        print('Hello World')