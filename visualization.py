#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
from PyQt5 import QtWidgets, QtCore, QtGui


class ImageWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        self.initUI()
    
    def initUI(self):
        self.resize(400,400)
        self.label = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap("AllFiles/02674 S01.jpg")
        self.label.setPixmap(pixmap.scaled(400,400))
        self.show()

class Visualizator(QtWidgets.QDialog):
    def readJson(self):
        with open("data.json","r") as f:
            self.overall = json.load(f)
            self.allTags = sorted(self.overall["AllTags"])
            self.tagsFilesMap = self.overall["Tags"]
            for tag in self.tagsFilesMap:
                self.tagsFilesMap[tag]=set(self.tagsFilesMap[tag])            
        
    def __init__(self, parent=None):
        self.readJson()
        
        super(Visualizator, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.ExtendedSelection
        )
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 211, 291))
        for tag in self.allTags:
            item = QtWidgets.QListWidgetItem(tag)
            self.listWidget.addItem(item)
        self.listWidget.itemClicked.connect(self.printItemText)
        self.layout.addWidget(self.listWidget)
        self.setLayout(self.layout)

    def printItemText(self):
        items = self.listWidget.selectedItems()
    
        commonFiles = set(self.tagsFilesMap[items[0].text()])
        for item in items:
            files = self.tagsFilesMap[item.text()]
            commonFiles = files.intersection(commonFiles)            
            #if len(commonFiles) == 0:
            #    image = ImageWidget()
        #x=[]
        #for i in range(len(items)):
        #    x.append(str(self.listWidget.selectedItems()[i].text()))
        #if len(commonFiles)<4:
        #    self.widget = ImageWidget(self)
            #for file in CommonFiles:
                
        print(commonFiles)

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    form = Visualizator()
    form.show()
    image = ImageWidget()
    app.exec_()