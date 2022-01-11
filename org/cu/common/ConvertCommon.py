import json
from abc import ABCMeta, abstractmethod
from typing import List

from PySide2.QtWidgets import QMainWindow, QComboBox, QLineEdit, QDoubleSpinBox, QSpinBox, QRadioButton, QDateEdit, \
    QTableView, QButtonGroup

from org.cu.common.ToolsCommon import getId, isNoneOrEmpty
from org.cu.entity.PersonalDetail import PersonalDetail
from org.cu.entity.Apply import Apply
from org.cu.entity.Qualification import Qualification
from org.cu.entity.Reference import Reference
from org.cu.entity.Reviewer import Reviewer
from org.cu.entity.WorkingExperience import WorkingExperience

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Convert the data to entity object from UI, parent class
'''
class Convert(metaclass=ABCMeta):

    # Handle method
    @abstractmethod
    def convert(self):
        pass


'''  
     Convert apply
     comboBoxPosition->position
     lineEditAppliedDate->createDate
     doubleSpinBoxExpSalary->expectedSalary
     spinBoxAvailabilityMonths->availabilityMonths
'''
class ApplyConvert(Convert):
    @staticmethod
    def convert(window: QMainWindow) -> Apply:
        apply = Apply()
        apply.applyId = getId("apply-")
        apply.position = window.findChild(QComboBox, "comboBoxPosition").currentText()
        apply.createDate = window.findChild(QLineEdit, "lineEditAppliedDate").text()
        apply.expectedSalary = window.findChild(QDoubleSpinBox, "doubleSpinBoxExpSalary").value()
        apply.availabilityMonths = window.findChild(QSpinBox, "spinBoxAvailabilityMonths").value()
        # print(apply.toJSON())
        return apply


'''
     Convert personal
     lineEditPName->name
     lineEditPPassport->passport
     lineEditPAddress->address
     lineEditPEmail->email
     lineEditPPhone->phoneNo
     lineEditPMobile->mobileNo
     dateEditPBirth->dateOfBirth
     radioButtonPFemale->gender
     radioButtonPMale->gender
     lineEditPostcode->postcode
'''
class PersonalDetailConvert(Convert):
    @staticmethod
    def convert(window: QMainWindow) -> PersonalDetail:
        personal = PersonalDetail()
        personal.personalId = getId("personal-")
        personal.name = window.findChild(QLineEdit, "lineEditPName").text()
        personal.passport = window.findChild(QLineEdit, "lineEditPPassport").text()
        personal.address = window.findChild(QLineEdit, "lineEditPAddress").text()
        personal.email = window.findChild(QLineEdit, "lineEditPEmail").text()
        personal.phoneNo = window.findChild(QLineEdit, "lineEditPPhone").text()
        personal.mobileNo = window.findChild(QLineEdit, "lineEditPMobile").text()
        personal.dateOfBirth = window.findChild(QDateEdit, "dateEditPBirth").text()
        isFemale = window.findChild(QRadioButton, "radioButtonPFemale").isChecked()
        # isMale = window.findChild(QRadioButton, "radioButtonPMale").isChecked()
        personal.gender = (isFemale and "faces-female") or "faces-male"
        personal.postcode = window.findChild(QLineEdit, "lineEditPostcode").text()
        # print(personal.toJSON())
        return personal


''' 
   Convert qualification
   c1->qualification
   c2->institution
   c3->major
   c4->grade
   c5->graduatedYear
'''
class QualificationsConvert(Convert):
    @staticmethod
    def convert(window: QMainWindow) -> List[Qualification]:
        tableData = window.findChild(QTableView, "tableViewQualification").model()
        qualifications = list()
        n = tableData.rowCount()
        for i in range(n):
            rows = list()
            isCheck = True
            for j in range(5):
                node = tableData.item(i, j)
                if node is None or len(node.text()) == 0:
                    isCheck = False
                    break
                rows.insert(j, node.text())
            if not isCheck:
                continue
            qualification = Qualification()
            qualification.qualificationId = getId("qualification-")
            qualification.qualification = rows[0]
            qualification.institution = rows[1]
            qualification.major = rows[2]
            qualification.grade = rows[3]
            qualification.graduatedYear = rows[4]
            qualifications.append(qualification)
        return qualifications


'''
    Convert reference
    lineEditRName->name
    lineEditROccupation->occupation
    lineEditRCompany->company
    lineEditRContact->contactNo
    lineEditREmail->email
    comboBoxRRelationship->relationship
