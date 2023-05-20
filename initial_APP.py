import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
#from PyQt6.QtCore import QSize, Qt #use if you want to size the app
#we are not going to use comment line applications



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First App")
        #self.setFixedSize(QSize(400,300)) #use if you want to fixed size the app


#if you want to use comment line you may use the following: QApplication(sys.argv)
app = QApplication([])

#Create the Qt widget, which will be our window
window = MainWindow()
window.show()  #windows are hidden by default

#star the app
app.exec()
