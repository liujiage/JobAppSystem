from abc import ABCMeta, abstractmethod

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/02/21
   @Handle apply Job, parent class
'''
class ApplicationService(metaclass=ABCMeta):

    # init page and resources
    @abstractmethod
    def load(self):
        pass

    # process apply
    @abstractmethod
    def submitApply(self):
        pass

    # check whether illegal
    @abstractmethod
    def checkApply(self):
        pass

    # save the data into database
    @abstractmethod
    def saveApply(self):
        pass

    # query data from database
    @abstractmethod
    def queryApply(self):
        pass
