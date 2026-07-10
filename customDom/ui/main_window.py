import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QPixmap
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Global Scope Setup
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.canvas = pg.PlotWidget()
        self.toolPanel = QWidget()

        # Window Setup
        self.configWindow()
        self.centerWindow()

        # Background Configuratiomn
        # self.configBg()

        # Layout Configuration
        self.configMainLayout()
        self.testLayout()
    
    # Configure Window
    def configWindow(self):
        # Set Window Title
        self.setWindowTitle("Custom Domination Maker")
        self.resize(1562, 770)

        # Set Window Icon
        icon_path = os.path.join(self.base_dir, "moo.png")
        self.setWindowIcon(QIcon(icon_path))

    # Center Window
    def centerWindow(self):
        # Grab User's Screen Dimensions and Center the Window
        screen = QApplication.primaryScreen().geometry()
        self.move(
            (screen.width() - window.width()) // 2, 
            (screen.height() - window.height()) // 2
        )

    # Configure Background Template
    def configBg(self):
        # Create Label
        labelImg = QLabel(self)
        labelImg.setGeometry(0, 0, self.width(), self.height())
        
        # Find the Image
        bg_path = os.path.join(self.base_dir, "nsga2excalidraw.png")
        pixmap = QPixmap(bg_path)
        
        # Make the Label Display the Image
        labelImg.setPixmap(pixmap)
        labelImg.setScaledContents(True)

    # Configure Main Layout
    def configMainLayout(self):
        # Create Central Widget
        central = QWidget()
        self.setCentralWidget(central)

        # Create Layout
        mainLayout = QHBoxLayout(central)
        mainLayout.addWidget(self.canvas, stretch=3) 
        mainLayout.addWidget(self.toolPanel, stretch=1)

    # Layout Color Testing
    def testLayout(self):
        self.canvas.setStyleSheet("background-color: #1e1e1e;")
        self.toolPanel.setStyleSheet("background-color: #2b2b2b;")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
