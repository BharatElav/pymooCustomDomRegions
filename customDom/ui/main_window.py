import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Global Scope Setup
        self.base_dir = os.path.dirname(os.path.abspath(__file__))

        # Window Setup
        self.configWindow()
        self.centerWindow()

        # Background Configuratiomn
        self.configBg()
    
    # Configure Window
    def configWindow(self):
        self.setWindowTitle("Custom Domination Maker")
        self.resize(1562, 770)

        icon_path = os.path.join(self.base_dir, "moo.png")
        self.setWindowIcon(QIcon(icon_path))

    # Center Window
    def centerWindow(self):
        screen = QApplication.primaryScreen().geometry()
        window = self.geometry()
        self.move(
            (screen.width() - window.width()) // 2, 
            (screen.height() - window.height()) // 2
        )

    # Configure Background Template
    def configBg(self):
        labelImg = QLabel(self)
        labelImg.setGeometry(0, 0, self.width(), self.height())
        
        bg_path = os.path.join(self.base_dir, "nsga2excalidraw.png")
        pixmap = QPixmap(bg_path)
        
        labelImg.setPixmap(pixmap)
        labelImg.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
