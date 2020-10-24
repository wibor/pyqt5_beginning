import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class UserProfile(QWidget):
    def __init__(self):
        super().__init__()
        self.user_profile()

    def user_profile(self):
        self.setGeometry(20,40,250, 400)
        self.setWindowTitle('User Profile GUI')
        self.display_image()
        self.display_user_info()

        self.show()

    def display_image(self):
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGreen)
        self.setPalette(p)
        
        image_path = "images/world.png"
        try:
            with open(image_path):
                image = QLabel(self)
                pixmap = QPixmap(image_path)
                image.setPixmap(pixmap)
                image.move(80, 15)
                image.resize(100,100)

        except FileNotFoundError:
            print('Image not found.')

    def display_user_info(self):
        label = QLabel(self)
        label.setText('John Doe')
        label.move(70, 120)
        label.setFont(QFont('Arial', 20))

        bio = QLabel(self)
        bio.setText('Biography')
        bio.move(15, 160)
        bio.setFont(QFont('Arial', 16))

        about = QLabel(self)
        about.setText("I'm a Software Engineer with 8 years experience creating awesome code.")
        about.setWordWrap(True)
        about.move(15, 190)

        skills_title = QLabel(self)
        skills_title.setText("Skills")
        skills_title.move(15, 230)
        skills_title.setFont(QFont('Arial', 16))

        skills = QLabel(self)
        skills.setText("Python | C# | SQL | JavaScript")
        skills.move(15, 260)


# run the program
if __name__=='__main__':
    app = QApplication(sys.argv) #or []
    #window = EmptyWindow()
    window = UserProfile()
    sys.exit(app.exec_())
