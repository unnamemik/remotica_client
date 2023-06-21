import sys
from socket import *
from time import sleep
from threading import Thread
import os.path

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QStyle, QSystemTrayIcon, QAction, qApp, QMenu

import about_mod
import remotica_client

outer_host = '0.0.0.0'
outer_port = 33444
inner_host = '127.0.0.1'
inner_port = 8266

tcp_addr = (outer_host, outer_port)
udp_addr = (inner_host, inner_port)
udp_socket = socket(AF_INET, SOCK_DGRAM)
tcp_socket = socket(AF_INET, SOCK_STREAM)


def udp_sender():
    while True:
        sleep(0.08)
        with open("exchange", "r") as file:
            replay_data = file.read()[2:-1]
            print("send: ", replay_data)
            udp_socket.sendto(replay_data.encode(), udp_addr)


def connector():
    while True:
        sleep(0.08)
        global used, data
        used = b'break'
        try:
            tcp_socket.connect(tcp_addr)
            tcp_socket.send(b'query')
            data = tcp_socket.recv(1024)
        except:
            # print('Error! Connection refused!')
            sleep(1)
            break
        if data != b'break' or data != used:
            with open("exchange", "w") as file:
                file.write(str(data))
            # with open("exchange", "r") as file:
            #     print("received: ", file.read()[2:-1])
            used = data
            tcp_socket.close()
        else:
            tcp_socket.close()


class AboutMod(QDialog, about_mod.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, remotica_client.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_DriveNetIcon))

        show_action = QAction("Settings", self)
        show_action.triggered.connect(self.show)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.pushButton_OK.clicked.connect(self.socket_set)
        self.pushButton_cancel.clicked.connect(self.showMinimized)
        self.pushButton_close.clicked.connect(self.disconnect)
        self.pushButton_about.clicked.connect(show_about)


    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def disconnect(self):
        udp_socket.close()
        tcp_socket.close()
        exit(0)

    def socket_set(self):
        global outer_host, outer_port, inner_host, inner_port
        print(self.lineEdit.text())
        outer_host = self.lineEdit.text()
        outer_port = self.lineEdit_2.text()
        inner_host = self.lineEdit_3.text()
        inner_port = self.lineEdit_4.text()
        try:
            server_starter()
            self.label_6.setText('Connected.')
        except:
            self.label_6.setText('Connection refused!')


def show_about():
    cam_ = AboutMod()
    cam_.exec()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()


if __name__ == '__main__':
    class Thr1(Thread):
        def run(self):
            Thread(target=connector(), daemon=True)


    class Thr2(Thread):
        def run(self):
            Thread(target=udp_sender(), daemon=True)


    def server_starter():
        if (not os.path.isfile('exchange')):
            try:
                f = open('exchange', 'x')
            except:
                print('Error! Buffer file not created!')
        Thr1().start()
        Thr2().start()
    main()

    while True:
        sleep(1)
        if not Thr1().is_alive() or not Thr2().is_alive():
            main()
        else:
            print("Server stopped")
            sleep(5)
