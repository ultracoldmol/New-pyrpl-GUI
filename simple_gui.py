import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit

class SimpleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple PyQt5 GUI')

        # Create a central widget and a layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Add a label
        self.label = QLabel('Enter your name:', self)
        layout.addWidget(self.label)

        # Add a text input field
        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        # Add a button
        self.button = QPushButton('Greet', self)
        self.button.clicked.connect(self.greet)
        layout.addWidget(self.button)

        # Set the layout to the central widget
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def greet(self):
        name = self.text_input.text()
        self.label.setText(f'Hello, {name}!')

def main():
    app = QApplication(sys.argv)
    ex = SimpleApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

