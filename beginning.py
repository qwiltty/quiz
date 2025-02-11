from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from main import *
from base import *


class Win_Main(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()
        self.connects()
        self.set_appear()
        self.show()

    def InitUI(self):
        self.line_main = QVBoxLayout()
        self.line_h1 = QHBoxLayout()
        self.line_h2 = QHBoxLayout()

        self.button = QPushButton('Викторина')
        self.button.setFont(QFont("Times", 20, QFont.Bold))
        self.button.setStyleSheet("color: rgb(101, 219, 78)")
        self.button2 = QPushButton('Создание викторины')
        self.button2.setFont(QFont("Times", 20, QFont.Bold))
        self.button2.setStyleSheet("color: rgb(214, 31, 31)")
        
        self.line_h1.addWidget(self.button, alignment=Qt.AlignCenter)
        self.line_h2.addWidget(self.button2, alignment=Qt.AlignCenter)

        self.line_main.addLayout(self.line_h1)
        self.line_main.addLayout(self.line_h2)
        self.setLayout(self.line_main)

    def next_click(self):
        self.hide()
        self.jw = Win3()
    
    def next_click2(self):
        self.hide()
        self.gw = Win1()
    

    def connects(self):
        self.button.clicked.connect(self.next_click)
        self.button2.clicked.connect(self.next_click2)

    def set_appear(self):
        self.setWindowTitle('Добро пожаловать!')
        self.resize(1400, 900)

app = QApplication([])
main_window = Win_Main()
app.exec_()