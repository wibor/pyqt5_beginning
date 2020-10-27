import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QAction, QStatusBar, QToolBar


class PhotoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Gui()

    def Gui(self):
        self.setGeometry(100, 100, 400, 350)
        self.setWindowTitle('Photo Editor')
        self.setCentralWidget(QTextEdit())

        self.createMenu()
        self.createToolBar()
        #self.createDockWidget()

        self.show()

    def createToolBar(self):
        tool_bar = QToolBar("Main Toolbar")
        tool_bar.setIconSize(QSize(16,16))
        self.addToolBar(tool_bar)

        tool_bar.addAction(self.exit_act)

    def createMenu(self):
        # create actions
        self.exit_act = QAction(QIcon('images/exit.png'), 'Exit', self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setStatusTip('Quit program')
        self.exit_act.triggered.connect(self.close)

        menu_bar = self.menuBar()
        # menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(self.exit_act)

        self.setStatusBar(QStatusBar(self))


if __name__ == '__main__':
    app = QApplication([])
    _  = PhotoEditor()
    sys.exit(app.exec_())
