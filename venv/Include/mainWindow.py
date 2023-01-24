import sys
import time
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets
import juanzhou
from read import readXML as rxml
from sec import Ui_Child
import re

input_str=''
rx = rxml()


class mainWindow(QMainWindow,juanzhou.Ui_MainWindow):
    # search_name='空值'
    def __init__(self ):
        QMainWindow.__init__(self)
        juanzhou.Ui_MainWindow.__init__(self)
        #主要界面
        self.setupUi(self)
        # #tip界面
        # self.setupUi2(self)
        # 设置窗口图标
        self.setWindowIcon(QIcon("res/app1.ico"))
        # 设置窗口名
        self.setWindowTitle("健康卷轴")
        #实时获取输入值，传递给查询按钮作为信号
        # self.lineEdit.textEdited[str].connect(self.onChange)
        # 查询的信号和槽
        # self.pushButton.clicked.connect(lambda :self.picChange(self.search_name))
        self.pushButton.clicked.connect(self.start)
        # self.detail.clicked.connect()
    # def onChange(self):
    #    self.search_name = self.lineEdit.text()
    #    print(self.search_name)




    def start(self):
        if self.lineEdit.text() =="":
            rx.pic("qwer")
            pix = QPixmap("效果图.png")
            self.label_2.setPixmap(pix)
        else:
            input_str=self.lineEdit.text()
            rx.pic(input_str)
            pix = QPixmap("效果图.png")
            self.label_2.setPixmap(pix)
            if rx.flag!=2:
                self.detail.raise_()
                self.detail.show()
            else:
                self.detail.hide()
    def l(self):

        self.label_2.setPixmap(QtGui.QPixmap("res/bg_1.png"))
    # def picChange(self,search_name):
    #     if search_name in search.keys():
    #         num=search[search_name]
    #         self.label_2.setPixmap(QPixmap(""))
    #         self.label_2.setStyleSheet(f"background-image: url(res/bg_{num}.png);\n"
    #                              " ")
    #         # rx.pic(self.lineEdit.text())
    #         # self.label_2.setStyleSheet("效果图.png")
    #         QApplication.processEvents()
    #         time.sleep(1)



class Child(QMainWindow, Ui_Child):
    textList=[]
    def __init__(self):
        super(Child, self).__init__()
        self.setupUi(self)
        self.textList=[self.textBrowser, self.textBrowser_2,
                    self.textBrowser_3, self.textBrowser_4, self.textBrowser_5, self.textBrowser_6,
                    self.textBrowser_7,
                    self.textBrowser_8, self.textBrowser_9, self.textBrowser_10, self.textBrowser_11,
                    self.textBrowser_12]

    def open(self):
        a = 0
        print(rx.flag)
        self.show()
        if rx.flag == 0:
            print(rx.input_str)
            ma = rx.getMajor(rx.input_str)
            print(ma)
            rc = re.compile("\d+、.*?\n")
            majors = re.findall(rc, ma)
            for major in majors:
                # self.textBrowser.setText(major)
                self.textList[a].setFontPointSize(16)
                # self.textList[a].setFontFamily("STXINGKA.TTF")
                self.textList[a].setText("<font color='black'size='15' face='STXingkai'>"+major+"</font>")
                a+=1
                if a==11:
                    self.textBrowser_12.setFontPointSize(16)
                    self.textBrowser_12.setText("<font color='black'size='24' face='STXingkai'>...........</font>")
                    break
            while a<=10:
                self.textList[a].setText("")
                a+=1
        else:
            ns=rx.getNodeBySick(rx.input_str)
            ls=rx.getPrescription(rx.input_str)
            for n in ns:
                str=ls[a]
                self.textList[a].setText("<font color='black' size='15' face='STXingkai'>" +str+ "</font>")
                # print(n.getAttribute('name'))
                # rx.getPrescription(rx.input_str)
                # self.textList[a].setText("<font color='black'size='15' face='STXingkai'>"+a+"</font>")
                a += 1
                if a==len(ls):
                    break
                elif a==11:
                    self.textBrowser_12.setText("<font color='black'size='24' face='STXingkai'>...........</font>")
                    break
            while a<=10:
                self.textList[a].setText("")
                a+=1

if __name__=='__main__':
    app=QApplication(sys.argv)
    mw=mainWindow()
    ch=Child()
    movie = QtGui.QMovie("res/pc.gif")
    mw.label_2.setMovie(movie)
    mw.show()
    movie.start()

    mw.detail.clicked.connect(ch.open)
    sys.exit(app.exec_())