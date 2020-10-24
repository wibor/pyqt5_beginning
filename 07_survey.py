import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication


class Survey(QWidget):
    def __init__(self):
        super().__init__()
        self.Gui()

    def Gui(self):
       self.setGeometry(100, 100, 300, 400)
       self.setWindowTitle('Survey GUI')
       self.surveyWidgets()

       self.show()
        
    def surveyWidget(self):
        font = QFont('Arial', 16)


# run the program
if __name__ == '__main__':
    app = QApplication(sys.argv) # or []
    window = Survey()
    sys.exit(app.exec_())
