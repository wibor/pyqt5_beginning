import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QAction, QStatusBar


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
        menus = {'File':'New Open Save Exit',
                 'Edit':'Undo Redo Cut Copy Paste Find',
                 'Tools':'Font Color Highlight',
                 'Help':'About'}
        shortcuts = 'NOSQZRXCVFBLHA'
        handlers = {
            'Exit': self.close,
        }
        menubar = self.menuBar()
        i=0
        for key,val in menus.items():
            menu = menubar.addMenu(key)
            for v in val.split(' '):
                action = QAction(v, self)
                # eliminated doubles in shortcuts
                action.setShortcut(f'Ctrl+{shortcuts[i]}')
                i+=1 # index for shortcuts
                if handlers.get(v):
                    action.triggered.connect(handlers[v])
                menu.addAction(action)





# run the program
if __name__ == '__main__':
    app = QApplication(sys.argv) # or []
    window = Notepad()
    sys.exit(app.exec_())
