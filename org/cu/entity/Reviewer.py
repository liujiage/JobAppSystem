from org.cu.common.Serializable import Serializable
from org.cu.entity.Apply import Apply

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Entity Reviewer
'''
class Reviewer(Serializable):
    def __init__(self, hrOfficer="-none-", outcome="none"):
        self._reviewerId = None
        self._dateReceived = None
        self._hrOfficer = hrOfficer
        self._outcome = outcome
        self._reason = None
        self._reviewDate = None
        self._apply = None

    @property
    def apply(self) -> Apply:
        return self._apply

    @apply.setter
    def apply(self, value: Apply):
        self._apply = value

    @property
    def reviewerId(self):
        return self._reviewerId

    @reviewerId.setter
    def reviewerId(self, value):
        self._reviewerId = value

    @property
    def dateReceived(self):
        return self._dateReceived

    @dateReceived.setter
    def dateReceived(self, value):
        self._dateReceived = value

    @property
    def hrOfficer(self):
        return self._hrOfficer

    @hrOfficer.setter
    def hrOfficer(self, value):
        self._hrOfficer = value

    @property
    def outcome(self):
        return self._outcome

    @outcome.setter
    def outcome(self, value):
        self._outcome = value

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value

    @property
    def reviewDate(self):
        return self._reviewDate

    @reviewDate.setter
    def reviewDate(self, value):
        self._reviewDate = value
