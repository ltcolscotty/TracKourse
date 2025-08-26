import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(500, 400)

        self.setWindowTitle("TracKourse")
        # self.setWindowIcon('WillGetToLater')

        button = QPushButton("Ding")
        self.setCentralWidget(button)
        self.setFixedSize(QSize(400, 300))
        self.setWindowOpacity(0.95)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
