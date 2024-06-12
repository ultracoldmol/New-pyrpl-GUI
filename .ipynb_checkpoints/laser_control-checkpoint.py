import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QMessageBox
from PyQt5.QtCore import QTimer
import pyrpl

class LaserControlApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.rp = pyrpl.Pyrpl(config=None)
        self.lasers = [self.rp.lockbox(i) for i in range(5)]

    def initUI(self):
        self.setWindowTitle('Laser Locking Control')
        self.setGeometry(100, 100, 400, 300)

        # Create central widget and layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        # Create labels and buttons for each laser
        self.laser_status_labels = []
        self.laser_buttons = []

        for i in range(5):
            label = QLabel(f'Laser {i+1} Locking Status: Unknown', self)
            label.setAlignment(Qt.AlignCenter)
            self.laser_status_labels.append(label)
            self.layout.addWidget(label)

            button = QPushButton(f'Check Laser {i+1}', self)
            button.clicked.connect(lambda checked, i=i: self.check_laser_locking(i))
            self.laser_buttons.append(button)
            self.layout.addWidget(button)

        # Set layout to the central widget
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def check_laser_locking(self, laser_index):
        try:
            laser = self.lasers[laser_index]
            if laser.is_locked:
                self.laser_status_labels[laser_index].setText(f'Laser {laser_index+1} Locking Status: Locked')
            else:
                self.laser_status_labels[laser_index].setText(f'Laser {laser_index+1} Locking Status: Not Locked')
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Failed to check laser {laser_index+1} locking status: {str(e)}')

def main():
    app = QApplication(sys.argv)
    ex = LaserControlApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

