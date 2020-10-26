import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFormLayout, QPushButton, QGridLayout, QVBoxLayout, \
    QCheckBox, QLineEdit, QTextEdit


class ToDo(QWidget):
    def __init__(self):
        super().__init__()
        self.Gui()

    def Gui(self):
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('TODO List')
        self.widgets()

        self.show()

    def widgets(self):
        main_grid = QGridLayout()

        title = QLabel("TODO List")
        title.setFont(QFont('Arial', 18, weight=75)) #bold as int75
        title.setAlignment(Qt.AlignCenter)

        mustdo_label = QLabel("Must Dos")
        mustdo_label.setFont(QFont('Arial', 12))
        appts_label = QLabel("Appointments")
        appts_label.setFont(QFont('Arial', 12))

        # Create must-do section
        mustdo_grid = QGridLayout()
        mustdo_grid.setContentsMargins(5, 5, 5, 5)
        mustdo_grid.addWidget(mustdo_label, 0, 0, 1, 2)

        for position in range(1, 15):
            checkbox = QCheckBox()
            checkbox.setChecked(False)
            linedit = QLineEdit()
            linedit.setMinimumWidth(100)
            mustdo_grid.addWidget(checkbox, position, 0)
            mustdo_grid.addWidget(linedit, position, 1)

        appt_v_box = QVBoxLayout()
        appt_v_box.setContentsMargins(5, 5, 5, 5)
        appt_v_box.addWidget(appts_label)
        appt_v_box.addWidget(appts_label)

        times = ["Morning", 'Noon', 'Evening']
        for time in times:
            label = QLabel(time)
            label.setFont(QFont('Arial', 10, italic=True))
            appt_v_box.addWidget(label)
            appt_v_box.addWidget(QTextEdit())

        submit = QPushButton('Close App')
        submit.clicked.connect(self.close)

        main_grid.addWidget(title, 0, 0, 1, 2)
        # The extra two parameters at the end, 1 and 2, tell the layout manager that we want to
        # span one row and three columns. This causes the widget to stretch horizontally.
        main_grid.addLayout(mustdo_grid, 1, 0)
        main_grid.addLayout(appt_v_box, 1, 1)
        main_grid.addWidget(submit, 2, 0, 1, 2)
        # The title QLabel widget is added to the main_grid layout at the position
        # where the row equals 0 and column equals 0, which is also the top-left corner.
        # Then, the mustdo_grid is added directly below it by increasing the row value to 1
        # and leaving the column value equal to 0.
        # Finally, we move over one column for the appt_v_box layout by setting
        # the column value to 1.

        self.setLayout(main_grid)

# run the program
if __name__ == '__main__':
    app = QApplication(sys.argv) # or []
    window = ToDo()
    sys.exit(app.exec_())
