from org.cu.common.ToolsCommon import isNoneOrEmpty
from org.cu.dao.DaoService import DaoService
from org.cu.entity.Apply import Apply
from org.cu.entity.Reviewer import Reviewer

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Handle apply inherit DaoService
'''
class JobApplyDao(DaoService):

    # query apply job use the condition review officer or outcome
    def query(self, value=Reviewer()) -> list:
        value.hrOfficer = (isNoneOrEmpty(value.hrOfficer) and "-none-") or value.hrOfficer
        return self.fetch("select id,name,position,expected_salary,availability_months,create_time,review_officer,"
                          "review_outcome,review_time from job_apply "
                          "where review_officer like '%%%s%%' or review_outcome like '%%%s%%' "
                          " order by create_time desc" % (value.hrOfficer, value.outcome))

    # delete apply job record. not use it.
    def delete(self, value) -> int:
        pass

    # create or modify apply job
    def updateOrInsert(self, value: Apply) -> int:
        # save data into database
        return self.execute("insert into job_apply(id,name,position,content,expected_salary,availability_months) "
                            "values('%s','%s','%s','%s',%f,%d)" % (
                                value.applyId, value.personalDetail.name, value.position,
                                value.toJSON(), value.expectedSalary, value.availabilityMonths))

    # detect apply job whether duplicate
    def isDuplicate(self, value: Apply) -> bool:
        count = self.fetchOneInt("select count(*) as con from job_apply where name = '%s' and "
                                 "position = '%s' and (date('now') - date(create_time)) <= 0 " % (
                                     value.personalDetail.name,
                                     value.position))
        return count > 0
