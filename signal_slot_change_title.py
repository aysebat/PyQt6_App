
#second basic app for signal and slot
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice
#from PyQt6.QtCore import QSize, Qt #use if you want to size the app
#we are not going to use comment line applications
window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My First App")
        self.button = QPushButton("Press ME!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)


        self.setCentralWidget(self.button)
        #self.setFixedSize(QSize(400,300)) #use if you want to fixed size the app

    def the_button_was_clicked(self):
        print('Clicked!')
        new_window_title = choice(window_titles)
        print(f"Setting title: {new_window_title}")
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print(f"Window title changed: {window_title}")

        if window_title == "Something went wrong":
            self.button.setDisabled(True)










#if you want to use comment line you may use the following: QApplication(sys.argv)
app = QApplication(sys.argv)

#Create the Qt widget, which will be our window
window = MainWindow()
window.show()  #windows are hidden by default

#star the app
app.exec()
