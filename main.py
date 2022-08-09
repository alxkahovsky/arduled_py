import sys
from PyQt5 import QtWidgets
import design
import os


class MyApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.RedButton.clicked.connect(self.red)
        self.GreenButton.clicked.connect(self.green)
        self.BlueButton.clicked.connect(self.blue)

    def red(self):
        self.lcdColor.display('red')

    def green(self):
        self.lcdColor.display('green')

    def blue(self):
        self.lcdColor.display('blue')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    # os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = 'PyQt5\Qt5\plugins\platforms' добавляем переменную среды когда собираем exe
    main()