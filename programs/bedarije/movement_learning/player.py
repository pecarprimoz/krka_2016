from PyQt4.QtCore import *
from PyQt4.QtGui import *

'''
def window():
    #application object, kaj dejansko delamo
    app=QtGui.QApplication(sys.argv)
    #widget katerega spreminjamo
    w= QtGui.QWidget()
    #labelo ki jo damo v widget
    b= QtGui.QLabel(w)
    b.setText("Hello world")
    #pozicija okna
    w.setGeometry(100,100,200,50)
    #pozicija labele
    b.move(50,20)
    w.setWindowTitle("Prvič")
    w.show()
    sys.exit(app.exec_())
'''
'''
def window():
    app=QApplication(sys.argv)
    win=QDialog()
    b1=QPushButton(win)
    b1.setText("Button1")
    b1.move(50,20)
    b1.clicked.connect(b1_clicked)
    b2= QPushButton(win)
    b2.setText("Memes")
    b2.move(50,50)
    QObject.connect(b2,SIGNAL("clicked()"),b2_clicked)

    win.setGeometry(100,100,200,100)
    win.show()
    sys.exit(app.exec_())
def b1_clicked():
    print("fuck")
def b2_clicked():
    print("what")
'''
