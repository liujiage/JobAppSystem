from org.cu.dao.DaoService import DaoService
from org.cu.entity.Reviewer import Reviewer

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Handle job review inherit DaoService
'''
class JobReviewDao(DaoService):
    # create or modify the record of job of review
    def updateOrInsert(self, value: Reviewer) -> int:
        self.execute("update job_apply set review_id = '%s',review_officer = '%s', "
                     "review_outcome = '%s',review_reason = '%s', review_time = date('now') "
                     "where id = '%s'" % (value.reviewerId, value.hrOfficer, value.outcome, value.reason, value.apply.applyId))

    # query review data. not use it, see @JobPositionDao
    def query(self, value) -> list:
        pass

    # remove review data. not use it.
    def delete(self, value) -> int:
        pass