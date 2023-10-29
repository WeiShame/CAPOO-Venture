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
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont, QPixmap, QMouseEvent
from PyQt5.QtCore import pyqtSlot, Qt, QSize
import os, glob
from layouts.ClickableLabel import myClickableLabel


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
        self.blockSize = QSize(60, 48)
        self.materialLabels = []

        self.selectTemp = myClickableLabel()

        self.mapMaterials = glob.glob("Images/Materials/*.png")


        #-----layouts Initial-----
        self.materialFormGridLayout = QGridLayout()
        
        #*****************************************************************
        #-----Widgets Initial setting-------------------------------------
        #-----load material images-----
        for image_str in self.mapMaterials:
            materialPixmap = QPixmap(image_str)
            materialBlockLabel = myClickableLabel()
            materialBlockLabel.setPixmap(materialPixmap)
            materialBlockLabel.resize(self.blockSize)

            materialBlockLabel.click_connect(self.materialClicked)


            self.materialLabels.append(materialBlockLabel)            
       

        #--------------------------------
        self.setBackgroundColor(self.materialForm, Qt.gray)
        self.setBackgroundColor(self.monsterForm, Qt.cyan)

        #*****************************************************************
        #-----layout setting----------------------------------------------
        self.addTab(self.materialForm, self.materiaLabel)
        self.addTab(self.monsterForm, self.monsterLabel)
        
        for index, materialImageLabel in enumerate(self.materialLabels):
            self.materialFormGridLayout.addWidget(materialImageLabel, int(index/2), int(index % 2))

        if self.materialFormGridLayout.rowCount() < 5:
            self.materialFormGridLayout.setRowStretch(self.materialFormGridLayout.rowCount(), 1)


        self.materialForm.setLayout(self.materialFormGridLayout)
    

        

        
        #*****************************************************************
        #-----button link setting-----------------------------------------
        
        
        #*****************************************************************
        
        
    #=====================================================================
    def setBackgroundColor(self, widget, color):
        widget.setAutoFillBackground(True)
        pal = QPalette()
        pal.setColor(widget.backgroundRole(), color)
        widget.setPalette(pal)
    #=====================================================================
    def checkMaterials(self):
        if len(self.mapMaterials) == 0:
            error_dialog = QtWidgets.QMessageBox.critical(self,"ERROR!", "Not Found Materials Error!")
            self.close()
    #=====================================================================
    def materialClicked(self):
        sender_label = self.sender()
        self.selectTemp.unSelected()
        sender_label.selected()
        self.selectTemp=sender_label
        
        