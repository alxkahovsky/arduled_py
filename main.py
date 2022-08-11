import sys
from PyQt5 import QtWidgets, QtGui
import design
import os
import json


class MyApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sliders = (self.RedSlider, self.GreenSlider, self.BlueSlider)

        self.radioStatic.setChecked(True)
        self.radio_simple = (self.radioStatic, self.radioPulse, self.radioStrobe)
        for slider in self.sliders:
            slider.setMinimum(0)
            slider.setMaximum(255)

        self.TimeSlider.setValue(5)

        self.RedButton.clicked.connect(self.red_button)
        self.RedSlider.sliderMoved.connect(self.red_slider)

        self.GreenButton.clicked.connect(self.green_button)
        self.GreenSlider.sliderMoved.connect(self.green_slider)

        self.BlueButton.clicked.connect(self.blue_button)
        self.BlueSlider.sliderMoved.connect(self.blue_slider)

        self.pushButton.clicked.connect(self.submit_tab1)

        self.actionSave_config.triggered.connect(self.save_config)
        self.actionLoad_config.triggered.connect(self.load_config)

        self.radioStrobe.clicked.connect(self._activate_time_slider)
        self.radioPulse.clicked.connect(self._activate_time_slider)
        self.radioStatic.clicked.connect(self._deactivate_time_slider)

        self.SeqButton1.clicked.connect(self.chose_color)
        self.SeqButton2.clicked.connect(self.chose_color)
        self.SeqButton3.clicked.connect(self.chose_color)
        self.SeqButton4.clicked.connect(self.chose_color)
        self.SeqButton5.clicked.connect(self.chose_color)
        self.SeqButton6.clicked.connect(self.chose_color)
        self.SeqButton7.clicked.connect(self.chose_color)

        self.pushButton_2.clicked.connect(self.submit_tab2)

    def _activate_time_slider(self):
        self.TimeSlider.setDisabled(False)

    def _deactivate_time_slider(self):
        self.TimeSlider.setDisabled(True)

    def _set_values(self, values: dict):
        self.LcdRed.display(values['Red'])
        self.RedSlider.setValue(values['Red'])

        self.LcdGreen.display(values['Green'])
        self.GreenSlider.setValue(values['Green'])

        self.LcdBlue.display(values['Blue'])
        self.BlueSlider.setValue(values['Blue'])

        self.radioStatic.setChecked(values['Static'])
        self.radioPulse.setChecked(values['Pulse'])
        self.radioStrobe.setChecked(values['Strobe'])
        if values['Pulse'] or radioStrobe.setChecked(values['Strobe']):
            self._activate_time_slider()
        self.TimeSlider.setValue(values['Time step'])

        self.ConfigName.setText(values['Config name'])

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

    def submit_tab1(self):
        r, g, b = self.LcdRed.value(), self.LcdGreen.value(), self.LcdBlue.value()
        try:
            ba = bytearray((int(r), int(g), int(b), (1 if self.radioStatic.isChecked() else 0),
              (1 if self.radioPulse.isChecked() else 0),
              (1 if self.radioStrobe.isChecked() else 0),
              int(self.TimeSlider.value())))
            print(ba)
            for b in ba:
                print(b)
        except Exception as e:
            print(e)

    def submit_tab2(self):
        elems = (self.Pre1, self.Pre2, self.Pre3, self.Pre4, self.Pre5, self.Pre6, self.Pre7)
        color_seq = []
        for el in elems:
            try:
                color = el.palette().color(QtGui.QPalette.Window)
                color_tuple = color.getRgb()[:3]
                color_seq.append(color_tuple)
            except Exception as e:
                print(e)
        color_seq = tuple(color_seq)
        print(color_seq)

    def save_config(self):
        config_data = {}
        try:
            for radio_button in self.radio_simple:
                if radio_button.isChecked():
                    config_data[radio_button.text()] = True
                else:
                    config_data[radio_button.text()] = False
        except Exception as e:
            print(e)
        config_data['Red'], config_data['Green'], config_data['Blue'] = int(self.LcdRed.value()), \
                                                                        int(self.LcdGreen.value()), \
                                                                        int(self.LcdBlue.value())
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Save config', 'New config')
        config_data['Config name'] = fname[0].split('/')[-1]
        config_data['Time step'] = int(self.TimeSlider.value())

        try:
            with open(fname[0] + '.json', 'w') as f:
                json.dump(config_data, f, indent=4)
        except Exception as e:
            print(e)

    def load_config(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Load config', '')
        with open(fname[0], 'r') as f:
            config_data = json.load(f)
            print(config_data)
            self._set_values(config_data)

    def chose_color(self):
        obj_name = self.sender().objectName()
        obj_id = obj_name[-1]
        c = self.findChild(QtWidgets.QGraphicsView, 'Pre'+obj_id)
        print(c.objectName())
        c.setStyleSheet('background: rgb(1,1,1);')
        color = QtWidgets.QColorDialog.getColor()
        print(color)
        print(color.getRgb()[:3])
        ms = ''
        try:
            for i, el in enumerate(color.getRgb()[:3]):
                if i == 0:
                    ms = ms + 'rgb(' + str(el) + ','
                elif i == 1:
                    ms = ms + str(el) + ','
                elif i == 2:
                    ms = ms + str(el) + ');'
        except Exception as e:
            print(e)
        style_str = 'background: '+ms
        print(style_str)
        c.setStyleSheet(style_str)




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    # os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = 'PyQt5\Qt5\plugins\platforms' добавляем переменную среды когда собираем exe
    main()
