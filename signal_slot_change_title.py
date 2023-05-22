
#second basic app for signal and slot
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#from PyQt6.QtCore import QSize, Qt #use if you want to size the app
#we are not going to use comment line applications



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My First App")
        self.button = QPushButton("Press ME!")
        self.button.clicked.connect(self.the_button_was_clicked)


        self.setCentralWidget(self.button)
        #self.setFixedSize(QSize(400,300)) #use if you want to fixed size the app

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

        self.setWindowTitle("My oneshot App")








#if you want to use comment line you may use the following: QApplication(sys.argv)
app = QApplication([])

#Create the Qt widget, which will be our window
window = MainWindow()
window.show()  #windows are hidden by default

#star the app
app.exec()
