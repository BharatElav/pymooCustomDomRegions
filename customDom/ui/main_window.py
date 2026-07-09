import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.setWindowTitle("Custom Domination Maker")
        self.resize(781, 385)

        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "moo.png")
        self.setWindowIcon(QIcon(icon_path))

        # Background Configuratiomn
        labelImg = QLabel(self)
        labelImg.setGeometry(0, 0, 781, 385)
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        bg_path = os.path.join(base_dir, "nsga2excalidraw.png")
        pixmap = QPixmap(bg_path)
        
        labelImg.setPixmap(pixmap)
        labelImg.setScaledContents(True)
    
    # Center Window
    def center(self):
        screen = QApplication.primaryScreen().geometry()
        window = self.geometry()
        self.move(
            (screen.width() - window.width()) // 2, 
            (screen.height() - window.height()) // 2
        )



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
