from org.cu.common.Serializable import Serializable
from org.cu.entity.PersonalDetail import PersonalDetail

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Entity Apply
'''
class Apply(Serializable):
    def __init__(self, applyId=None):
        self._applyId = applyId
        self._position = None
        self._createDate = None
        self._expectedSalary = 0
        self._availabilityMonths = 0
        self._personalDetail = None  # reference PersonalDetail

    @property
    def personalDetail(self) -> PersonalDetail:
        return self._personalDetail

    @personalDetail.setter
    def personalDetail(self, value: PersonalDetail):
        self._personalDetail = value

    @property
    def applyId(self):
        return self._applyId

    @applyId.setter
    def applyId(self, value):
        self._applyId = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def createDate(self):
        return self._createDate

    @createDate.setter
    def createDate(self, value):
        self._createDate = value

    @property
    def expectedSalary(self):
        return self._expectedSalary

    @expectedSalary.setter
    def expectedSalary(self, value):
        self._expectedSalary = value

    @property
    def availabilityMonths(self):
        return self._availabilityMonths

    @availabilityMonths.setter
    def availabilityMonths(self, value):
        self._availabilityMonths = value

