import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QCheckBox, QPushButton, QMessageBox

from Registration import CreateNewUser

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize()

    def initialize(self):
        """
        Initialize the window and display its content
        :return:
        """
        self.setGeometry(100, 100, 400, 230)
        self.setWindowTitle('Login GUI')
        self.loginUserInterface()

        self.show()

    def loginUserInterface(self):
        font = QFont('Arial', 16)
        login = QLabel(self)
        login.setText('LOGIN')
        login.setFont(font)
        login.move(150,10)

        label_login = QLabel(self)
        label_login.setText('username:')
        label_login.setFont(font)
        label_login.move(40,40)

        label_password = QLabel('password:', self)
        label_password.setFont(font)
        label_password.move(40,70)

        self.name_entry = QLineEdit(self)
        self.name_entry.move(150, 40)
        self.name_entry.resize(200, 25)
        self.pass_entry = QLineEdit(self)
        self.pass_entry.move(150, 70)
        self.pass_entry.resize(200, 25)
        self.pass_entry.setEchoMode(QLineEdit.Password)

        # Sign in push button
        sign_in_button = QPushButton('login', self)
        sign_in_button.setFont(font)
        sign_in_button.move(250, 125)
        sign_in_button.resize(100, 70)
        sign_in_button.clicked.connect(self.login_button)

        # Display show password checkbox
        check = QCheckBox('Show password', self)
        check.toggle()
        check.setChecked(False)
        check.move(150, 100)
        check.stateChanged.connect(self.show_password)

        # Display sign up label and push button
        not_a_member = QLabel("not a member?", self)
        not_a_member.move(55, 150)
        sign_up = QPushButton("sign up", self)
        sign_up.move(150, 145)
        sign_up.clicked.connect(self.signup_button)

    def show_password(self, state):
        if state==Qt.Checked:
            self.pass_entry.setEchoMode(QLineEdit.Normal)
        else:
            self.pass_entry.setEchoMode(QLineEdit.Password)

    def login_button(self):
        """  When user clicks sign in button, check if username and password match
        any existing profiles in users.txt. If they exist, display messagebox and
        close program. If they don't, display error messagebox. """
        users ={}
        try:
            with open('files/users.txt', 'r') as f:
                for line in f:
                    field = line.split(' ')
                    username = field[0]
                    password = field[1].strip('\n')
                    users[username] = password
        except FileNotFoundError:
            print("The data_file does not exist. Creating a new file.")
            f = open('files/users.txt', 'w')
            f.close()

        username = self.name_entry.text()
        password = self.pass_entry.text()

        if (username, password) in users.items():
            QMessageBox.information(self, "Login Successful!", "Login Successful!", QMessageBox.Ok, QMessageBox.Ok)
            self.close() # close program or open main window
        else:
            QMessageBox.warning(self, "Error Message", "The username or password is incorrect.", QMessageBox.Close, QMessageBox.Close)

    def signup_button(self):
        """ When the sign up button is clicked,
        open a new window and allow the user to create a new account."""
        self.new_user = CreateNewUser()
        self.new_user.show()

    # add-on: override event in PyQt
    def closeEvent(self, event):
        """
        When a QWidget is closed in PyQt, it generates a QCloseEvent. So we need to change
how the closeEvent() method is handled. To do so we create a new method called closeEvent() that accepts as a parameter an event.
        :param event:
        :return:
        """
        quit_msg = QMessageBox.question(self, "Quit Application?", "Are you sure you want to Quit?", QMessageBox.No | QMessageBox.Yes, QMessageBox.Yes)
        if quit_msg == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


# run the program
if __name__ == '__main__':
    app = QApplication(sys.argv) # or []
    window = Login()
    sys.exit(app.exec_())
