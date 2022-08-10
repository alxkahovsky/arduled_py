import sys
from PyQt5 import QtWidgets
import design
import os
import json


class MyApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sliders = (self.RedSlider, self.GreenSlider, self. BlueSlider)

        for slider in self.sliders:
            slider.setMinimum(0)
            slider.setMaximum(255)

        self.RedButton.clicked.connect(self.red_button)
        self.RedSlider.sliderMoved.connect(self.red_slider)

        self.GreenButton.clicked.connect(self.green_button)
        self.GreenSlider.sliderMoved.connect(self.green_slider)

        self.BlueButton.clicked.connect(self.blue_button)
        self.BlueSlider.sliderMoved.connect(self.blue_slider)

        self.pushButton.clicked.connect(self.submit)
        # self.pushButton.
        self.actionSave_config.triggered.connect(self.save)

    def red_button(self):
        self.LcdRed.display(255)
        self.RedSlider.setValue(255)

    def red_slider(self):
        self.LcdRed.display(self.RedSlider.sliderPosition())

    def green_button(self):
        self.LcdGreen.display(255)
        self.GreenSlider.setValue(255)

    def green_slider(self):
        self.LcdGreen.display(self.GreenSlider.sliderPosition())

    def blue_button(self):
        self.LcdBlue.display(255)
        self.BlueSlider.setValue(255)

    def blue_slider(self):
        self.LcdBlue.display(self.BlueSlider.sliderPosition())

    def submit(self):
        r,g,b = self.LcdRed.value(), self.LcdGreen.value(), self.LcdBlue.value()
        print('RGB', (int(r), int(g), int(b)))

    def save(self):
        r, g, b = self.LcdRed.value(), self.LcdGreen.value(), self.LcdBlue.value()
        data = {'Name': 'New_name', 'Red':r, 'Green':g, 'Blue':b, 'Static': True, 'Strobe':False, 'Pulse':False}
        with open('configs/config.json', 'w') as f:
            json.dump(data, f, indent=4)
        print('ass')




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    # os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = 'PyQt5\Qt5\plugins\platforms' добавляем переменную среды когда собираем exe
    main()