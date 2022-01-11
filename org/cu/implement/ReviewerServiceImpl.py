from typing import Tuple

import PySide2
from PySide2 import QtCore
from PySide2.QtCore import QModelIndex
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QMainWindow, QPushButton, QTableView, QCommandLinkButton, QLineEdit, QComboBox, \
    QMessageBox

from org.cu.api.ReviewerService import ReviewerService
from org.cu.common.ConvertCommon import ReviewerConvert
from org.cu.common.MessageCommon import showMessage, showMessageSDC
from org.cu.common.ToolsCommon import isNoneOrEmpty, getCurrentDate
from org.cu.dao.JobApplyDao import JobApplyDao
from org.cu.dao.JobReviewDao import JobReviewDao
from org.cu.entity.Apply import Apply
from org.cu.entity.Reviewer import Reviewer


'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Handle review job implements the parent abstract class ReviewerService
'''
class ReviewerServiceImpl(ReviewerService):

    # init attributes associate the main window (QMainWindow), JobApplyDao, and JobReviewDao
    def __init__(self, window: QMainWindow):
        self._jobApplyDao = JobApplyDao()
        self._jobReviewDao = JobReviewDao()
        self._window = window
        self._tableViewReviewJobs = None
        self._tableViewReviewJobsModel = None
        self._window.findChild(QPushButton, "pushButtonReviewSave").clicked.connect(self.submitReview)
        self._window.findChild(QCommandLinkButton, "commandLinkButtonGo").clicked.connect(self.__query)
        self._reviewer = Reviewer()
        self._currentSelectedApplyId = None

    # init the job review ui page
    def load(self):
        self._tableViewReviewJobs = self._window.findChild(QTableView, "tableViewReviewJobs")
        self._tableViewReviewJobs.clicked.connect(self.__select)
        self._tableViewReviewJobsModel = QStandardItemModel(0, 9)
        self.__query()

    # submit review job
    @QtCore.Slot()
    def submitReview(self):
        self._reviewer = ReviewerConvert.convert(self._window)
        self._reviewer.apply = Apply(self._currentSelectedApplyId)
        # check submit
        checkResult = self.checkReview()
        if not checkResult[0]:
            showMessage(_type=QMessageBox.Abort, _title="Fill illegally", _content=checkResult[1])
            return
        # show operation result
        if showMessageSDC() != QMessageBox.Save:
            return
        # save the data into database
        self.saveReview()
        # refresh
        self.__query()

    # detect whether illegal
    def checkReview(self) -> Tuple[bool, str]:
        # check fill the form of job
        if self._reviewer is None or isNoneOrEmpty(self._reviewer.reviewerId) or \
                isNoneOrEmpty(self._reviewer.outcome) or isNoneOrEmpty(self._reviewer.hrOfficer):
            return False, "Missing review key field, try again!"
        if self._reviewer.apply is None or isNoneOrEmpty(self._reviewer.apply.applyId):
            return False, "Please choose one apply record!"
        return True, "Ok"

    # save data into database
    def saveReview(self):
        self._jobReviewDao.updateOrInsert(self._reviewer)

    # query the record of apply of job
    def __query(self):
        # get query keys
        queryOfficerName = self._window.findChild(QLineEdit, "lineEditQueryOfficerName").text()
        queryOutcome = self._window.findChild(QComboBox, "comboBoxQueryOutcome").currentText()
        # clear all data
        self._tableViewReviewJobsModel.clear()
        self._currentSelectedApplyId = None
        # set table view header
        self._tableViewReviewJobsModel.setHorizontalHeaderLabels(
            ['ID', 'Name', 'Position', 'Expected Salary', 'Availability Month', 'Apply Date', 'HR-Officer', 'Outcome',
             'Review Date'])
        # get apply records from data
        records = self._jobApplyDao.query(Reviewer(queryOfficerName, queryOutcome))
        if isNoneOrEmpty(records):
            self._tableViewReviewJobs.setModel(self._tableViewReviewJobsModel)
            return
        # bind the data in table view
        for record in records:
            self._tableViewReviewJobsModel.appendRow(
                [QStandardItem(str(record[0])), QStandardItem(str(record[1])), QStandardItem(record[2]),
                 QStandardItem(str(record[3])), QStandardItem(str(record[4])),
                 QStandardItem(str(record[5])), QStandardItem(record[6]),
                 QStandardItem(str(record[7])), QStandardItem(str(record[8]))])
        self._tableViewReviewJobs.setModel(self._tableViewReviewJobsModel)

    # get which one be selected it for reviewing
    def __select(self, index: QModelIndex):
        applyDate = self._tableViewReviewJobsModel.item(index.row(), 5).text()
        lineEditReviewReceivedDate = self._window.findChild(QLineEdit, "lineEditReviewReceivedDate")
        lineEditReviewReceivedDate.setText(applyDate)
        lineEditReviewDate = self._window.findChild(QLineEdit, "lineEditReviewDate")
        lineEditReviewDate.setText(getCurrentDate(_format="%Y-%m-%d %H:%M:%S"))
        self._currentSelectedApplyId = self._tableViewReviewJobsModel.item(index.row(), 0).text()


