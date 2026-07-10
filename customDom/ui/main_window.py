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
        self.configBg()

        # Layout Configuration
        self.configMainLayout()
    
    # Configure Window
    def configWindow(self):
        # Set Window Title
        self.setWindowTitle("Custom Domination Maker")
        self.resize(1588, 783)

        # Set Window Icon
        icon_path = os.path.join(self.base_dir, "moo.png")
        self.setWindowIcon(QIcon(icon_path))

        # Block Resizing
        self.setFixedSize(self.width(), self.height())  # no resizing at all

    # Center Window
    def centerWindow(self):
        # Grab User's Screen Dimensions and Center the Window
        screen = QApplication.primaryScreen().geometry()
        self.move(
            (screen.width() - self.width()) // 2, 
            (screen.height() - self.height()) // 2
        )

    # Configure Background Template
    def configBg(self):
        # Create Label
        labelImg = QLabel(self)
        labelImg.setGeometry(13, 13, self.width() - 26, self.height() - 26) # Adjusting for default margins
        
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
        mainLayout.addWidget(self.canvas, stretch=43) 
        mainLayout.addWidget(self.toolPanel, stretch=50)

        # Configure Background Colors 
        self.toolPanel.setStyleSheet("background-color: rgba(43, 43, 43, 180);")

# Create the App and Window, Show the Window and Start the App
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# Only Execute this File if its Run Directly
if __name__ == "__main__":
    main()
