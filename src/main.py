print("branch development")
print("sqlite3")
print("devo")


import gui
import sys
from PyQt6.QtWidgets import QApplication

def main():
    print("Hello sunt sqlite21121232")
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gui.Gui(500,500, "Vocal Home Automation")
    window.build()
    sys.exit(app.exec())