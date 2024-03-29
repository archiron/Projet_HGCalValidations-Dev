#! /usr/bin/env python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore

from Datasets_default import DataSetsFilter
from Paths_default import *

def initGpCalcul(self):

    self.QGBox1 = QGroupBox("Comparison")
    self.QGBox1.setMaximumHeight(120)
    self.QGBox1.setMinimumWidth(120)
    self.radio11 = QRadioButton("FULL vs FULL") # default
    self.radio12 = QRadioButton("FAST vs FAST")
    self.radio13 = QRadioButton("FAST vs FULL")
    self.radio11.setChecked(True)
    self.radio11.setEnabled(False)
    self.radio12.setEnabled(False)
    self.radio13.setEnabled(False)
    self.connect(self.radio11, SIGNAL("clicked()"), self.radio11Clicked) 
    self.connect(self.radio12, SIGNAL("clicked()"), self.radio12Clicked) 
    self.connect(self.radio13, SIGNAL("clicked()"), self.radio13Clicked) 
    vbox1 = QVBoxLayout()
    vbox1.addWidget(self.radio11)
    vbox1.addWidget(self.radio12)
    vbox1.addWidget(self.radio13)
    vbox1.addStretch(1)
    self.QGBox1.setLayout(vbox1)
    return
    
def initGpSpecTarget(self):

    self.QGBox2 = QGroupBox("Validation")
    self.QGBox2.setMaximumHeight(120)
    self.QGBox2.setMinimumWidth(100)
    self.checkSpecTarget1 = QRadioButton("RECO") # default
    self.checkSpecTarget2 = QRadioButton("PU25")
    self.checkSpecTarget3 = QRadioButton("PUpmx25")
    self.checkSpecTarget4 = QRadioButton("miniAOD")
    self.checkSpecTarget5 = QRadioButton("PU140")
    self.checkSpecTarget6 = QRadioButton("PU200")
    self.checkSpecTarget1.setChecked(True) #default
    self.checkSpecTarget1.setEnabled(False)
    self.checkSpecTarget2.setEnabled(False)
    self.checkSpecTarget3.setEnabled(False)
    self.checkSpecTarget4.setEnabled(False)
    self.checkSpecTarget5.setEnabled(False)
    self.checkSpecTarget6.setEnabled(False)
    self.connect(self.checkSpecTarget1, SIGNAL("clicked()"), self.checkSpecTarget1_Clicked) 
    self.connect(self.checkSpecTarget2, SIGNAL("clicked()"), self.checkSpecTarget2_Clicked) 
    self.connect(self.checkSpecTarget3, SIGNAL("clicked()"), self.checkSpecTarget3_Clicked) 
    self.connect(self.checkSpecTarget4, SIGNAL("clicked()"), self.checkSpecTarget4_Clicked) 
    self.connect(self.checkSpecTarget5, SIGNAL("clicked()"), self.checkSpecTarget5_Clicked) 
    self.connect(self.checkSpecTarget6, SIGNAL("clicked()"), self.checkSpecTarget6_Clicked) 
    vbox2 = QVBoxLayout()
    vbox2.addWidget(self.checkSpecTarget1)
    vbox2.addWidget(self.checkSpecTarget2)
    vbox2.addWidget(self.checkSpecTarget3)
    vbox2.addWidget(self.checkSpecTarget4)
    vbox2.addWidget(self.checkSpecTarget5)
    vbox2.addWidget(self.checkSpecTarget6)
    vbox2.addStretch(1)
    self.QGBox2.setLayout(vbox2)
    return

