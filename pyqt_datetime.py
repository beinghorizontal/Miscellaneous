# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 23:18:14 2020

@author: alex1
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPalette, QFont
from PyQt5 import QtGui
from datetime import date, timedelta, datetime
import psutil
import time
import warnings

warnings.filterwarnings('ignore')

qApp = QApplication(sys.argv)
screen = qApp.primaryScreen()
rect = screen.availableGeometry()


def dl_ul():
    dl_old_value = 0
    ul_old_value = 0
    i = 0
    while i < 2:
        i += 1
        dl_new_value = psutil.net_io_counters().bytes_recv
        ul_new_value = psutil.net_io_counters().bytes_sent

        if dl_old_value:
            dl = round((dl_new_value - dl_old_value) / 1024, 2)

        if ul_old_value:
            ul = round((ul_new_value - ul_old_value) / 1024, 2)

        dl_old_value = dl_new_value
        ul_old_value = ul_new_value

        time.sleep(0.8)
    return dl, ul


class MainWindow(QMainWindow):
    # constructor
    def __init__(self):
        QMainWindow.__init__(self)
        # counter
        self.i = 0
        # add QLabel
        self.qLbl = QLabel('Date time')

        self.setCentralWidget(self.qLbl)
        self.qTimer = QTimer()
        self.qTimer.setInterval(1000)  # 1000 ms = 1 s
        # connect timeout signal to signal handler
        self.qTimer.timeout.connect(self.getSensorValue)
        # start timer
        self.qTimer.start()

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.FramelessWindowHint)

        # set the title
        self.setWindowTitle("pyqt_datetime")

        # setting  the geometry of window
        self.setGeometry(rect.width() - 225, rect.height() - 75, 220, 60)  # x,y, GUI Width, height
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

    def getSensorValue(self):
        self.i += 1
        # print('%d. call of getSensorValue()' % self.i)
        self.qLbl.setText('%d. call of getSensorValue()' % self.i)

        mdate = date.today() + timedelta(0)
        msday = mdate.strftime('%A')
        # print(mdate, msday)
        tx = str((datetime.now().strftime("%H:%M:%S")))
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        # net_counters = psutil.net_io_counters()
        speed = dl_ul()
        if speed[0] > 1000:
            t1 = round(speed[0] / 1000, 2)
            dn_string = str(t1) + ' Mbps'
        else:
            dn_string = str(speed[0]) + ' Kbps'
        if speed[1] > 1000:
            t2 = round(speed[1] / 1000, 2)
            ul_string = str(t2) + ' Mbps'
        else:
            ul_string = str(speed[1]) + ' Kbps'

        self.qLbl.setText('{} {} {}\n CPU:{}% RAM:{}%\n Dn:{} Ul:{} '.format(str(mdate), str(msday),
                                                                             str(tx), str(cpu), str(mem),
                                                                             dn_string, ul_string))

        self.qLbl.setFont(QFont('Times', 10))


palette = QPalette()
# palette.setColor(QPalette.ButtonText, Qt.red)
palette.setColor(QPalette.Foreground, Qt.cyan)
qApp.setPalette(palette)
qApp.setStyle('Fusion')
# setup GUI
qWin = MainWindow()
qWin.show()
# run application
sys.exit(qApp.exec_())
