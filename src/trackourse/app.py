import sys
import os

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from nonmodify.frontend_helper import *

def createClassListing(ID) -> QWidget:

    widget = QWidget()
    layout = QGridLayout(widget)

    text = QLabel(str(ID))
    removeButton = QPushButton("Remove")
    layout.addWidget(text, 1, 1)
    layout.addWidget(removeButton, 1, 2)

    return widget


class CurrentList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        layout = QStackedLayout(self)
        self.setStyleSheet("border: 2px solid white; border-radius: 5px;")
        classes = get_current_classes()
        for classCode in classes:
            newLine = createClassListing(classCode)
            layout.addWidget(newLine)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(500, 400)

        class_code_label = QLabel(text="Class Code")
        class_code_field = QLineEdit()
        class_code_submit = QPushButton("Add Class")

        layout = QGridLayout(self)

        layout.addWidget(class_code_label, 1, 1)
        layout.addWidget(class_code_field, 1, 2)
        layout.addWidget(class_code_submit, 1, 3)
        self.setWindowTitle("TracKourse")
        self.setWindowIcon(QIcon("Trackourse.ico"))

        # button = QPushButton("Ding")
        # self.setCentralWidget(button)
        self.setFixedSize(QSize(400, 300))
        self.setWindowOpacity(0.95)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
