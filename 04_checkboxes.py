import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QApplication, QPushButton, QMessageBox


class Checkboxes(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.selected = set()

    def initUi(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle('QCheckBox')
        self.display()

        self.show()

    def display(self):
        label = QLabel(self)
        label.setText('Select some checkboxes')
        label.setWordWrap(True)
        label.move(10, 10)
        label.resize(230, 60)

        items = []
        for i in range(3):
            # morning_cb.toggle() # uncomment if you want box to start off checked
            check = QCheckBox(f'Choice Nr.{i}', self)
            check.move(20, 80+i*20)
            check.stateChanged.connect(self.handler)
            # When a checkbox’s state changes, rather than using clicked()
            # like with the QPushButton, we can use stateChanged() to send a signal
            # and then connect to our function
            items.append(check)

        button = QPushButton("Status", self)
        button.move(120,170)
        button.resize(100,40)
        button.clicked.connect(self.button_handler)

    def button_handler(self):
        info = (lambda x: x if len(x) else 'nothing')(self.selected)
        msg = QMessageBox.question(self, "Object Status (some title)",
                f"Selected: {info}\nDo you wish to continue?",
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.No:
            print("Closing application.")
            self.close()
        else:
            pass

    def handler(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            self.selected.add(sender.text())
            print(f'{sender.text()} selected.')
        else:
            try:
                self.selected.remove(sender.text())
            except:
                pass
            print(f'{sender.text()} deselected.')

# run the program
if __name__ == '__main__':
    app = QApplication(sys.argv) # or []
    window = Checkboxes()
    sys.exit(app.exec_())
