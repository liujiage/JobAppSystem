import sys
from PySide2.QtWidgets import QMessageBox, QApplication

'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Common show confirm window
'''
def showMessageSDC(_save=None, _discard=None, _cancel=None,
                   _title="The document has been modified.",
                   _content="Do you want to save your changes?") -> QMessageBox:
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    msgBox = QMessageBox()
    msgBox.setText(_title)
    msgBox.setInformativeText(_content)
    msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
    msgBox.setDefaultButton(QMessageBox.Save)
    ret = msgBox.exec_()
    if ret == QMessageBox.Save:
        print("Save was clicked")
        if _save is not None:
            _save()
    elif ret == QMessageBox.Discard:
        print("Don't save was clicked")
        if _discard is not None:
            _discard()
    elif ret == QMessageBox.Cancel:
        print("cancel was clicked")
        if _cancel is not None:
            _cancel()
    else:
        print("should never be reached")
    # sys.exit()
    msgBox.close()
    return ret


'''
   @Author Liu JiaGe
   @School Coventry University & PSB
   @Date 01/03/21
   @Common show normal window
'''
def showMessage(_type=QMessageBox.Ok, _title="System Info", _content="Operation successful!") -> QMessageBox:
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    msgBox = QMessageBox()
    msgBox.setText(_title)
    msgBox.setInformativeText(_content)
    msgBox.setStandardButtons(_type)
    msgBox.setDefaultButton(_type)
    ret = msgBox.exec_()
    msgBox.close()
    return ret