def initGpSpecReference(self):

    self.QGBoxSpecReference = QGroupBox("Spec/Ref")
    self.QGBoxSpecReference.setMaximumHeight(120)
    self.QGBoxSpecReference.setMinimumHeight(120)
    self.checkSpecReference1 = QRadioButton("RECO") #default
    self.checkSpecReference2 = QRadioButton("PU25")
    self.checkSpecReference3 = QRadioButton("PUpmx25")
    self.checkSpecReference4 = QRadioButton("miniAOD")
    self.checkSpecReference5 = QRadioButton("PU140")
    self.checkSpecReference6 = QRadioButton("PU200")
    self.checkSpecReference1.setChecked(True) #default
    self.checkSpecReference1.setEnabled(False)
    self.checkSpecReference2.setEnabled(False)
    self.checkSpecReference3.setEnabled(False)
    self.checkSpecReference4.setEnabled(False)
    self.checkSpecReference5.setEnabled(False)
    self.checkSpecReference6.setEnabled(False)
    self.connect(self.checkSpecReference1, SIGNAL("clicked()"), self.checkSpecReference1_Clicked)
    self.connect(self.checkSpecReference2, SIGNAL("clicked()"), self.checkSpecReference2_Clicked)
    self.connect(self.checkSpecReference3, SIGNAL("clicked()"), self.checkSpecReference3_Clicked)
    self.connect(self.checkSpecReference4, SIGNAL("clicked()"), self.checkSpecReference4_Clicked)
    self.connect(self.checkSpecReference5, SIGNAL("clicked()"), self.checkSpecReference5_Clicked)
    self.connect(self.checkSpecReference6, SIGNAL("clicked()"), self.checkSpecReference6_Clicked)
    vboxSpecReference = QVBoxLayout()
    vboxSpecReference.addWidget(self.checkSpecReference1)
    vboxSpecReference.addWidget(self.checkSpecReference2)
    vboxSpecReference.addWidget(self.checkSpecReference3)
    vboxSpecReference.addWidget(self.checkSpecReference4)
    vboxSpecReference.addWidget(self.checkSpecReference5)
    vboxSpecReference.addWidget(self.checkSpecReference6)
    vboxSpecReference.addStretch(1)
    self.QGBoxSpecReference.setLayout(vboxSpecReference)
        				
    return

def initGpAllNone(self):

    self.QGBoxAllNone = QGroupBox("All / None")
    self.QGBoxAllNone.setMaximumHeight(120)
    self.QGBoxAllNone.setMinimumHeight(120)
    self.checkAllNone1 = QRadioButton("All")
    self.checkAllNone2 = QRadioButton("None")
    self.checkAllNone1.setChecked(True)
    self.checkAllNone1.setEnabled(False)
    self.checkAllNone2.setEnabled(False)
    self.connect(self.checkAllNone1, SIGNAL("clicked()"), self.checkAllNone1Clicked)
    self.connect(self.checkAllNone2, SIGNAL("clicked()"), self.checkAllNone2Clicked)
    vboxAllNone = QVBoxLayout()
    vboxAllNone.addWidget(self.checkAllNone1)
    vboxAllNone.addWidget(self.checkAllNone2)
    vboxAllNone.addStretch(1)
    self.QGBoxAllNone.setLayout(vboxAllNone)
  
    return

def initGpDataSets(self):

    self.QGBoxDataSets = QGroupBox("DataSets")
    self.QGBoxDataSets.setMaximumHeight(120)
    self.QGBoxDataSets.setMinimumHeight(120)
    self.checkDataSets1 = QPushButton("List")
    self.checkDataSets2 = QPushButton("Reload")
    self.checkDataSets1.setEnabled(False)
    self.checkDataSets2.setEnabled(False)
    self.connect(self.checkDataSets2, SIGNAL("clicked()"), self.checkDataSets2Clicked)
    self.menu = QMenu()
    self.ag = QActionGroup(self, exclusive=False)
    self.DataSetTable = DataSetsFilter(self)
    for item in self.DataSetTable:
        (item_name, item_checked) = item
        a = self.ag.addAction(QAction(item_name, self, checkable=True, checked=item_checked)) # checked=True
        self.menu.addAction(a)
        self.connect(a, SIGNAL('triggered()'), self.QGBoxListsUpdate)
    self.checkDataSets1.setMenu(self.menu)
    self.selectedDataSets = self.DataSetTable # default, all datasets selected
    vboxDataSets = QVBoxLayout()
    vboxDataSets.addWidget(self.checkDataSets1)
    vboxDataSets.addWidget(self.checkDataSets2)
    vboxDataSets.addStretch(1)
    self.QGBoxDataSets.setLayout(vboxDataSets)
        
    return

