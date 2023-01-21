from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Ui(QtWidgets.QWidget):
    one = ""
    two = ""
    modifier = ""
    history = []
    modifiers = ["%","/","*","+","-","=","C","AC","+/-"]

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('calculator.ui', self)

        for button in self.findChildren(QtWidgets.QPushButton):
            if(button.text() in self.modifiers):
                button.clicked.connect(self.modifier_click)
            else:
                button.clicked.connect(self.numerical_click)
        self.show()

    def modifier_click(self):
        sender = self.sender()
        if(sender.text() == "C"):
            self.clear()
            return       
        if(sender.text() == "AC"):
            self.clear()
            self.history.clear()
            return
        if(self.one == ""):
            return
        if(sender.text() == "+/-"):
            print("invert")
            return

        if(sender.text() == "=" and self.one and self.two and self.modifier != ""):
            expression = self.one + self.modifier + self.two
            evaluation = eval(expression)
            self.results.setText(str(evaluation))
            self.history.append(expression + "=" + str(evaluation))
            self.one = str(evaluation)
            self.two = ""
            print(self.history)
            return



        self.modifier = sender.text()
        self.results.setText("")

    def numerical_click(self):
        sender = self.sender()

        if(self.modifier == "" ):
            self.one += sender.text()
            self.results.insert(sender.text())
        elif(self.one != ""):
            self.two += sender.text()
            self.results.insert(sender.text())
    
    def clear(self):
            self.results.setText("")
            self.one = "" 
            self.two = ""
            self.modifier = ""

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()