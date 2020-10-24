import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QCheckBox, QButtonGroup, QVBoxLayout, \
    QPushButton


class Survey(QWidget):
    def __init__(self):
        super().__init__()
        self.Gui()

    def Gui(self):
       self.setGeometry(100, 100, 400, 250)
       self.setWindowTitle('Survey GUI')
       self.surveyWidgets()

       self.show()

    def surveyWidgets(self):
        font = QFont('Arial', 16)
        title = QLabel("Movie score")
        title.setFont(font)
        question = QLabel("How would you rate our service today?")

        # Create horizontal layouts
        title_h_box = QHBoxLayout()
        title_h_box.addStretch()
        title_h_box.addWidget(title)
        title_h_box.addStretch()

        ratings = ["Hate it", "Don't like it", "Like it", "Love it", "Really love it"]
        ratings_h_box = QHBoxLayout()
        ratings_h_box.setSpacing(60) # Set spacing between widgets in horizontal layout
        ratings_h_box.addStretch()
        for r in ratings:
            ratings_h_box.addWidget(QLabel(r, self))
        ratings_h_box.addStretch()

        # checkboxes
        checkbox_h_box = QHBoxLayout()
        checkbox_h_box.setSpacing(60)
        # Create button group to contain checkboxes
        scale_bg = QButtonGroup(self)

        checkbox_h_box.addStretch()
        for i,r in enumerate(ratings):
            item = QCheckBox(str(i+1), self)
            checkbox_h_box.addWidget(item)
            scale_bg.addButton(item)
        checkbox_h_box.addStretch()

        scale_bg.buttonClicked.connect(self.checkboxClicked)

        close_button = QPushButton("Close", self)
        close_button.setFont(font)
        close_button.clicked.connect(self.close)

        # vertical layout
        v_box = QVBoxLayout()
        v_box.addLayout(title_h_box)
        v_box.addWidget(question)
        v_box.addStretch(1)

        v_box.addLayout(ratings_h_box)
        v_box.addLayout(checkbox_h_box)
        v_box.addStretch(2)

        v_box.addWidget(close_button)

        self.setLayout(v_box)

    def checkboxClicked(self, cb):
        self.select = cb.text()
        print(f'Selected {self.select}.')

    def close(self):
        print(f'Finally selected: {self.select}.')
        super().close()


# run the program
if __name__ == '__main__':
    app = QApplication(sys.argv) # or []
    window = Survey()
    sys.exit(app.exec_())
