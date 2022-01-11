from PySide2 import QtCore
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QMainWindow, QTableView, QPushButton, QMessageBox, QComboBox

from org.cu.api.ManagerService import ManagerService
from org.cu.common.MessageCommon import showMessageSDC
from org.cu.dao.JobPositionDao import JobPositionDao

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Manager apply position implements the parent abstract class ManagerService
'''
class ManagerPositionImpl(ManagerService):

    # init attributes associate the main window (QMainWindow), JobPositionDao
    def __init__(self, window: QMainWindow):
        self._jobPositionDao = JobPositionDao()
        self._window = window
        self._tableViewMJob = None
        self._modelMJob = None
        self._pushButtonMJobSave = None
        # bind event must be in here, can not write it into function
        self._window.findChild(QPushButton, "pushButtonMJobSave").clicked.connect(self.modify)

    # init the job manager ui page
    def load(self):
        # setting table header
        self._tableViewMJob = self._window.findChild(QTableView, "tableViewMJob")
        self._modelMJob = QStandardItemModel(0, 2)
        self._modelMJob.setHorizontalHeaderLabels(['ID', 'Job Position'])
        # setting table rows
        records = self._jobPositionDao.query()
        titles = list()
        for record in records:
            titles.append(record[1])
            self._modelMJob.appendRow([QStandardItem(str(record[0])), QStandardItem(record[1])])
        n = len(records)
        while n < 10:
            self._modelMJob.appendRow([QStandardItem(""), QStandardItem("")])
            n += 1
        self._tableViewMJob.setModel(self._modelMJob)
        # update position comboBox for apply from
        self.__updateDisplay(titles)

    # add or modify job position
    @QtCore.Slot()
    def modify(self):
        # show operation result
        res = showMessageSDC(None, self.load)
        # if not choose save then do nothing
        if res != QMessageBox.Save:
            return
        # choose save
        # delete all
        self._jobPositionDao.delete()
        # insert all data into database
        n = self._modelMJob.rowCount()
        titles = list()
        for i in range(n):
            title = self._modelMJob.item(i, 1).text()
            if title is None or len(title) == 0:
                continue
            titles.append(title)
            # insert data into database
            self._jobPositionDao.updateOrInsert(title)
        # re-load data from database
        self.load()
        # update position comboBox for apply from
        self.__updateDisplay(titles)

    # refresh data to display
    def __updateDisplay(self, items: list):
        if items is None or len(items) == 0:
            return
        comboBoxPosition = self._window.findChild(QComboBox, "comboBoxPosition")
        comboBoxPosition.clear()
        for item in items:
            comboBoxPosition.addItem(item)


# mp = ManagerPositionImpl(None)