'''
class ReferencesConvert(Convert):
    @staticmethod
    def convert(window: QMainWindow) -> List[Reference]:
        references = list()
        reference1 = Reference()
        reference1.referenceId = getId("reference-")
        reference1.name = window.findChild(QLineEdit, "lineEditRName").text()
        if isNoneOrEmpty(reference1.name):
            return references
        reference1.occupation = window.findChild(QLineEdit, "lineEditROccupation").text()
        reference1.company = window.findChild(QLineEdit, "lineEditRCompany").text()
        reference1.contactNo = window.findChild(QLineEdit, "lineEditRContact").text()
        reference1.email = window.findChild(QLineEdit, "lineEditREmail").text()
        reference1.relationship = window.findChild(QComboBox, "comboBoxRRelationship").currentText()
        references.append(reference1)
        # print(reference1.toJSON())
        reference2 = Reference()
        reference2.referenceId = getId("reference-")
        reference2.name = window.findChild(QLineEdit, "lineEditRName2").text()
        if isNoneOrEmpty(reference2.name):
            return references
        reference2.occupation = window.findChild(QLineEdit, "lineEditROccupation2").text()
        reference2.company = window.findChild(QLineEdit, "lineEditRCompany2").text()
        reference2.contactNo = window.findChild(QLineEdit, "lineEditRContact2").text()
        reference2.email = window.findChild(QLineEdit, "lineEditREmail2").text()
        reference2.relationship = window.findChild(QComboBox, "comboBoxRRelationship2").currentText()
        references.append(reference2)
        # print(reference2.toJSON())
        return references


'''
   Convert working experience
   lineEditWCompany->company
   lineEditWIndustry->industry
   lineEditWPosition->position
   dateEditWFrom->dateFrom
   dateEditWEnd->dateEnd
   buttonGroupWLevel->level
   doubleSpinBoxWSalary->monthlySalary
'''
class WorkingExperienceConvert(Convert):
    @staticmethod
    def convert(window: QMainWindow) -> WorkingExperience:
        experience = WorkingExperience()
        experience.experienceId = getId("experience-")
        experience.company = window.findChild(QLineEdit, "lineEditWCompany").text()
        experience.industry = window.findChild(QLineEdit, "lineEditWIndustry").text()
        experience.position = window.findChild(QLineEdit, "lineEditWPosition").text()
        experience.dateFrom = window.findChild(QDateEdit, "dateEditWFrom").text()
        experience.dateEnd = window.findChild(QDateEdit, "dateEditWEnd").text()
        experience.level = window.findChild(QButtonGroup, "buttonGroupWLevel").checkedButton().text()
        experience.monthlySalary = window.findChild(QDoubleSpinBox, "doubleSpinBoxWSalary").value()
        # print(experience.toJSON())
        return experience


'''
   Convert reviewer
   lineEditReviewOfficer->hrOfficer
   buttonGroupReviewOutcome->outcome
   lineEditReviewReason->reason
'''
class ReviewerConvert(Convert):
    @staticmethod
    def convert(window: QMainWindow) -> Reviewer:
        reviewer = Reviewer()
        reviewer.reviewerId = getId("review-")
        reviewer.hrOfficer = window.findChild(QLineEdit, "lineEditReviewOfficer").text()
        reviewer.outcome = window.findChild(QButtonGroup, "buttonGroupReviewOutcome").checkedButton().text()
        reviewer.reason = window.findChild(QLineEdit, "lineEditReviewReason").text()
        reviewer.dateReceived = window.findChild(QLineEdit, "lineEditReviewReceivedDate").text()
        reviewer.reviewDate = window.findChild(QLineEdit, "lineEditReviewDate").text()
        return reviewer
