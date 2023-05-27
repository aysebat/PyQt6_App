import sys
import os

from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

basedir = os.path.dirname(__file__)
print(f"Current working folder: {os.getcwd()}")
print(f"Paths are relative to : {basedir}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Label Example App")

        widget = QLabel("Hello World")
        widget.setPixmap(QPixmap(os.path.join(basedir, "data/download.jpeg")))
        widget.setScaledContents(True)

        widget.setAlignment(
            Qt.AlignmentFlag.AlignHCenter
            | Qt.AlignmentFlag.AlignVCenter
        )

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
