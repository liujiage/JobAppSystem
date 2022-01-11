from org.cu.common.Serializable import Serializable

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Entity Qualification
'''
class Qualification(Serializable):
    def __init__(self):
        self._qualificationId = None
        self._qualification = None
        self._institution = None
        self._major = None
        self._grade = None
        self._graduatedYear = None

    @property
    def qualificationId(self):
        return self._qualificationId

    @qualificationId.setter
    def qualificationId(self, value):
        self._qualificationId = value

    @property
    def qualification(self):
        return self._qualification

    @qualification.setter
    def qualification(self, value):
        self._qualification = value

    @property
    def institution(self):
        return self._institution

    @institution.setter
    def institution(self, value):
        self._institution = value

    @property
    def major(self):
        return self.major

    @major.setter
    def major(self, value):
        self._major = value

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    @property
    def graduatedYear(self):
        return self._graduatedYear

    @graduatedYear.setter
    def graduatedYear(self, value):
        self._graduatedYear = value
