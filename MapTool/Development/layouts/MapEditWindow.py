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
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
import os


#==================================================================================================
#======variable declare============================================================================
class myMapEditWindow(QWidget):
    def __init__(self, parent = None):
        super(myMapEditWindow, self).__init__(parent)
        #===========variable==============================================


        #-----layouts Initial-----
        self.mapGridLayout = QGridLayout()
        
        #*****************************************************************
        #-----Widgets Initial setting-------------------------------------
        self.setBackgroundColor(self, Qt.green)
        #--------------------------------

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