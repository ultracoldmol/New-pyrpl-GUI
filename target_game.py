import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QMessageBox, QDesktopWidget)
from PyQt5.QtCore import QTimer, Qt

class TargetGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.score = 0  # Initialize score before calling initUI
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Click the Target Game')
        self.setGeometry(100, 100, 800, 600)
        self.center()

        # Create central widget and layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        # Create a label to display the score
        self.score_label = QLabel(f'Score: {self.score}', self)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.score_label)

        # Create the target button
        self.target_button = QPushButton('Target', self)
        self.target_button.setStyleSheet("background-color: red; font-size: 20px;")
        self.target_button.setFixedSize(100, 100)
        self.target_button.clicked.connect(self.hit_target)
        self.layout.addWidget(self.target_button)

        # Set layout to the central widget
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Timer to move the target
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_target)
        self.timer.start(1000)  # Move the target every second

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def hit_target(self):
        self.score += 1
        self.score_label.setText(f'Score: {self.score}')

    def move_target(self):
        max_x = self.width() - self.target_button.width()
        max_y = self.height() - self.target_button.height()

        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)

        self.target_button.move(new_x, new_y)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    ex = TargetGame()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

