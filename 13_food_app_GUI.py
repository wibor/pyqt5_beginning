import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QTabWidget, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, \
    QPushButton

# Set up style sheet for the entire GUI
style_sheet = """
    QWidget{ background-color: #C92108;}
    QWidget#Tab{ background-color: #FCEBCD; 
    border-radius: 4px}
"""
class Food(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self) -> None:
        self.setMinimumSize(600,700)
        self.setWindowTitle('Food GUI with CSS')
        self.setupTabs()

        self.show()

    def setupTabs(self):
        self.tab_bar = QTabWidget(self)

        self.pizza_tab = QWidget()
        self.pizza_tab.setObjectName("Tab") # for CSS
        self.wings_tab = QWidget()
        self.wings_tab.setObjectName("Tab")

        self.tab_bar.addTab(self.pizza_tab, 'Pizza')
        self.tab_bar.addTab(self.wings_tab, 'Wings')

        # Call methods that contain the widgets for each tab
        self.pizzaTab()
        self.wingsTab()

        # plus side_widget out of tabs
        self.side_widget = QWidget()

        self.side_widget.setObjectName("Tab")
        order_label = QLabel("YOUR ORDER")
        order_label.setObjectName("Header")
        side_v_box = QVBoxLayout()
        side_v_box.addWidget(order_label)
        items_box = QWidget()
        # what inside?
        pizza_label = QLabel("Pizza Type: ")
        toppings_label = QLabel("Topping: ")
        extra_label = QLabel("Extra: ")
        items_box.setObjectName("Side")
        items_grid = QGridLayout()
        items_grid.addWidget(pizza_label, 0, 0, Qt.AlignRight)
        items_grid.addWidget(toppings_label, 1, 0, Qt.AlignRight)
        items_grid.addWidget(extra_label, 2, 0, Qt.AlignRight)
        items_box.setLayout(items_grid)
        side_v_box.addWidget(items_box)
        side_v_box.addStretch()

        self.side_widget.setLayout(side_v_box)

        # Add widgets to main window and set layout
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(self.tab_bar)
        main_h_box.addWidget(self.side_widget)
        self.setLayout(main_h_box)


    def pizzaTab(self):
        tab_pizza_label = QLabel("BUILD YOUR OWN PIZZA")
        tab_pizza_label.setObjectName("Header")
        description_box = QWidget()
        pizza_desc = QLabel()
        pizza_desc.setText("Build a custom pizza for you.")
        pizza_desc.setWordWrap(True)

        h_box = QHBoxLayout()
        h_box.addWidget(pizza_desc)
        description_box.setLayout(h_box)

        add_to_order_button1 = QPushButton("Add To Order")

        page1_v_box = QVBoxLayout()
        page1_v_box.addWidget(tab_pizza_label)
        page1_v_box.addWidget(description_box)
        page1_v_box.addStretch()
        page1_v_box.addWidget(add_to_order_button1,
                              alignment=Qt.AlignRight)

        self.pizza_tab.setLayout(page1_v_box)

    def wingsTab(self):
        tab_pizza_label = QLabel("BUILD YOUR OWN PIZZA")
        tab_pizza_label.setObjectName("Header")
        description_box = QWidget()
        pizza_desc = QLabel()
        pizza_desc.setText("Build a custom pizza for you.")
        pizza_desc.setWordWrap(True)

        h_box = QHBoxLayout()
        h_box.addWidget(pizza_desc)
        description_box.setLayout(h_box)

        add_to_order_button1 = QPushButton("Add To Order")

        page1_v_box = QVBoxLayout()
        page1_v_box.addWidget(tab_pizza_label)
        page1_v_box.addWidget(description_box)
        page1_v_box.addStretch()
        page1_v_box.addWidget(add_to_order_button1,
                              alignment=Qt.AlignRight)

        self.wings_tab.setLayout(page1_v_box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    window = Food()

    sys.exit(app.exec_())
