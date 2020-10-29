import sys

from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout


class Food(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Food GUI with CSS')
        self.widgets()

        self.show()

    def widgets(self):
        # Set up layout and add child widgets to the layout
        h_box = QHBoxLayout()
        column1 = QVBoxLayout()
        column2 = QVBoxLayout()
        h_box.addWidget(column1)
        h_box.addWidget(column2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Food()

    sys.exit(app.exec_())
