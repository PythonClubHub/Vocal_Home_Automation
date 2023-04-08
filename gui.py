from PyQt6.QtWidgets import QWidget, QPushButton, QLabel

class Gui(QWidget):
    
    def __init__(self, width, height, title):
        super().__init__()

        self.width = width
        self.height = height
        self.title = title

        btn = QPushButton("Button", self)
        btn.setGeometry(100, 100, 150, 80)

        label = QLabel("Text", self)
        label.move(150,50)
        label.setStyleSheet("font-size: 20px")

    def build(self):
        self.resize(self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()


