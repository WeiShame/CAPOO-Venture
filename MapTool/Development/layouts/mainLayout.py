"""**************************************************************
*   Desciribe:                                                  *
*       The main form of my Map tool.         s                  *
*                                                               *
*   Date    : 2021/06/06                                        *
*   Author  : YongHong, Liu                                     *
*                                                               *
**************************************************************"""
#======import part=================================================================================
import sys
from tkinter import Label
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QMainWindow, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont
from PyQt5.QtCore import pyqtSlot, Qt
from layouts.MaterialBox import myMaterialBox
from layouts.MapEditWindow import myMapEditWindow

#==================================================================================================
#======variable declare============================================================================
class myMainLayout(QMainWindow):
    def __init__(self, parent = None):
        super(myMainLayout, self).__init__(parent)
        #===========variable==============================================
        self.window_width = 1080
        self.window_height = 720
        self.materialBox = myMaterialBox()
        self.mapEditWindow = myMapEditWindow()

        self.mainframe = QWidget()      # It need a central widget for mainwidow.

        self.boxLabel = QLabel("Material Box")
        self.mapLabel = QLabel("Map")
        # layouts Initial
        self.gridLayout = QGridLayout()
        #*****************************************************************
        #-----Widgets Initial setting-------------------------------------
        self.setWindowTitle('Map Tool')    # set window title
        self.setWindow2Center()
        self.setFixedSize(self.window_width, self.window_height) # Fixed the size of window
        self.setBackgroundColor(QColor(255, 240, 195))

        #----- Settting lables font -----
        labelfont = QFont()
        labelfont.setPointSize(16)
        labelfont.setBold(True)

        self.boxLabel.setFont(labelfont)
        self.mapLabel.setFont(labelfont)

        #--------------------------------
        
        #*****************************************************************
        #-----layout setting----------------------------------------------
        self.setCentralWidget(self.mainframe)

        #self.gridLayout.setColumnStretch(3,1)

        self.gridLayout.addWidget(self.boxLabel, 0, 0, Qt.AlignLeft)
        self.gridLayout.addWidget(self.mapLabel, 0, 3)
        self.gridLayout.addWidget(self.materialBox,1,0,9,2)
        self.gridLayout.addWidget(self.mapEditWindow, 1, 3, 9, 7)
        
        self.mainframe.setLayout(self.gridLayout)
        #*****************************************************************
        #-----button link setting-----------------------------------------
        
        
        #*****************************************************************
        
        
    #=====================================================================
    #===========function==================================================
    def setWindow2Center(self):
        screenSize = QDesktopWidget().screenGeometry()  # get screen size
        print("Sw: ", screenSize.width(), "Sh: ", screenSize.height())
        self.setGeometry((screenSize.width() - self.window_width) /2 , (screenSize.height() - self.window_height) / 2, self.window_width, self.window_height)    

    #*****************************************************************
    def setBackgroundColor(self, color):
        pal = QPalette()
        pal.setColor(self.backgroundRole(), color)
        self.setPalette(pal)