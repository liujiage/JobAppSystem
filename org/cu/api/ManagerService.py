from abc import ABCMeta, abstractmethod

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/02/21
   @Manager Job positions, parent class
'''
class ManagerService(metaclass=ABCMeta):

    # init the page and resources
    @abstractmethod
    def load(self):
        pass

    # modify and add the job positions
    @abstractmethod
    def modify(self):
        pass
