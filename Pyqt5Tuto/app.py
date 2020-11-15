from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Chat Application")        
        self.initUI()
        
    def initUI(self):
        
    
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Click me")
        self.btn.clicked.connect(self.clicked)
    
    def update(self):
        self.label.adjustSize()
    
    def clicked(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Here is my label")
        self.label.move(50, 50)
        #self.label.setText("You pressed the button")
        self.update()
        
def window():
    app = QApplication(sys.argv)
    win = MyWindow()   
    win.show()
    sys.exit(app.exec_())
    
window()
