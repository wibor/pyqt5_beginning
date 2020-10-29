import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Food(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self) -> None:
        self.setMinimumSize(600,700)
        self.setWindowTitle('Food GUI with CSS')
        self.setupTabs()

        self.show()

    def setupTabs(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Food()

    sys.exit(app.exec_())
