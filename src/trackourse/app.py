import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from BlurWindow.blurWindow import blur

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.setWindowTitle("TracKourse")
        # button = QPushButton("Ding")
        # self.setCentralWidget(button)
        self.setFixedSize(QSize(400, 300))
        self.setWindowOpacity(0.8)
        self.blur = QGraphicsBlurEffect()
        self.blur.setBlurRadius(10)
        self.setGraphicsEffect(self.blur)

        self.setLayout(layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
