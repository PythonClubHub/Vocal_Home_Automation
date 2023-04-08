print("branch development")
print("test")

import gui
import sys
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = gui.Gui(500,500, "Vocal Home Automation")
    window.build()
    app.exec()
    print("Hello")


if __name__ == "__main__":
    main()