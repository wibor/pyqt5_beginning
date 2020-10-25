import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFormLayout, QPushButton


class ToDo(QWidget):
    def __init__(self):
        super().__init__()
        self.Gui()

    def Gui(self):
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('TODO List')
        self.widgets()

        self.show()

    def widgets(self):
        title = QLabel("TODO List")
        title.setFont(QFont('Arial', 18))
        title.setAlignment(Qt.AlignCenter)

        submit = QPushButton('Close App')
        submit.clicked.connect(self.close)

        app_layout = QFormLayout()
        app_layout.addRow(title)
        #...
        app_layout.addRow(submit)

        self.setLayout(app_layout)

# run the program
if __name__ == '__main__':
    app = QApplication(sys.argv) # or []
    window = ToDo()
    sys.exit(app.exec_())
