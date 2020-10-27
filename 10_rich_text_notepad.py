import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QTextCursor, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QAction, QStatusBar, QInputDialog, QFontDialog, \
    QMessageBox, QFileDialog, QColorDialog


class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Gui()

    def Gui(self):
        self.setGeometry(100, 100, 350, 400)
        self.setWindowTitle('NOTEPAD 2')
        self.widgets()
        self.notepadMenu()

        self.show()

    def widgets(self):
        self.text_field = QTextEdit()
        self.setCentralWidget(self.text_field)
        self.setStatusBar(QStatusBar())

    def notepadMenu(self):
        # x -> as separator
        menus = {'File':'New x Open Save Exit',
                 'Edit':'Undo Redo Cut Copy Paste x Find',
                 'Tools':'Font Color x Highlight',
                 'Help':'About'}
        shortcuts = 'NOSQZRXCVFBLHA'
        handlers = {
            'New':   self.newFile,
            'Open':  self.openFile,
            'Save':  self.saveFile,
            'Find':  self.findText,
            'Font':  self.selectFont,
            'Color': self.chooseFontColor,
            'Highlight': self.highlightColor,
            'Exit':  self.close,
            'About': self.aboutDialog,
        }
        menubar = self.menuBar()
        i=0
        for key,val in menus.items():
            menu = menubar.addMenu(key)
            for v in val.split(' '):
                if v=='x':
                    menu.addSeparator()
                else:
                    action = QAction(v, self)
                    # eliminated doubles in shortcuts
                    action.setShortcut(f'Ctrl+{shortcuts[i]}')
                    i+=1 # index for shortcuts
                    if handlers.get(v):
                        action.triggered.connect(handlers[v])
                    menu.addAction(action)

    # handlers:
    def saveFile(self):
        # display dialog asking user if they want to save the text in the text edit field to a text file.
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', "","HTML Files (*.html);;Text Files (*.txt)")
        notepad_text = ''
        if file_name.endswith('.txt'):
            notepad_text = self.text_field.toPlainText()
        elif file_name.endswith('.html'):
            notepad_text = self.text_field.toHtml()

        try:
            with open(file_name, 'w') as file:
                file.write(notepad_text)
        except:
            QMessageBox.information(self, "Error", "Unable to save file.", QMessageBox.Ok)

    def openFile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "HTML Files (*.html);;Text Files (*.txt)")
        if file_name:
            with open(file_name, 'r') as file:
                text = file.read()
            self.text_field.setText(text)
        else:
            QMessageBox.information(self, "Error", "Unable to open file.", QMessageBox.Ok)

    def newFile(self):
        self.backup_copy = self.text_field.toPlainText()
        self.text_field.clear()

    def aboutDialog(self):
        QMessageBox.about(self, "About Notepad", "Beginner's Practical Guide to PyQt\n\nProject 5.1 - Notepad GUI")

    def selectFont(self):
        current = self.text_field.currentFont()
        #font, ok = QFontDialog.getFont(QFont("Helvetica", 10), self)
        font, ok = QFontDialog.getFont(current, self) # MacOs - , options=QFontDialog.DontUseNativeDialog
        if ok:
            self.text_field.setCurrentFont(font)

    def chooseFontColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_field.setTextColor(color)

    def highlightColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_field.setTextBackgroundColor(color)

    def findText(self):
        find_text, ok = QInputDialog.getText(self, "Search Text", 'Find:')
        # Check to make sure the text can be modified
        selections = []
        if ok and not self.text_field.isReadOnly():
            self.text_field.moveCursor(QTextCursor.Start)
            color = QColor(Qt.yellow)

            while self.text_field.find(find_text):
                # Use ExtraSelections to mark the text you are searching for as yellow
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(color)
                # Set the cursor of the selection
                selection.cursor = self.text_field.textCursor()
                # Add selection to list
                selections.append(selection)

            # Highlight selections in text edit widget
            for _ in selections:
                self.text_field.setExtraSelections(selections)






# run the program
if __name__ == '__main__':
    app = QApplication(sys.argv) # or []
    window = Notepad()
    sys.exit(app.exec_())
