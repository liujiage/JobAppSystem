from org.cu.dao.DaoService import DaoService


'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Manager job position inherit DaoService
'''
class JobPositionDao(DaoService):

    # query job position
    def query(self, value=None) -> list:
        return self.fetch("select id,title from job_position")

    # delete job position
    def delete(self, value=None) -> int:
        if value is None:
            return self.execute("delete from job_position")
        else:
            return self.execute("delete from job_position where id = %d" % (value,))

    # create or modify job position
    def updateOrInsert(self, value) -> int:
        return self.execute("insert into job_position(title) values('%s')" % (value,))

# job = JobPositionDao()
# print(job.query())
