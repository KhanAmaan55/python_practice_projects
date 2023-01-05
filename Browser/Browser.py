import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import*

class Mainwindow(QMainWindow):
    
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        homebtn = QAction("HOME", self)
        homebtn.triggered.connect(self.nav_home)
        navbar.addAction(homebtn)

        backbutton = QAction('BACK', self)
        backbutton.triggered.connect(self.browser.back)
        navbar.addAction(backbutton)

        frdbutton = QAction("FORWARD", self)
        frdbutton.triggered.connect(self.browser.forward)
        navbar.addAction(frdbutton)

        reloadbtn = QAction("RELOAD", self)
        reloadbtn.triggered.connect(self.browser.reload)
        navbar.addAction(reloadbtn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.nav_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

    def nav_home(self):
        self.browser.setUrl(QUrl('http://www.google.com'))
    def nav_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self,q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('Browser')
window = Mainwindow()
app.exec_()