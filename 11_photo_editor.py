import sys

from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QTransform
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QAction, QStatusBar, QToolBar, QDockWidget, \
    QDesktopWidget, QWidget, QPushButton, QVBoxLayout, QLabel, QSizePolicy, QFileDialog, QMessageBox


class PhotoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Gui()

    def Gui(self):
        #self.setGeometry(100, 100, 650, 650)
        self.setFixedSize(650, 650)
        self.setWindowTitle('Photo Editor')
        #self.setCentralWidget(QTextEdit())
        self.centerMainWindow()
        self.dock = QDockWidget()
        self.toggle_dock_tools_act = None
        self.createMenu()
        self.createToolBar()
        self.createToolsDockWidget()
        self.photoEditorWidgets()

        self.show()

    def centerMainWindow(self):
        desktop = QDesktopWidget().screenGeometry()
        screen_width = desktop.width()
        screen_height = desktop.height()
        self.move(int((screen_width - self.width()) / 2), int((screen_height - self. height()) / 2))

    def createToolBar(self):
        tool_bar = QToolBar("Toolbar")
        # You should set the size of the icons in the toolbar using the setIconSize() method
        # with QSize() to avoid extra padding
        # when PyQt tries to figure out the arrangement by itself.
        tool_bar.setIconSize(QSize(24,24))
        self.addToolBar(tool_bar)

        tool_bar.addAction(self.open_act)
        tool_bar.addAction(self.save_act)
        tool_bar.addAction(self.print_act)
        tool_bar.addSeparator()
        tool_bar.addAction(self.exit_act)

    def createMenu(self):
        # create actions
        self.exit_act = QAction(QIcon('images/exit.png'), 'Exit', self)
        self.open_act = QAction(QIcon('images/open_file.png'), 'Open', self)
        self.save_act = QAction(QIcon('images/save_file.png'), 'Save', self)
        self.print_act = QAction(QIcon('images/print.png'), 'Print', self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.open_act.setShortcut('Ctrl+O')
        self.save_act.setShortcut('Ctrl+S')
        self.print_act.setShortcut('Ctrl+P')
        # In order to display a message in the status bar when the mouse hovers over an icon,
        self.exit_act.setStatusTip('Quit program')
        self.exit_act.triggered.connect(self.close)
        self.open_act.triggered.connect(self.openImage)
        self.save_act.triggered.connect(self.saveImage)
        self.print_act.triggered.connect(self.printImage)
        self.print_act.setEnabled(False)

        menu_bar = self.menuBar()
        # menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')

        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addSeparator()
        file_menu.addAction(self.print_act)
        file_menu.addSeparator()
        file_menu.addAction(self.exit_act)

        # Create actions for edit menu
        self.rotate90_act = QAction("Rotate 90°", self)
        self.flip_hor_act = QAction("Flip Horizonal°", self)
        self.flip_ver_act = QAction("Flip Vertical°", self)
        self.resize_act = QAction("Resize Image°", self)
        self.rotate90_act.setShortcut("Ctrl+R")
        self.flip_hor_act.setShortcut("Ctrl+H")
        self.flip_ver_act.setShortcut("Ctrl+V")
        self.rotate90_act.triggered.connect(self.rotateImage)
        self.flip_hor_act.triggered.connect(self.flipHorImage)
        self.flip_ver_act.triggered.connect(self.flipVerImage)
        self.resize_act.triggered.connect(self.resizeImage)

        # Create edit menu and add actions
        edit_menu = menu_bar.addMenu('Edit')

        edit_menu.addAction(self.rotate90_act)
        edit_menu.addAction(self.flip_hor_act)
        edit_menu.addAction(self.flip_ver_act)
        edit_menu.addSeparator()
        edit_menu.addAction(self.resize_act)

        # Create view menu and add actions
        view_menu = menu_bar.addMenu('View')
        self.toggle_dock_tools_act = QAction('Toggle View', self)
        self.toggle_dock_tools_act = self.dock.toggleViewAction()
        view_menu.addAction(self.toggle_dock_tools_act)

        self.setStatusBar(QStatusBar(self))


    def createToolsDockWidget(self):
        # Use View -> Edit Image Tools menu and click the dock widget on or off.

        self.dock.setWindowTitle('Dock')
        #dock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dock.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)

        #dock.setWidget(QTextEdit())
        # Create container QWidget to hold all widgets inside dock widget
        self.toolsDock = QWidget()
        # Set initial location of dock widget in main window (Left area)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock)
        # In order to place multiple widgets inside the dock,
        # you could use a single QWidget as the parent for multiple child widgets
        # and arrange them using one of the layout managers
        # Create tool push buttons:
        self.rotate90 = QPushButton("Rotate 90°")
        self.rotate90.setMinimumSize(QSize(130, 40))
        self.rotate90.clicked.connect(self.rotateImage)
        self.flip_horizontal = QPushButton("Flip Horizontal")
        self.flip_horizontal.setMinimumSize(QSize(130, 40))
        self.flip_horizontal.clicked.connect(self.flipHorImage)
        self.flip_vertical = QPushButton("Flip Vertical")
        self.flip_vertical.setMinimumSize(QSize(130, 40))
        self.flip_vertical.clicked.connect(self.flipVerImage)
        self.resize_half = QPushButton("Resize Half")
        self.resize_half.setMinimumSize(QSize(130, 40))
        self.resize_half.clicked.connect(self.resizeImage)

        # Set up vertical layout to contain all the push buttons
        dock_vert_box = QVBoxLayout()
        dock_vert_box.addWidget(self.rotate90)
        dock_vert_box.addStretch(1)
        dock_vert_box.addWidget(self.flip_horizontal)
        dock_vert_box.addWidget(self.flip_vertical)
        dock_vert_box.addStretch(1)
        dock_vert_box.addWidget(self.resize_half)
        dock_vert_box.addStretch(6)
        # Set the main layout for the QWidget, tools_contents,
        # then set the main widget of the dock widget
        self.toolsDock.setLayout(dock_vert_box)
        self.dock.setWidget(self.toolsDock)

        # Handles the visibility of the dock widget
        self.toggle_dock_tools_act = self.dock.toggleViewAction()

    def photoEditorWidgets(self):
        # Set up instances of widgets for photo editor GUI
        self.image = QPixmap()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        # Use setSizePolicy to specify how the widget can be resized,
        # horizontally and vertically. Here, the image will stretch
        # horizontally, but not vertically.
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)

        self.setCentralWidget(self.image_label)

    def openImage(self):
        image_file, _ = QFileDialog.getOpenFileName(self,
                                                    caption="Open File",
                                                    directory='',
        filter="JPG Files (*.jpeg *.jpg );;PNG Files (*.png);;Bitmap Files (*.bmp);;GIF Files (*.gif)")
        if image_file:
            self.image = QPixmap(image_file)
            self.image_label.setPixmap(self.image.scaled(self.image_label. size(),Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.print_act.setEnabled(True)
        else:
            QMessageBox.information(self, "Error", "Unable to open image.", QMessageBox.Ok)

    def saveImage(self):
        image_file, _ = QFileDialog.getOpenFileName(self,
                                                    caption="Save Image File",
                                                    directory='',
        filter="PNG Files (*.png);;JPG Files (*.jpeg *.jpg );;Bitmap Files (*.bmp);;GIF Files (*.gif)")
        if image_file and self.image.isNull()==False:
            self.image.save(image_file)
        else:
            QMessageBox.information(self, "Error", "Unable to save image.", QMessageBox.Ok)

    def printImage(self):
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.NativeFormat) # QPrinter.NativeFormat is the default

        print_dialog = QPrintDialog(printer)
        # If the dialog is accepted by the user, begin printing
        if print_dialog.exec_() == QPrintDialog.Accepted:
            # Use QPainter to output a PDF file
            painter = QPainter()
            painter.begin(printer)
            rect = QRect(painter.viewport())
            size = QSize(self.image_label.pixmap().size())
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size. height())
            painter.setWindow(self.image_label.pixmap().rect())
            # Scale the image_label to fit the rect source (0, 0)
            painter.drawPixmap(0, 0, self.image_label.pixmap())
            painter.end()

    def rotateImage(self):
        if self.image.isNull() == False:
            transform = QTransform().rotate(90)
            rotated = self.image.transformed(transform,
                                             mode=Qt.SmoothTransformation)
            self.image = rotated
            self.image_label.setPixmap(self.image.scaled(self.image_label.size(),
                                                         Qt.KeepAspectRatio,
                                                         Qt.SmoothTransformation))
            self.image_label.repaint()
        else:
            pass

    def flipHorImage(self):
        pass
    def flipVerImage(self):
        pass
    def resizeImage(self):
        pass



if __name__ == '__main__':
    app = QApplication([])
    _  = PhotoEditor()
    sys.exit(app.exec_())
