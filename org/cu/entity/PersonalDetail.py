from typing import List

from org.cu.common.Serializable import Serializable
from org.cu.entity.Qualification import Qualification
from org.cu.entity.Reference import Reference
from org.cu.entity.WorkingExperience import WorkingExperience

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Entity Personal
'''
class PersonalDetail(Serializable):
    def __init__(self):
        self._personalId = None
        self._name = None
        self._address = None
        self._passport = None
        self._postcode = None
        self._email = None
        self._phoneNo = None
        self._mobileNo = None
        self._dateOfBirth = None
        self._gender = 1  # 1 faces-male 2 faces-female
        self._qualifications = None  # reference list[qualification]
        self._workingExperiences = None  # reference list[workingExperience]
        self._references = None  # reference list[Reference]

    @property
    def qualifications(self) -> List[Qualification]:
        return self._qualifications

    @qualifications.setter
    def qualifications(self, value: List[Qualification]):
        self._qualifications = value

    @property
    def workingExperiences(self) -> List[WorkingExperience]:
        return self._workingExperiences

    @workingExperiences.setter
    def workingExperiences(self, value):
        self._workingExperiences = value

    @property
    def references(self) -> List[Reference]:
        return self._references

    @references.setter
    def references(self, value: List[Reference]):
        self._references = value

    @property
    def personalId(self):
        return self._personalId

    @personalId.setter
    def personalId(self, value):
        self._personalId = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def passport(self):
        return self._passport

    @passport.setter
    def passport(self, value):
        self._passport = value

    @property
    def postcode(self):
        return self._passport

    @postcode.setter
    def postcode(self, value):
        self._postcode = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phoneNo(self):
        return self._phoneNo

    @phoneNo.setter
    def phoneNo(self, value):
        self._phoneNo = value

    @property
    def mobileNo(self):
        return self._mobileNo

    @mobileNo.setter
    def mobileNo(self, value):
        self._mobileNo = value

    @property
    def dateOfBirth(self):
        return self._dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, value):
        self._dateOfBirth = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
