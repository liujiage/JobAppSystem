from abc import ABCMeta, abstractmethod

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/02/21
   @Handle HR or Office review the record of apply job, parent class
'''
class ReviewerService(metaclass=ABCMeta):

    # init page and resources
    @abstractmethod
    def load(self):
        pass

    # process review
    @abstractmethod
    def submitReview(self):
        pass

    # check whether illegal
    @abstractmethod
    def checkReview(self):
        pass

    # save the data into database
    @abstractmethod
    def saveReview(self):
        pass
