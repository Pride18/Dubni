import io
import sys


from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog

import RPi.GPIO as GPIO
import time


class Pump:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)
        self.pin = pin

    def pour(self, time_delay):  # Время в секундах
        GPIO.setup(self.pin, GPIO.OUT)
        time.sleep(time_delay)
        GPIO.setup(self.pin, GPIO.IN)


class Motor:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BOARD)
        self.pin = pin

    def rotate(self, time_delay, reverse=False):  # Время в секундах
        
        print("rotate start")
        time.sleep(time_delay)
        GPIO.setup(self.pin, GPIO.OUT)
        print("rotate stop")


juice = Pump(18)
water = Pump(16)
mint = Pump(22)



recipes = {  # (water_units, juice_units, mint_units)
    "": (0, 0, 0),
    "Газированная вода": (5, 0, 0),
    "Мятный сироп": (0, 0, 1),
    "Апельсиновый сок": (0, 4, 0),
    "Лимонад “Мятный”": (8, 0, 2),
    "Лимонад “Заводной апельсин”": (3, 5, 0),
    "Лимонад ‘Тройной”": (3.5, 4.5, 1)
}

initial_time_rotate = 1  # Время для оборота первого стакана на выдачу
time_per_cup = 1  # Время для поворота на одного стакана.
time_per_10ml = 1


def process_the_order(slots):
    for i in range(len(slots)):
        
        water_time, juice_time, mint_time = recipes[slots[i]]
        print(1, water_time, juice_time, mint_time)
        water.pour(time_per_10ml * water_time)
        juice.pour(time_per_10ml * juice_time)
        mint.pour(time_per_10ml * mint_time)




template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>order</class>
 <widget class="QMainWindow" name="order">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Order</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="choice1">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>100</y>
      <width>141</width>
      <height>151</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>-1</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    font-size: 30px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 5px 5px;
    cursor: pointer;
}
</string>
    </property>
    <property name="text">
     <string>-НИЧЕГО-</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Choices</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="choice2">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>100</y>
      <width>141</width>
      <height>151</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>-1</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    font-size: 30px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 5px 5px;
    cursor: pointer;
}</string>
    </property>
    <property name="text">
     <string>-НИЧЕГО-</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Choices</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="choice3">
    <property name="geometry">
     <rect>
      <x>430</x>
      <y>100</y>
      <width>141</width>
      <height>151</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>-1</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    font-size: 30px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 5px 5px;
    cursor: pointer;
}</string>
    </property>
    <property name="text">
     <string>-НИЧЕГО-</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Choices</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="choice4">
    <property name="geometry">
     <rect>
      <x>610</x>
      <y>100</y>
      <width>141</width>
      <height>151</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>-1</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    font-size: 30px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 5px 5px;
    cursor: pointer;
}</string>
    </property>
    <property name="text">
     <string>-НИЧЕГО-</string>
    </property>
    <attribute name="buttonGroup">
     <string notr="true">Choices</string>
    </attribute>
   </widget>
   <widget class="QPushButton" name="finish">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>392</y>
      <width>271</width>
      <height>91</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>-1</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
    font-size: 30px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 5px 5px;
    cursor: pointer;
}</string>
    </property>
    <property name="text">
     <string>СДЕЛАТЬ ЗАКАЗ</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="Choices"/>
 </buttongroups>
</ui>
"""
slots = ['', '', '', '']


class Order(QMainWindow):
    count = 0
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.Choices.buttonClicked.connect(self.choice)
        self.finish.clicked.connect(self.run)
        self.choice1.setText('')
        self.choice2.setText('')
        self.choice3.setText('')
        self.choice4.setText('')

    def choice(self, btn):
        NOTHING = 'Ничего'
        drink, ok_pressed = QInputDialog.getItem(
            self, "Выбор", "Выберите ваш напиток",
            ("Газированная вода", "Мятный сироп", "Апельсиновый сок", "Лимонад “Мятный”", "Лимонад “Заводной апельсин”"
             , "Лимонад ‘Тройной”", "Ничего"), 0, False)
        if ok_pressed:
            slot = int(btn.objectName()[-1]) - 1
            if drink != NOTHING:
                btn.setIcon(QtGui.QIcon(f'{drink}.png'))
                btn.setIconSize(QtCore.QSize(85, 85))
            else:
                slots[slot] = drink
                btn.setIcon(QtGui.QIcon())
            if drink != NOTHING:
                slots[slot] = drink
            else:
                slots[slot] = ''

    def run(self):
        process_the_order(slots)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Order()
    ex.show()
    sys.exit(app.exec())
