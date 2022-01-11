import sys
from PySide2.QtWidgets import QMessageBox, QApplication


def showMessageTest(_save, _discard, _cancel):
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    msgBox = QMessageBox()
    msgBox.setText("The document has been modified.")
    msgBox.setInformativeText("Do you want to save your changes?")
    msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
    msgBox.setDefaultButton(QMessageBox.Save)
    ret = msgBox.exec_()
    if ret == QMessageBox.Save:
        print("Save was clicked")
        _save()
    elif ret == QMessageBox.Discard:
        print("cancel was discard")
        _discard()
    elif ret == QMessageBox.Cancel:
        print("cancel was clicked")
        _cancel()
    else:
        print("should never be reached")
    msgBox.close()
    sys.exit()
    return ret

def fun1():
    print("call fun1")

def fun2():
    print("call fun2")

def fun3():
    print("call fun3")


v = showMessageTest(fun1, fun2, fun3)
print("test", v)
