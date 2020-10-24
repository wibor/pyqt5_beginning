import sys

from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.window()
        self.counter = 0

    def window(self):
        self.setWindowTitle('LogIn')
        self.setGeometry(100, 100, 200, 150)
        self.widgets()
        self.display_button() # call our displayButton function
        self.show()

    def widgets(self):
        name_label = QLabel(self)
        name_label.setText("Name:")
        name_label.move(QPoint(30,30))
        self.name_input = QLineEdit(self)
        self.name_input.setAlignment(Qt.AlignLeft) # The default alignment is AlignLeft
        self.name_input.resize(100, 20)
        self.name_input.move(80, 30)

    def display_button(self):
        button = QPushButton('Push me', self)
        #button.clicked.connect(self.buttonClicked)
        button.clicked.connect(self.buttonClear)
        button.move(80, 70) # arrange button

    def buttonClear(self):
        sender = self.sender()
        if sender.text()=='Push me':
            self.name_input.clear()

    def buttonClicked(self):
        print(f"The button has been clicked {self.counter} times.")
        self.counter +=1

'''
When the clear_button is clicked, it emits a signal that is connected 
to the clearEntries() function. In order to determine where the source 
of a signal is coming from in your applications, you could also 
use the sender() method. Here, the signal is sent from our button 
when it is clicked, and if the text on the sender is 'Clear', 
then the name_entry widget reacts to the signal and clears its current text.
'''

# run the program
if __name__=='__main__':
    app = QApplication(sys.argv) #or []
    window = Login()
    sys.exit(app.exec_())
