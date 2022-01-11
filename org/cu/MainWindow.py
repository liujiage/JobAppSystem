import os
import sys
from PySide2 import QtCore, QtWidgets, QtUiTools
from PySide2.QtCore import Qt
from org.cu.implement.JobApplication import JobApplication

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/02/21
   @Main Window
'''
class Window(QtCore.QObject):
    def __init__(self):
        super(Window, self).__init__()
        # add window design from job.ui by QTDesigner
        self._filename = os.path.dirname(os.path.dirname(__file__)) + '/cu/resources/gui/job.ui'
        file = QtCore.QFile(self._filename)
        if not file.open(QtCore.QFile.ReadOnly):
            sys.exit(-1)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(file)
        self._jobApplication = JobApplication(self.ui)
        self.ui.setWindowFlag(Qt.WindowType.Dialog)
        self.ui.setFixedSize(self.ui.width(), self.ui.height())
        # load sub-pages, apply page, review page, and manage page
        self._jobApplication.load()
        self.ui.show()


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())