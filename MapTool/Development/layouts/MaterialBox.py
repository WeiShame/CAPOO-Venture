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
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QTabWidget
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
import os


#==================================================================================================
#======variable declare============================================================================
class myMaterialBox(QTabWidget):
    def __init__(self, parent = None):
        super(myMaterialBox, self).__init__(parent)
        #===========variable==============================================
        self.materiaLabel = "Material"
        self.monsterLabel = "Monster"
        self.materialForm = QWidget()
        self.monsterForm = QWidget()

        self.materialBlockLabel = QLabel()
        self.materialBlockPixmap = QPixmap("Images/block1.png")
 
        self.materialQuestionLabel = QLabel()
        self.materialQuestionPixmap = QPixmap("Images/question.png")

        #-----layouts Initial-----
        self.materialFormGridLayout = QGridLayout()
        print(os.path.dirname(os.path.abspath(__file__)))
        
        #*****************************************************************
        #-----Widgets Initial setting-------------------------------------
        self.setBackgroundColor(QColor(255, 255, 255))

        self.materialBlockLabel.setPixmap(self.materialBlockPixmap)
        self.materialBlockLabel.resize(60,48)

        self.materialQuestionLabel.setPixmap(self.materialQuestionPixmap)
        self.materialQuestionLabel.resize(60,48)
        #--------------------------------
        
        #*****************************************************************
        #-----layout setting----------------------------------------------
        self.addTab(self.materialForm, self.materiaLabel)
        self.addTab(self.monsterForm, self.monsterLabel)
        
        self.materialFormGridLayout.addWidget(self.materialBlockLabel, 0, 0)
        self.materialFormGridLayout.addWidget(self.materialQuestionLabel, 0, 1)
        self.materialFormGridLayout.setRowStretch(1,4)

        self.materialForm.setLayout(self.materialFormGridLayout)

        

        
        #*****************************************************************
        #-----button link setting-----------------------------------------
        
        
        #*****************************************************************
        
        
    #=====================================================================
    def setBackgroundColor(self, color):
        pal = QPalette()
        pal.setColor(self.backgroundRole(), color)
        self.setPalette(pal)