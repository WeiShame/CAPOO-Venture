"""**************************************************************
*   Desciribe:                                                  *
*       The main form of my Map tool.                           *
*                                                               *
*   Date    : 2021/06/21                                        *
*   Author  : YongHong, Liu                                     *
*                                                               *
**************************************************************"""
#======import part=================================================================================
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit, QTabWidget
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont, QPixmap, QImage, QBrush
from PyQt5.QtCore import pyqtSlot, Qt
import os
from layouts.ClickableLabel import myClickableLabel

#==================================================================================================
#======variable declare============================================================================
class myMapEditWindow(QWidget):
    def __init__(self, parent = None):
        super(myMapEditWindow, self).__init__(parent)
        #===========variable==============================================
        self.horizontalBlockCount = 16
        self.verticalBlockCount = 15
        self.Blocks = []

        #-----layouts Initial-----
        self.mapGridLayout = QGridLayout()
        
        #*****************************************************************
        #-----Widgets Initial setting-------------------------------------
        self.setBackgroundColor(self, Qt.green)
        #--------------------------------
        # create 16 * 15 block for editmapwindow
        for row in range(self.verticalBlockCount):
            tempRowLabelList = []
            for column in range(self.horizontalBlockCount):
                templabel = myClickableLabel()
                templabel.setBackgroundColor(templabel, Qt.white)
                templabel.setBorder(1)
                tempRowLabelList.append(templabel)
                self.mapGridLayout.addWidget(templabel, column, row)
            # init blocks 2 dim list
            self.Blocks.append(tempRowLabelList)
        
        print("columns: {}; rows: {}".format(len(self.Blocks[0]), len(self.Blocks)))
            

        #*****************************************************************
        #-----layout setting----------------------------------------------
        self.setLayout(self.mapGridLayout)
        
        #*****************************************************************
        #-----button link setting-----------------------------------------
        
        
        #*****************************************************************
        
        
    #=====================================================================
    def setBackgroundColor(self, widget, color):
        widget.setAutoFillBackground(True)
        pal = QPalette()
        pal.setColor(widget.backgroundRole(), color)
        widget.setPalette(pal)
    #--------------------------------------------------------------
    def setBackgroundimage(self, imagePath):
        oImage = QImage(imagePath)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(oImage))
        self.setPalette(palette)