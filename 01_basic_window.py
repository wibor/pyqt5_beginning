# basic window
# pipenv install pyqt5
import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__() #QWidget constructor
        self.initialize()

    def initialize(self):
        # initialize and show window
        self.setGeometry(100,600,400,300) #position and size
        self.setWindowTitle('Empty PyQt window')
        self.show()

class HelloWorldWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle('QLabel Ex.')
        self.displayLabel()
        self.show()

    def displayLabel(self):
        label = QLabel(self)
        label.setText('Hello')
        label.move(105, 15)

        image = "images/world.png"
        try:
            with open(image):
                world_image = QLabel(self)
                pixmap = QPixmap(image)
                world_image.setPixmap(pixmap)
                world_image.move(25, 40)
        except FileNotFoundError:
            print('Image not found.')

# run the program
if __name__=='__main__':
    app = QApplication(sys.argv) #or []
    #window = EmptyWindow()
    window = HelloWorldWindow()
    sys.exit(app.exec_())
