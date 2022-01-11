from org.cu.common.Serializable import Serializable

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Entity Working experience
'''
class WorkingExperience(Serializable):
    def __init__(self):
        self._experienceId = None
        self._company = None
        self._industry = None
        self._position = None
        self._level = None
        self._monthlySalary = 0.0
        self._dateFrom = None
        self._dateEnd = None

    @property
    def experienceId(self):
        return self._experienceId

    @experienceId.setter
    def experienceId(self, value):
        self._experienceId = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    @property
    def industry(self):
        return self._industry

    @industry.setter
    def industry(self, value):
        self._industry = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def monthlySalary(self):
        return self._monthlySalary

    @monthlySalary.setter
    def monthlySalary(self, value):
        self._monthlySalary = value

    @property
    def dateFrom(self):
        return self._dateFrom

    @dateFrom.setter
    def dateFrom(self, value):
        self._dateFrom = value

    @property
    def dateEnd(self):
        return self._dateEnd

    @dateEnd.setter
    def dateEnd(self, value):
        self._dateEnd = value