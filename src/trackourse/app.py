import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(500, 400)

        class_code_label = QLabel(text="Class Code")
        class_code_field = QLineEdit()
        class_code_submit = QPushButton("Submit")

        layout = QGridLayout(self)

        layout.addWidget(class_code_label, 1, 1)
        layout.addWidget(class_code_field, 1, 2)
        layout.addWidget(class_code_submit, 1, 3)

        self.setWindowTitle("TracKourse")
        # self.setWindowIcon('WillGetToLater')

        # button = QPushButton("Ding")
        # self.setCentralWidget(button)
        self.setFixedSize(QSize(400, 300))
        self.setWindowOpacity(0.95)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
