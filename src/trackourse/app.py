import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from BlurWindow.blurWindow import GlobalBlur

import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(500, 400)

        GlobalBlur(self.winId(), hexColor=False, Dark=True, Acrylic=False,QWidget=self)

        self.setWindowTitle("TracKourse")
        # button = QPushButton("Ding")
        # self.setCentralWidget(button)
        self.setFixedSize(QSize(400, 300))
        self.setWindowOpacity(0.8)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
