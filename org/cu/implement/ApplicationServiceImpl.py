from typing import Tuple

from PySide2 import QtCore
from PySide2.QtGui import QStandardItemModel
from PySide2.QtWidgets import QMainWindow, QLineEdit, QTableView, QPushButton, QCommandLinkButton, QMessageBox

from org.cu.api.ApplicationService import ApplicationService
from org.cu.common.ConvertCommon import ApplyConvert, PersonalDetailConvert, QualificationsConvert, ReferencesConvert, \
    WorkingExperienceConvert
from org.cu.common.MessageCommon import showMessageSDC, showMessage
from org.cu.common.ToolsCommon import getCurrentDate, isNoneOrEmpty, isEmail
from org.cu.dao.JobApplyDao import JobApplyDao
from org.cu.entity.Apply import Apply

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Handle apply job implements the parent abstract class ApplicationService
'''
class ApplicationServiceImpl(ApplicationService):

    # init attributes associate the main window (QMainWindow), JobApplyDao
    def __init__(self, window: QMainWindow):
        self._apply = Apply()
        self._workingExperiences = dict()
        self._window = window
        self._lineEditAppliedDate = None
        self._tableViewQualification = None
        self._window.findChild(QPushButton, "pushButtonApplySave").clicked.connect(self.submitApply)
        self._window.findChild(QCommandLinkButton, "commandLinkButtonWSaveMore").clicked.connect(
            self.__workingExperienceSaveAndMore)
        self._jobApplyDao = JobApplyDao()

    # init the apply ui page
    def load(self):
        self._lineEditAppliedDate = self._window.findChild(QLineEdit, "lineEditAppliedDate")
        self._lineEditAppliedDate.setText(getCurrentDate())
        self._lineEditAppliedDate.setReadOnly(True)
        self._tableViewQualification = self._window.findChild(QTableView, "tableViewQualification")
        model = QStandardItemModel(5, 5)
        model.setHorizontalHeaderLabels(['Qualification', 'Institution/University', 'Major', 'Grade', 'Year Graduated'])
        self._tableViewQualification.setModel(model)

    # process submit
    @QtCore.Slot()
    def submitApply(self):
        print("submit job apply")
        # set apply
        self.__setApply()
        # check submit
        checkResult = self.checkApply()
        if not checkResult[0]:
            showMessage(_type=QMessageBox.Abort, _title="Fill illegally", _content=checkResult[1])
            return
        # show operation result
        if showMessageSDC() != QMessageBox.Save:
            return
        # save data
        self.saveApply()
        self.__clear()

    # check whether illegal
    def checkApply(self) -> Tuple[bool, str]:
        print("check submit")
        # check fill the form of job
        if self._apply is None or isNoneOrEmpty(self._apply.applyId) or \
                isNoneOrEmpty(self._apply.position) or self._apply.expectedSalary == 0:
            return False, "Missing apply part, try again!"
        personal = self._apply.personalDetail
        if personal is None or isNoneOrEmpty(personal.name) or isNoneOrEmpty(personal.references) \
                or isNoneOrEmpty(personal.qualifications) or \
                isNoneOrEmpty(personal.gender) or isNoneOrEmpty(personal.dateOfBirth):
            return False, "Missing personal or qualification or references parts, try again!"
        if not isEmail(personal.email):
            return False, "Personal Email format is wrong!, try again!"
        reference = self._apply.personalDetail.references[0]
        if reference is None or isNoneOrEmpty(reference.name):
            return False, "Missing references part, try again!"
        # check whether occupation in database
        if self._jobApplyDao.isDuplicate(self._apply):
            return False, "Sorry,Only allow one personal one position for one day! "
        return True, "ok"

    # save data
    def saveApply(self):
        print(self._apply.toJSON())
        self._jobApplyDao.updateOrInsert(self._apply)

    # query data . not use it.
    def queryApply(self):
        pass

    # handle add more personal working experiences
    @QtCore.Slot()
    def __workingExperienceSaveAndMore(self):
        print("save and add more working experiences")
        # show operation result
        if showMessageSDC() != QMessageBox.Save:
            return
        # convert the data from ui
        experience = WorkingExperienceConvert.convert(self._window)
        if experience is None or len(experience.company) == 0:
            return
        # choose save
        self._workingExperiences[experience.company] = experience

    # clear working experiences after submit
    def __clear(self):
        self._workingExperiences.clear()

    # sort out all of data relate apply
    def __setApply(self):
        self._apply = ApplyConvert.convert(self._window)
        personal = PersonalDetailConvert.convert(self._window)
        qualifications = QualificationsConvert.convert(self._window)
        references = ReferencesConvert.convert(self._window)
        personal.qualifications = qualifications
        personal.references = references
        personal.workingExperiences = [i for i in self._workingExperiences.values()]
        self._apply.personalDetail = personal
