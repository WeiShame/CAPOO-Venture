"""**************************************************************
*   Desciribe:                                                  *
*       clickable Lable                                         *
*                                                               *
*   Date    : 2023/10/29                                        *
*   Author  : YongHong, Liu                                     *
*                                                               *
**************************************************************"""
#======import part=================================================================================
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import pyqtSlot, pyqtSignal
import os, glob
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#==================================================================================================
#======variable declare============================================================================
class myClickableLabel(QLabel):
    clickSignal = pyqtSignal()
    def __init__(self, parent = None):
        super(myClickableLabel, self).__init__(parent)
        self.clicked = False
        #===========variable==============================================
    def mouseReleaseEvent(self, event):
        self.clickSignal.emit()
    #*********************************************
    def click_connect(self,func):
        self.clickSignal.connect(func)
    #*********************************************
    def selected(self):
          self.setStyleSheet("border: 3px solid black;")
    #*********************************************
    def unSelected(self):
          self.setStyleSheet("border: 0px") 
    

        

        
        #*****************************************************************
        #-----button link setting-----------------------------------------
        
        
        #*****************************************************************
        
        
    #=====================================================================

    #=====================================================================

    #=====================================================================

        