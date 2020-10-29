import sys

from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QTabWidget, \
    QLabel, QLineEdit


class Food(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle('Food GUI with CSS')
        #self.widgets()
        self.setupTabs()

        self.show()

    def setupTabs(self):
        self.tab_bar = QTabWidget()
        self.upper_tab = QWidget()
        self.down_tab = QWidget()

        self.tab_bar.addTab(self.upper_tab, 'Default')
        self.tab_bar.addTab(self.down_tab, 'Background')
        # Call methods that contain the widgets for each tab
        self.upperTab()
        self.downTab()

        # Create layout for main window
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.tab_bar)
        self.setLayout(main_h_box)

    def upperTab(self):
        name_label = QLabel("Name")
        name_entry = QLineEdit()

        sex_group = QGroupBox("Sex")
        male_rb = QRadioButton("Male")
        female_rb = QRadioButton("FeMale")
        sex_box = QHBoxLayout()
        sex_box.addWidget(male_rb)
        sex_box.addWidget(female_rb)
        sex_group.setLayout(sex_box)

        tab_v_box = QVBoxLayout()
        # Add all widgets to the default page layout
        tab_v_box.addWidget(name_label)
        tab_v_box.addWidget(name_entry)
        tab_v_box.addStretch()
        tab_v_box.addWidget(sex_group)
        tab_v_box.addStretch()

        # Set layout for the tab
        self.upper_tab.setLayout(tab_v_box)

    def downTab(self):
        name_label = QLabel("Select One")
        # 1 create grup
        select_group = QGroupBox()
        # 2 create layout
        radio_box = QVBoxLayout()
        tab_v_box = QVBoxLayout()
        choice1 = QRadioButton('one')
        choice2 = QRadioButton('two')
        choice3 = QRadioButton('five')
        tab_v_box.addWidget(name_label)
        tab_v_box.addStretch()
        # 3 add buttons to layout
        radio_box.addWidget(choice1)
        radio_box.addWidget(choice2)
        radio_box.addWidget(choice3)
        # 4 SET layout for group
        select_group.setLayout(radio_box)
        # 5 add group to main layout
        tab_v_box.addWidget(select_group)
        tab_v_box.addStretch()

        # 6 SET layout for self.property
        self.down_tab.setLayout(tab_v_box)


    def widgets(self):
        # Set up layout and add child widgets to the layout
        h_box = QHBoxLayout()

        effects_gb = QGroupBox("RadioButton Group")
        effect1_rb = QRadioButton("through")
        effect2_rb = QRadioButton("into")
        h_box.addWidget(effect1_rb)
        h_box.addWidget(effect2_rb)

        effects_gb.setLayout(h_box)

        column1 = QVBoxLayout()
        column2 = QVBoxLayout()
        #h_box.addWidget(column1)
        #h_box.addWidget(column2)

        self.setLayout(h_box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Food()

    sys.exit(app.exec_())
