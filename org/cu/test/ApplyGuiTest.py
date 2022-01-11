import os
import sys

from PySide2 import QtCore, QtWidgets, QtUiTools
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit


class Window(QtCore.QObject):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = None
        self.submitBut = None
        self.clearBut = None
        self.valueInput1 = None
        self.valueInput2 = None
        self.init_ui()
        self.ui.show()

    def init_ui(self):
        file = QtCore.QFile("resources/gui/apply.ui")
        if not file.open(QtCore.QFile.ReadOnly):
            sys.exit(-1)
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(file)
        self.submitBut = self.ui.findChild(QPushButton, "submitBut")
        self.submitBut.clicked.connect(self.submit)
        self.clearBut = self.ui.findChild(QPushButton, "clearBut")
        self.clearBut.clicked.connect(self.clear)
        self.valueInput1 = self.ui.findChild(QLineEdit, "valueInput1")
        self.valueInput2 = self.ui.findChild(QLineEdit, "valueInput2")

    @QtCore.Slot()
    def submit(self):
        print("submit input")
        print(self.valueInput1.text())
        print(self.valueInput2.text())

    @QtCore.Slot()
    def clear(self):
        print("clear input")
        self.valueInput1.clear()
        self.valueInput1.repaint()
        self.valueInput2.clear()
        self.valueInput2.repaint()


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
