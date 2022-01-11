from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QPushButton

from org.cu.implement.ApplicationServiceImpl import ApplicationServiceImpl
from org.cu.implement.ManagerPositionImpl import ManagerPositionImpl
from org.cu.implement.ReviewerServiceImpl import ReviewerServiceImpl

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Handle all pages functions through only one method Load() to load all page
   @Integrated ManagerPositionImpl,ApplicationServiceImpl and ReviewerServiceImpl 
'''
class JobApplication(object):

    # init attributes associate the main window (QMainWindow), ManagerPositionImpl,ApplicationServiceImpl and ReviewerServiceImpl
    def __init__(self, window: QMainWindow):
        self._window = window
        self._managerPosition = ManagerPositionImpl(self._window)
        self._applicationServiceImpl = ApplicationServiceImpl(self._window)
        self._reviewerServiceImpl = ReviewerServiceImpl(self._window)

    # load all of pages
    def load(self):
        self._managerPosition.load()
        self._applicationServiceImpl.load()
        self._reviewerServiceImpl.load()


# job = JobApplication(None)
