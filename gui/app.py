import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui, QtCharts
import finnhub

from chart import ChartWidget



class Color(QtWidgets.QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(color))
        self.setPalette(palette)

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.menu_bar = QtWidgets.QMenuBar()
        self.menu_bar.addMenu("File")


        self.chart = ChartWidget()
        self.input = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton("Search Ticker")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QGridLayout()

        self.layout.setSpacing(10)

        #self.layout.addWidget(self.chart, 0, 0, 4, 5)
        #self.layout.addWidget(self.input, 5, 4, 1, 1)
        #self.layout.addWidget(self.button, 5, 5, 1, 1)
        #self.layout.addWidget(self.menu_bar)
        
        self.layout.addWidget(Color('red'), 0, 0, 1, 10)
        self.layout.addWidget(Color('green'), 0, 0, 8, 10)
        self.layout.addWidget(Color('blue'), 1, 1, 1, 1)
        self.layout.addWidget(Color('purple'), 9, 9, 1, 1)
        self.layout.addWidget(Color('red'), 9, 0, 1, 10)
        

        self.setLayout(self.layout)


        self.button.clicked.connect(self.get_ticker)



    def get_ticker(self):
        ticker = self.input.text()
        self.input.clear()
        try:
            pass

        except:
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())