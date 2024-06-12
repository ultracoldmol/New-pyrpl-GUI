import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QVBoxLayout, QWidget, 
                             QLabel, QLineEdit, QPushButton, QTabWidget, QTableWidget, 
                             QTableWidgetItem, QHeaderView, QMessageBox)
from PyQt5.QtCore import Qt

class AdvancedApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Advanced PyQt5 GUI')
        self.setGeometry(100, 100, 800, 600)

        # Create menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # Add actions to the menu bar
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Create central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Create tab widget
        self.tabs = QTabWidget()
        self.tabs.addTab(self.createTab1(), "Tab 1")
        self.tabs.addTab(self.createTab2(), "Tab 2")

        # Add tabs to layout
        layout.addWidget(self.tabs)

        # Set the layout to the central widget
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def createTab1(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Add label, text input, and button
        self.label = QLabel('Enter some text:')
        self.text_input = QLineEdit()
        self.button = QPushButton('Show Message')
        self.button.clicked.connect(self.showMessage)

        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)
        tab.setLayout(layout)
        return tab

    def createTab2(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Add table
        self.table = QTableWidget(0, 2)  # 0 rows, 2 columns
        self.table.setHorizontalHeaderLabels(['Name', 'Age'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Add input fields and button to add data to table
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('Name')
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText('Age')
        self.add_button = QPushButton('Add to Table')
        self.add_button.clicked.connect(self.addToTable)

        layout.addWidget(self.table)
        layout.addWidget(self.name_input)
        layout.addWidget(self.age_input)
        layout.addWidget(self.add_button)
        tab.setLayout(layout)
        return tab

    def showMessage(self):
        text = self.text_input.text()
        QMessageBox.information(self, 'Message', f'You entered: {text}')

    def addToTable(self):
        name = self.name_input.text()
        age = self.age_input.text()
        if not name or not age:
            QMessageBox.warning(self, 'Input Error', 'Please enter both name and age.')
            return
        
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(name))
        self.table.setItem(row_position, 1, QTableWidgetItem(age))

        self.name_input.clear()
        self.age_input.clear()

def main():
    app = QApplication(sys.argv)
    ex = AdvancedApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

