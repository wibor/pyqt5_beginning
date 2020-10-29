import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QSpinBox, QComboBox, QTextEdit, QPushButton, \
    QHBoxLayout, QFormLayout


class AppForm(QWidget):
    def __init__(self):
        super().__init__()
        self.Gui()

    def Gui(self):
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('App Form GUI')
        self.formWidgets()

        self.show()

    def formWidgets(self):
        # Create every single widget
        title = QLabel("Appointment Submission Form")
        title.setFont(QFont('Arial', 18))
        title.setAlignment(Qt.AlignCenter)

        name = QLineEdit()
        address = QLineEdit()
        phone = QLineEdit()
        age_label = QLabel("Age")
        age = QSpinBox()
        height_label = QLabel("Height")
        height = QLineEdit()
        weight_label = QLabel("Weight")
        weight = QLineEdit()
        gender = QComboBox()
        surgery = QTextEdit()
        blood_type = QComboBox()
        hours = QSpinBox()
        minutes = QComboBox()

        #name.resize(10, 100)
        phone.setInputMask("000-000-0000;")
        age.setRange(1, 110)
        height.setPlaceholderText("cm")
        weight.setPlaceholderText("kg")
        gender.addItems(['Male', 'Female'])
        blood_type.addItems(["A", "B", "AB", "O"])
        hours.setRange(0, 23)
        minutes.addItems([":00", ":15", ":30", ":45"])

        submit = QPushButton('Submit Appointment')
        # CSS
        submit.setStyleSheet("""
            background-color: skyblue;
            color: white;
            border-style: outset;
            border-width: 3px;
            border-radius: 5px;
            border-color: black;
            font: bold 16px 'Times New Roman';
            qproperty-alignment: AlignCenter
        """)
        submit.setToolTip("Click this to close app");
        submit.clicked.connect(self.close)

        # Create horizontal layout and add age, height, and weight to h_box
        horizont1 = QHBoxLayout()
        horizont1.addSpacing(10)
        horizont1.addWidget(age_label)
        horizont1.addWidget(age)
        horizont1.addWidget(height_label)
        horizont1.addWidget(height)
        horizont1.addWidget(weight_label)
        horizont1.addWidget(weight)
        # Create horizontal layout and add time information
        horizont2 = QHBoxLayout()
        horizont2.addSpacing(10)
        horizont2.addWidget(hours)
        horizont2.addWidget(minutes)

        # Create form layout
        app_form_layout = QFormLayout()

        # Add all widgets to form layout
        app_form_layout.addRow(title)
        app_form_layout.addRow('Full Name', name)
        app_form_layout.addRow('Address', address)
        app_form_layout.addRow('Mobile Number', phone)
        app_form_layout.addRow(horizont1)
        app_form_layout.addRow('Gender', gender)
        app_form_layout.addRow('Surgery', surgery)
        app_form_layout.addRow('Blood Type', blood_type)
        app_form_layout.addRow('Desired Time', horizont2)
        app_form_layout.addRow(submit)

        self.setLayout(app_form_layout)

# run the program
if __name__ == '__main__':
    app = QApplication(sys.argv) # or []
    window = AppForm()
    sys.exit(app.exec_())
