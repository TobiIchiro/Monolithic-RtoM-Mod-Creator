import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, 
    QWidget, QLabel, QVBoxLayout, QCheckBox,
    QGroupBox, QFormLayout, QPushButton
    )
from PySide6.QtGui import QIcon
import os
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.mods = [
            "Mod_FatStacks",
            "Mod_EpicPacksEverywhere",
            "Mod_CraftableWearable",
            "Mod_RestoreMarshuzShayarAmzulArmors",
            "Mod_SandboxItemsInCampaign",
            "Mod_RestoreConstructions",
            "Mod_CustomConstructions"
        ]

        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout()

        self.modsGroup = QGroupBox("Mods")
        self.modsGroupLayout = QVBoxLayout()
        self.modCheckBoxes = []

        for mod in self.mods:
            checkBox = QCheckBox(mod)
            self.modCheckBoxes.append(checkBox)
            self.modsGroupLayout.addWidget(checkBox)
        
        self.modsGroup.setLayout(self.modsGroupLayout)
        layout.addWidget(self.modsGroup)

        self.submitButton = QPushButton("Generate Mod")
        layout.addWidget(self.submitButton)

        self.setLayout(layout)

    def createMod(self):
        #Check which ones are active
            #priority
            #Top
            #1. CraftableWereable
            #2. CustomConstructions
            #3. RestoreConstructions
            #4. RestoreMSAArmor
            #5. SandboxInCampaign
            #6. FatStacks
            #7. EpicPacksEverywere
        #if CraftableWereable is selected
            #append recipes
        #if CustomConstructions is selected
            #append architecture
            #append constructions
            #append construction recipes
            #append hammer to DT_Tools
            #append hammer recipe
        #if RestoreConstructions is selected
            #enable constructions
        #if RestoreMSAArmor is selected
            #execute script to restore
        #if SandboxInCampaign is selected
            #execute script to enable in capaign
        #if FatStacks is selected
            #execture script to set value to 9999
        #if EpicPacksEverywere
            #EpicPAcksEverywere script

        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())