# JobAppSystem
The GUI application by Python3.8. Using QT Design draw UI and generator UI XML file provides to PySide2 build GUI components.  Total adopt  OOD design class, service, and abstract class. OOP implemented this project. 

# Introduction
This is a simple demo as my study case for  University of Coventry & PSB Singapore
author full Chinese name is Liu JiaGe, the English name is Eric, this is my first model need to implement a
study case and required use Python, before I use Python very less, for this time also give me an opportunity
to study how to use Python to do a GUI project.
about the study case is study and exam content from school so it can not open to everyone.

1. Environment
IDE, PyCharm
Python, 3.8
GUI API, PySide2
QTDesigner, designer UI XML
Database, sqlite3
OS, Mac Pro
2. Package Hierarchy
JobAppSystem
    --->readme.txt                      #Help to understand and start the project
    --->org
        --->cu
            --->api
                ApplicationService      #Definition abstract functions to implements apply job for the role of applicant
                ReviewerService         #Definition abstract functions to implements review job for the role of reviewer
                ManagerService          #Definition abstract functions to implements manager job positions for the role of manger
            --->common
                ConvertCommon           #Convert ui data to entity object
                MessageCommon           #Provide common message window, like pop alert,confirm sub-window
                ToolsCommon             #Provide common functions, like get unique id, current data...
                Serializable            #Provide object to JSON
            --->dao
                ...
                DaoService.py           #Handle operation database and provide basically functions to access database and initial tables of database when the first started.
            --->entity
                ...
            --->implement
                ...                     #implements all functions reference the package api
                JobApplication          #Load all of sub-page, it was called by MainWindow
            --->resources
                --->database
                    job.db              #Database sqlite3
                --->gui
                    job.ui              #All GUI design by QTDesigner
            --->test                    #For testing
                --->resources
                    --->gui
            MainWindow.py               #Main Window with main function, it can start project.
3. How to start it
if you have been installed Python, 3.8 on your computer, only need you to start main window(MainWindow.py) enjoy it.
