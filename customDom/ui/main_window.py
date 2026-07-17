import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QSizePolicy, QComboBox, QStackedWidget, QLineEdit
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
        self.toolSelectorPanel = QWidget()
        self.toolOptionsPanel = QStackedWidget()
        self.shadePanel = QStackedWidget()
        self.plotButton = QPushButton("Plot")

        # Tool Selector Panel
        self.toolSelectorBox = QComboBox()

        # Tool Options Panel
        self.lineOptionsPanel = QWidget()
        self.circleOptionsPanel= QWidget()

        # Line Options Panel
        self.infiniteToggle = QPushButton("Infinite")
        self.infiniteToggle.setCheckable(True)
        self.p1Panel = QWidget()
        self.p2Panel = QWidget()

        # Point 1 Panel
        self.p1f1Value = QLineEdit()
        self.p1f2Value = QLineEdit()

        # Point 2 Panel
        self.p2f1Value = QLineEdit()
        self.p2f2Value = QLineEdit()

        # Circle Options Panel
        self.centerPointPanel = QWidget()
        self.radiusPanel = QWidget()
        self.circleAnglePanel = QWidget()

        # Center Panel
        self.cf1Value = QLineEdit()
        self.cf2Value = QLineEdit()

        # Radius Panel
        self.rValue = QLineEdit()

        # Circle Angle Panel
        self.cat1Value = QLineEdit()
        self.cat2Value = QLineEdit()

        # Shade Panel
        self.shadeLinePanel = QWidget()
        self.shadeCirclePanel = QWidget()

        # Shade Line Panel
        self.shadeDirectionBox = QComboBox()

        # Shade Circle Panel
        self.shadeRegionBox = QComboBox()

        # Window Setup
        self.configWindow()
        self.centerWindow()

        # Background Configuratiomn
        self.configBg()

        # Layout Configuration
        self.configMainLayout()
        self.configMainPanel()
        self.configPanel1()
        self.configToolSelectorPanel()
        self.configToolOptionsPanel()
        self.configLineOptionsPanel()
        self.configCircleOptionsPanel()
        self.configP1Panel()
        self.configP2Panel()
        self.configcenterPointPanel()
        self.configRadiusPanel()
        self.configCircleAnglePanel()
        self.configShadePanel()
        self.configShadeLinePanel()
        self.configShadeCirclePanel()
    
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
        self.panel1.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.panel2.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.panel3.setStyleSheet("background-color: rgba(255, 255, 255, 180);")

    # Configure Panel 1 (Tools, Shade Options, Plot Button)
    def configPanel1(self):
        # Create Layout
        panel1Layout = QVBoxLayout(self.panel1)

        # Configure Plot Button Widget to be able to be Stretched
        self.plotButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Add Widgets to Panel
        panel1Layout.addWidget(self.toolSelectorPanel, stretch=3)
        panel1Layout.addWidget(self.toolOptionsPanel, stretch=16)
        panel1Layout.addWidget(self.shadePanel, stretch=3)
        panel1Layout.addWidget(self.plotButton, stretch=3)

        # Configure Background Colors
        self.toolSelectorPanel.setStyleSheet("background-color: rgba(0, 0, 0, 180);")
        self.toolOptionsPanel.setStyleSheet("background-color: rgba(0, 0, 0, 180);")
        self.shadePanel.setStyleSheet("background-color: rgba(0, 0, 0, 180);")
        self.plotButton.setStyleSheet("background-color: rgba(255, 255, 255, 180);")

    # Configure Tool Selector Panel
    def configToolSelectorPanel(self):
        # Create Layout
        toolSelectorPanelLayout = QVBoxLayout(self.toolSelectorPanel)

        # Create Local Widgets
        toolSelectorLabel = QLabel("Tool Selector") 

        # Configure Tool Selector Options
        self.toolSelectorBox.addItems(["Line Tool", "Circle Tool"])

        # Add Widgets to Panel
        toolSelectorPanelLayout.addWidget(toolSelectorLabel)
        toolSelectorPanelLayout.addWidget(self.toolSelectorBox)

        # Configure Background Colors
        toolSelectorLabel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.toolSelectorBox.setStyleSheet("background-color: rgba(255, 255, 255, 180);" \
        "selection-background-color: transparent;" \
        "selection-color: black;")

    # Configure the ComboBox
    def onToolChanged(self, index):
        self.toolOptionsPanel.setCurrentIndex(index)
        self.shadePanel.setCurrentIndex(index)

    # Configure Tool Options Panel
    def configToolOptionsPanel(self):
        # Add Pages
        self.toolOptionsPanel.addWidget(self.lineOptionsPanel)   # index 0
        self.toolOptionsPanel.addWidget(self.circleOptionsPanel) # index 1

        # Show Page 0 by Default
        self.toolOptionsPanel.setCurrentIndex(0)

        # Link with ComboBox
        self.toolSelectorBox.currentIndexChanged.connect(self.onToolChanged)

    # Configure Line Options Panel
    def configLineOptionsPanel(self):
        # Create Layout
        lineOptionsPanelLayout = QVBoxLayout(self.lineOptionsPanel)

        # Create Local Widgets
        lineToolOptionLabel = QLabel("Line Tool Options") 
        p1Label = QLabel("Point 1")
        p2Label = QLabel("Point 2")

        # Add Widgets to Panel
        lineOptionsPanelLayout.addWidget(lineToolOptionLabel)
        lineOptionsPanelLayout.addWidget(self.infiniteToggle)
        lineOptionsPanelLayout.addWidget(p1Label)
        lineOptionsPanelLayout.addWidget(self.p1Panel)
        lineOptionsPanelLayout.addWidget(p2Label)
        lineOptionsPanelLayout.addWidget(self.p2Panel)

        # Configure Background Colors
        lineToolOptionLabel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.infiniteToggle.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        p1Label.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.p1Panel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        p2Label.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.p2Panel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")

    # Configure Point 1 Panel
    def configP1Panel(self):
        # Create Layout
        p1PanelLayout = QHBoxLayout(self.p1Panel)

        # Create Local Widgets
        f1Label = QLabel("f1")
        f2Label = QLabel("f2")

        # Add Widgets to Panel
        p1PanelLayout.addWidget(f1Label)
        p1PanelLayout.addWidget(self.p1f1Value)
        p1PanelLayout.addWidget(f2Label)
        p1PanelLayout.addWidget(self.p1f2Value)

        # Configure Background Colors
        f1Label.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.p1f1Value.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        f2Label.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.p1f2Value.setStyleSheet("background-color: rgba(255, 255, 255, 180);")

    # Configure Point 2 Panel
    def configP2Panel(self):
        # Create Layout
        p2PanelLayout = QHBoxLayout(self.p2Panel)

        # Create Local Widgets
        f1Label = QLabel("f1")
        f2Label = QLabel("f2")

        # Add Widgets to Panel
        p2PanelLayout.addWidget(f1Label)
        p2PanelLayout.addWidget(self.p2f1Value)
        p2PanelLayout.addWidget(f2Label)
        p2PanelLayout.addWidget(self.p2f2Value)

        # Configure Background Colors
        f1Label.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.p2f1Value.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        f2Label.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.p2f2Value.setStyleSheet("background-color: rgba(255, 255, 255, 180);")

    # Configure Circle Options Panel
    def configCircleOptionsPanel(self):
        # Create Layout
        circleOptionsPanelLayout = QVBoxLayout(self.circleOptionsPanel)

        # Create Local Widgets
        circleToolOptionLabel = QLabel("Circle Tool Options") 
        centerLabel = QLabel("Center Point")
        radiusLabel = QLabel("Radius")
        circleAngleLabel = QLabel("Circle Angle")   

        # Add Widgets to Panel
        circleOptionsPanelLayout.addWidget(circleToolOptionLabel)
        circleOptionsPanelLayout.addWidget(centerLabel)
        circleOptionsPanelLayout.addWidget(self.centerPointPanel)
        circleOptionsPanelLayout.addWidget(radiusLabel)
        circleOptionsPanelLayout.addWidget(self.radiusPanel)
        circleOptionsPanelLayout.addWidget(circleAngleLabel)
        circleOptionsPanelLayout.addWidget(self.circleAnglePanel)

        # Configure Background Colors
        circleToolOptionLabel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        centerLabel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.centerPointPanel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        radiusLabel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.radiusPanel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        circleAngleLabel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.circleAnglePanel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")

    # Configure Center Panel
    def configcenterPointPanel(self):
        # Create Layout
        centerPointPanelLayout = QHBoxLayout(self.centerPointPanel)

        # Create Local Widgets
        f1Label = QLabel("f1")
        f2Label = QLabel("f2")

        # Add Widgets to Panel
        centerPointPanelLayout.addWidget(f1Label)
        centerPointPanelLayout.addWidget(self.cf1Value)
        centerPointPanelLayout.addWidget(f2Label)
        centerPointPanelLayout.addWidget(self.cf2Value)

        # Configure Background Colors
        f1Label.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.cf1Value.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        f2Label.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.cf2Value.setStyleSheet("background-color: rgba(255, 255, 255, 180);")

    # Configure Radius Panel
    def configRadiusPanel(self):
        # Create Layout
        radiusPanelLayout = QHBoxLayout(self.radiusPanel)

        # Create Local Widgets
        rLabel = QLabel("r")

        # Add Widgets to Panel
        radiusPanelLayout.addWidget(rLabel)
        radiusPanelLayout.addWidget(self.rValue)

        # Configure Background Colors
        rLabel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.rValue.setStyleSheet("background-color: rgba(255, 255, 255, 180);")

    # Configure Circle Angle Panel
    def configCircleAnglePanel(self):
        # Create Layout
        circleAnglePanelLayout = QHBoxLayout(self.circleAnglePanel)

        # Create Local Widgets
        t1Label = QLabel("t1")
        t2Label = QLabel("t2")

        # Add Widgets to Panel
        circleAnglePanelLayout.addWidget(t1Label)
        circleAnglePanelLayout.addWidget(self.cat1Value)
        circleAnglePanelLayout.addWidget(t2Label)
        circleAnglePanelLayout.addWidget(self.cat2Value)

        # Configure Background Colors
        t1Label.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.cat1Value.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        t2Label.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.cat2Value.setStyleSheet("background-color: rgba(255, 255, 255, 180);")

    # Configure Shade Options Panel
    def configShadePanel(self):
        # Add Pages
        self.shadePanel.addWidget(self.shadeLinePanel)   # index 0
        self.shadePanel.addWidget(self.shadeCirclePanel) # index 1

        # Show Page 0 by Default
        self.shadePanel.setCurrentIndex(0)

        # Link with ComboBox
        self.toolSelectorBox.currentIndexChanged.connect(self.onToolChanged)

    def configShadeLinePanel(self):
        # Create Layout
        shadeLinePanelLayout = QVBoxLayout(self.shadeLinePanel)

        # Create Local Widgets
        shadeDirectionLabel = QLabel("Shade Direction") 

        # Configure Shade Direction Options
        self.shadeDirectionBox.addItems(["Above", "Below", "Left", "Right"])

        # Add Widgets to Panel
        shadeLinePanelLayout.addWidget(shadeDirectionLabel)
        shadeLinePanelLayout.addWidget(self.shadeDirectionBox)

        # Configure Background Colors
        shadeDirectionLabel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.shadeDirectionBox.setStyleSheet("background-color: rgba(255, 255, 255, 180);" \
        "selection-background-color: transparent;" \
        "selection-color: black;")

    def configShadeCirclePanel(self):
        # Create Layout
        shadeCirclePanelLayout = QVBoxLayout(self.shadeCirclePanel)

        # Create Local Widgets
        shadeRegionLabel = QLabel("Shade Region") 

        # Configure Shade Direction Options
        self.shadeRegionBox.addItems(["Inside", "Outside"])

        # Add Widgets to Panel
        shadeCirclePanelLayout.addWidget(shadeRegionLabel)
        shadeCirclePanelLayout.addWidget(self.shadeRegionBox)

        # Configure Background Colors
        shadeRegionLabel.setStyleSheet("background-color: rgba(255, 255, 255, 180);")
        self.shadeRegionBox.setStyleSheet("background-color: rgba(255, 255, 255, 180);" \
        "selection-background-color: transparent;" \
        "selection-color: black;")
    
# Create the App and Window, Show the Window and Start the App
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# Only Execute this File if its Run Directly
if __name__ == "__main__":
    main()
