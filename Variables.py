#! /usr/bin/env python
#-*-coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore

import os,sys,subprocess, datetime

from functions import list_search_0

def initVariables(self):
    self.version = 'GUI HGCal Electron Validations v0.5.0.0'
    
    self.texte = ""
    self.validationType1 = 'Full'   # default
    self.validationType2 = 'RECO'   # default
    self.validationType3 = 'RECO' # default
    self.choice_rel = ""
    self.choice_ref = ""
    self.coll_list = []
    self.files_list = []
    self.my_choice_rel = "" # release to work on
    self.my_choice_ref = "" # reference for comparison
    self.my_choice_tmp = "" # to store reference when working with miniAOD, pmx vs pmx or Fast vs Full.
    self.releasesList_ref_2_tmp = [] # to store the reference root files list
    self.ref_list_1_tmp = [] # to store the reference datasets

    self.working_dir_base = os.getcwd()
    self.working_dir_rel = os.getcwd()
    self.working_dir_ref = os.getcwd()
    self.working_dir_report = ""
    self.finalFolder = ""
    self.location = ""
    self.URL = ""
    self.exist_working_dir_rel = False
    self.exist_working_dir_ref = False
    self.exist_finalFolder = False
    self.temp_rl = '' # for release web folder name modification
    self.temp_rf = '' # for reference web folder name modification
    self.selected_files_rel = []
    self.selected_files_ref = []
        
    self.releasesList_0 = list_search_0(self) # list of releases in https://cmsweb.cern.ch/dqm/relval/data/browse/ROOT/
    self.releasesList_rel_1 = []
    self.releasesList_ref_1 = []
    self.releasesList_rel_2 = []
    self.releasesList_ref_2 = []
    self.releasesList_rel_3 = []
    self.releasesList_ref_3 = []
    self.releasesList_rel_3b = []
    self.releasesList_ref_3b = []
    self.releasesList_rel_5 = []
    self.releasesList_ref_5 = []
    self.my_choice_rel_0 = "" # 
    self.my_choice_rel_1 = "" # 
    self.my_choice_ref_0 = "" # 
    self.my_choice_ref_1 = "" # 
    self.rel_list_0 = []
    self.ref_list_0 = []
    self.rel_list_1 = []
    self.ref_list_1 = []
    self.rel_list_2 = []
    self.ref_list_2 = []
    self.profondeur_rel = 0
    self.profondeur_ref = 0
    self.target = ""
    self.reference = ""
    self.referenceList = []
    self.refList = []
    self.finalList = []
    
    now = datetime.datetime.now()
    globalReportName = self.working_dir_rel + '/report_' + now.strftime("%Y_%m_%d-%H%M%S") + '.txt'
    try:
        self.wp = open(globalReportName, 'w') # report page
    except IOError as ioe:
        print("Can not open %s file! " % globalReportName)
        BoiteMessage = QMessageBox()
        BoiteMessage.setText("cannot open report.txt file !!")
        BoiteMessage.setIcon(QMessageBox.Critical)
        BoiteMessage.setWindowTitle("WARNING !")
        BoiteMessage.exec_()
    
    self.textReport = ""
    
    # Release : the release to be validated
    # Reference : the reference release
    # Lists : list of globalTags for release/reference
    # Selected : the selected globalTag and associated DataSets
    self.tasks_list = ['Release list', 'Reference list', 'Lists', 'Selected', 'Web page'] # 
    self.tasks_counter = 0
    self.tasks_counterMax = len(self.tasks_list) - 1
    self.wp.write("self.tasks_counterMax = %d\n" % self.tasks_counterMax)
    self.textReport += "self.tasks_counterMax = " + str(self.tasks_counterMax) + "<br>"
    self.textReport += 'self.tasks_counter = ' + str(self.tasks_counter) + '/' + str(self.tasks_counterMax) + '<br>'
    self.textReport += '<b><font color=\'blue\'> release selection </font></b>' + '<br>'
    
    self.selectedDataSets = []
    
    self.allMenuListDatasetsChecked = False # default
    self.checkFastvsFull = False # default
    
    self.listHeader = ["DataSets", "GlobalTags"]
    
    self.selectedRelDatasets = ""
    self.selectedRefDatasets = ""
    self.selectedRelGlobalTag = ""
    self.selectedRefGlobalTag = ""
    
    self.okToPublishDatasets = ""
    self.okToPublishFvsFDatasets = ""
    self.okToDisplayFvsFDatasets = "" # only for display
    
    self.filesHistos = ['ElectronMcSignalHistosPt1000.txt', 'ElectronMcSignalHistosMiniAOD.txt', 'ElectronMcSignalHistos.txt', 'ElectronMcFakeHistos.txt']

    
    return
    
