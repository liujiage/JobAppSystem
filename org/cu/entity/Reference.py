from org.cu.common.Serializable import Serializable

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Entity Reference
'''
class Reference(Serializable):
    def __init__(self):
        self._referenceId = None
        self._name = None
        self._occupation = None
        self._company = None
        self._contactNo = None
        self._email = None
        self._relationship = None

    @property
    def referenceId(self):
        return self._referenceId

    @referenceId.setter
    def referenceId(self, value):
        self._referenceId = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, value):
        self._occupation = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    @property
    def contactNo(self):
        return self._contactNo

    @contactNo.setter
    def contactNo(self, value):
        self._contactNo = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def relationship(self):
        return self._relationship

    @relationship.setter
    def relationship(self, value):
        self._relationship = value
