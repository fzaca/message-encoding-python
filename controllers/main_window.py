from utils.encoding_utils import *

from PySide6.QtWidgets import QWidget

from views.main_window_ui import MainWindow

class MainWindowForm(QWidget, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.encode_button.clicked.connect(self.encode)
        self.decode_button.clicked.connect(self.decode)

    def encode(self):
        message = self.message_input.toPlainText()
        if not message:
            return
        
        algorithm = self.algorithm_combobox.currentText()
        if algorithm == 'Base16':
            key = base16_encode(message)
        elif algorithm == 'Rot13':
            key = rot13_encode(message)
        elif algorithm == 'Delta':
            key = delta_encode(message)
        elif algorithm == 'RLE':
            key = rle_encode(message)
        elif algorithm == 'LZW':
            key = lzw_encode(message)

        self.key_input.setPlainText(key)
        self.message_input.clear()

    def decode(self):
        key = self.key_input.toPlainText()
        if not key:
            return
        
        algorithm = self.algorithm_combobox.currentText()
        if algorithm == 'Base16':
            message = base16_decode(key)
        elif algorithm == 'Rot13':
            message = rot13_decode(key)
        elif algorithm == 'Delta':
            message = delta_decode(key)
        elif algorithm == 'RLE':
            message = rle_decode(key)
        elif algorithm == 'LZW':
            message = lzw_decode(key)

        self.message_input.setPlainText(message)
        self.key_input.clear()