def initGpFolderName(self): # can add modification on release name to obtain the folder name for the web page.

    self.QGBoxFolderName = QGroupBox("Web folder name customization : ")
    self.QGBoxFolderName.setMaximumHeight(120)
    self.QGBoxFolderName.setMinimumHeight(120)
    self.label_rel = QLabel("Release : ", self) # Release customization
    self.label_rel.setMaximumWidth(150)
    self.label_rel.setMinimumWidth(150)
    self.lineEdit_rel = QLineEdit(self)
    self.lineEdit_rel.setMaximumWidth(300)
    self.lineEdit_rel.setMinimumWidth(200)
    self.lineEdit_rel.connect(self.lineEdit_rel, SIGNAL("textChanged(QString)"), self.changeText)
    self.label_ref = QLabel("Reference  : ", self) # Reference customization
    self.label_ref.setMaximumWidth(150)
    self.label_ref.setMinimumWidth(150)
    self.lineEdit_ref = QLineEdit(self)
    self.lineEdit_ref.setMaximumWidth(300)
    self.lineEdit_ref.setMinimumWidth(200)
    self.lineEdit_ref.connect(self.lineEdit_ref, SIGNAL("textChanged(QString)"), self.changeText)
    vbox_FolderName = QVBoxLayout()
    hbox1 = QHBoxLayout()
    hbox2 = QHBoxLayout()
    self.lineEdit_ref.setEnabled(False)
    self.lineEdit_rel.setEnabled(False)
    hbox1.addWidget(self.label_rel)
    hbox1.addWidget(self.lineEdit_rel)
    hbox2.addWidget(self.label_ref)
    hbox2.addWidget(self.lineEdit_ref)
    vbox_FolderName.addLayout(hbox1)
    vbox_FolderName.addLayout(hbox2)
    vbox_FolderName.addStretch(1)
    self.QGBoxFolderName.setLayout(vbox_FolderName)

    return

def initGpLocation(self):

    self.QGBoxLocation = QGroupBox("Location")
    self.QGBoxLocation.setMaximumHeight(120)
    self.QGBoxLocation.setMinimumHeight(120)
    self.checkLocation1 = QPushButton("List")
    self.checkLocation2 = QPushButton("Reload")
    self.checkLocation1.setEnabled(False)
    self.checkLocation2.setEnabled(False)
    self.connect(self.checkLocation2, SIGNAL("clicked()"), self.checkLocation2Clicked)
    self.menu_loc = QMenu()
    self.loc = QActionGroup(self, exclusive=True)
    self.LocationTable = LocationFilter(self)
    for item in self.LocationTable:
        (item_name, item_checked, item_location) = item
        a2 = self.loc.addAction(QAction(item_name, self, checkable=True, checked=item_checked)) # checked=True
        self.menu_loc.addAction(a2)
        self.connect(a2, SIGNAL('triggered()'), self.PathUpdate)
    self.checkLocation1.setMenu(self.menu_loc)
    vboxLocation = QVBoxLayout()
    vboxLocation.addWidget(self.checkLocation1)
    vboxLocation.addWidget(self.checkLocation2)
    vboxLocation.addStretch(1)
    self.QGBoxLocation.setLayout(vboxLocation)
    return

def initGpResume(self):

    self.QGBoxRelRef = QGroupBox("release")
    self.QGBoxRelRef.setMaximumHeight(120)
    self.QGBoxRelRef.setMinimumHeight(120)
    self.QGBoxRelRef.setMinimumWidth(250)
        
    self.labelCombo1 = QLabel(self.trUtf8("Release"), self)   # label used for resuming the rel/ref.
    self.labelCombo2 = QLabel(self.trUtf8("Reference"), self) # label used for resuming the rel/ref.

    vbox6 = QVBoxLayout()
    vbox6.addWidget(self.labelCombo1) 
    vbox6.addWidget(self.labelCombo2) 
    vbox6.addStretch(1)
    self.QGBoxRelRef.setLayout(vbox6)
    return

def initGpOptions(self):
	# creation du grpe Calcul
    initGpCalcul(self)
    
	# creation du grpe Validation
    initGpSpecTarget(self)
        				
	# creation du grpe Specific/Global
    initGpSpecReference(self)

    # creation du grpe initGpDataSets
    initGpDataSets(self)
    
    # creation du gpe initGpFolderName
    initGpFolderName(self)
    
    # creation du grpe All/None
    initGpAllNone(self)

    # creation du grpe Location
    initGpLocation(self)
    
    # creation des Label pour release/reference resume
    initGpResume(self)    
    
    #Layout intermédiaire : création et peuplement des gpes radios
    self.layoutH_radio = QHBoxLayout()
    self.layoutH_radio.addWidget(self.QGBox1)
    self.layoutH_radio.addWidget(self.QGBox2)
    self.layoutH_radio.addWidget(self.QGBoxSpecReference)
    self.layoutH_radio.addWidget(self.QGBoxAllNone)
    self.layoutH_radio.addWidget(self.QGBoxDataSets)
    self.layoutH_radio.addStretch(1)
    self.layoutH_radio.addWidget(self.QGBoxFolderName)
    self.layoutH_radio.addStretch(1)
    self.layoutH_radio.addWidget(self.QGBoxLocation)
    self.layoutH_radio.addWidget(self.QGBoxRelRef)

    return

