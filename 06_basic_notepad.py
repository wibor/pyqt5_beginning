import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QFileDialog


class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.Gui()

    def Gui(self):
       self.setGeometry(100, 100, 300, 400)
       self.setWindowTitle('Notepad GUI')
       self.notepadWidgets()

       self.show()

    def notepadWidgets(self):
        button_new = QPushButton('New', self)
        button_save = QPushButton('Save', self)
        button_new.move(20,20)
        button_save.move(205,20)
        button_new.clicked.connect(self.new) #clearText
        button_save.clicked.connect(self.save) #saveText

        # Create text edit field
        self.text_field = QTextEdit(self)
        self.text_field.resize(280, 330)
        self.text_field.move(10, 60)

    def new(self):
        self.text_field.clear()

    def save(self):
        options = QFileDialog.Options()
        text = self.text_field.toPlainText()
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', "","All Files (*);;Text Files (*.txt)", options=options)

        if file_name:
            with open(file_name, 'w') as f:
                f.write(text)


# run the program
if __name__ == '__main__':
    app = QApplication(sys.argv) # or []
    window = Notepad()
    sys.exit(app.exec_())
