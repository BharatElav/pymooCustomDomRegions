import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Global Scope Setup
        # Layout Setups
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.canvas = pg.PlotWidget()
        self.mainPanel = QWidget()
        self.panel1 = QWidget()
        self.panel2 = QWidget()
        self.panel3 = QWidget()

        # Panel 1 Widgets
        self.toolOptions = QWidget()
        self.plotButton = QPushButton("Plot")

        # Window Setup
        self.configWindow()
        self.centerWindow()

        # Background Configuratiomn
        self.configBg()

        # Layout Configuration
        self.configMainLayout()
        self.configMainPanel()
        self.configPanel1()
    
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
        mainLayout.addWidget(self.mainPanel, stretch=50)

        # Configure Background Colors 
        self.mainPanel.setStyleSheet("background-color: rgba(43, 43, 43, 180);")

    # Confiure Main Panel
    def configMainPanel(self):
        # Create Layout
        mainPanelLayout = QHBoxLayout(self.mainPanel)
        mainPanelLayout.addWidget(self.panel1, stretch=4)
        mainPanelLayout.addWidget(self.panel2, stretch=3)
        mainPanelLayout.addWidget(self.panel3, stretch=3)

        # Configure Background Colors
        self.panel1.setStyleSheet("background-color: rgba(255, 0, 0, 180);")
        self.panel2.setStyleSheet("background-color: rgba(0, 255, 0, 180);")
        self.panel3.setStyleSheet("background-color: rgba(0, 0, 255, 180);")

    # Configure Panel 1 (Tools, Shade Options, Plot Button)
    def configPanel1(self):
        # Create Layout
        panel1Layout = QVBoxLayout(self.panel1)

        # Create Local Widgets
        toolOptionsLabel = QLabel("Tool Options")   

        # Configure Plot Button Widget to be able to be Stretched
        self.plotButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Add Widgets to Panel
        panel1Layout.addWidget(toolOptionsLabel, stretch=1)
        panel1Layout.addWidget(self.toolOptions, stretch=20)
        panel1Layout.addWidget(self.plotButton, stretch=2)

        # Configure Background Colors
        toolOptionsLabel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.toolOptions.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.plotButton.setStyleSheet("background-color: rgba(255, 255, 255, 180);")

# Create the App and Window, Show the Window and Start the App
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# Only Execute this File if its Run Directly
if __name__ == "__main__":
    main()
