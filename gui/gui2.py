import sys
#from m2 import *
from PyQt5.QtCore import QTimer,QTime
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QPainter, QPixmap 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget ,QLabel,QDesktopWidget,QTableWidget,QListWidgetItem,QListWidget
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

CSS = \
{
    'QWidget':
    {
        'background-color': '#1E272C',
    },
    
    'QLabel#label':
    {
        'color': '#888888',
        'background-color': '#444444',
        'font-weight': 'bold',
    },
    'QLabel#label:active':
    {
        'color': '#1d90cd',
    },
    'QPushButton#button':
    {
        'color': '#888888',
        'background-color': 'transparent',
        'font-weight': 'bold',
        'border': 'none',
        'padding': '15px',
    },
    
    'QPushButton#button:hover':
    {
     
        'background': 'hsla(190, 97%, 38%,0.4)',

    },
   
    'QPushButton#rect':
    {
	 'background': 'hsla(190, 97%, 38%,0.1)',
    },
    'QPushButton#bb':
    {

        'background-color': 'green',
        'font-weight': 'bold',
        'border': 'none',
        'padding': '15px',
        'text-align': 'center'
        
        
    },

    'QPushButton#bb:hover':
    {
	 'background': 'red',
    },
    'QTableWidget':
    {
	 
	 
	 'color':'white',
	 'border':'0px',
	 #'background': 'hsla(190, 97%, 38%,0.1)',
	 'padding':'60px',
 	 'padding-top':'15px',
  	 'padding-bottom':'185px',
    }

}
cc=1
def dictToCSS(dictionnary):
    stylesheet = ""
    for item in dictionnary:
        stylesheet += item + "\n{\n"
        for attribute in dictionnary[item]:
            stylesheet += "  " + attribute + ": " + dictionnary[item][attribute] + ";\n"
        stylesheet += "}\n"
    return stylesheet


class WidgetButtons(QWidget):  #home page
    def __init__(self):
        super().__init__()
        self.movie = QMovie("g2.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()
        self.C = QLabel('C', self)
        self.C.setFont(QFont('Arial', 55))	
        self.C.setStyleSheet("color: #171717; background: white")
        self.C.move(117,240)
        self.DOT1 = QLabel('.', self)
        self.DOT1.setFont(QFont('Arial', 65))
        self.DOT1.setStyleSheet("color: #171717; background: transparent")
        self.DOT1.move(175, 225)
        self.A = QLabel('A', self)
        self.A.setFont(QFont('Arial', 55))
        self.A.setStyleSheet("color: #171717; background: white")
        self.A.move(210,240)
        self.DOT2 = QLabel('.', self)
        self.DOT2.setFont(QFont('Arial', 65))
        self.DOT2.setStyleSheet("color: #171717; background: transparent")
        self.DOT2.move(270, 225)
        self.T = QLabel('T', self)
        self.T.setFont(QFont('Arial', 55))
        self.T.move(295,240)
        self.T.setStyleSheet("color: #039fbe; background:transparent;");
        self.DOT3 = QLabel('.', self)
        self.DOT3.setFont(QFont('Arial', 65))
        self.DOT3.setStyleSheet("color:  white; background: transparent")
        self.DOT3.move(335, 225)
        self.C1 = QLabel('C', self)
        self.C1.setFont(QFont('Arial', 55))
        self.C1.setStyleSheet("color: white; background:transparent;")
        self.C1.move(365,240)
        self.DOT4 = QLabel('.', self)
        self.DOT4.setFont(QFont('Arial', 65))
        self.DOT4.setStyleSheet("color: white; background: transparent")
        self.DOT4.move(425,225)
        self.H = QLabel('H', self)
        self.H.setFont(QFont('Arial', 55))
        self.H.setStyleSheet("color: white; background:transparent;")
        self.H.move(455,240)
        
        
    def paintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frameRect.left(), frameRect.top(), currentFrame)
        
        
       

class WidgetLineEdits(QWidget):
    def __init__(self):
        super().__init__()
        
     
        
            
            


class WidgetRadioButtons(QWidget):
    def __init__(self):
        super().__init__()
        global cc
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(14)  
  
        #Column count 
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setGeometry(100, 30, 185, 185)
        
        
  
       # self.timer = QTimer()
        #self.timer.timeout.connect(self.up)
        #self.timer.start(9000) # repeat self.update_labelTime every 1 sec 
	      
      
        self.layout = QVBoxLayout() 
       
	
        self.layout.addWidget(self.tableWidget)
  #      self.layout.addWidget(self.button2)
         
        self.setLayout(self.layout)
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch) 
        self.button2 = QPushButton("Scan",self)
        self.button2.setObjectName("button")
        self.button2.setGeometry(200, 470, 85, 85)
        self.button2.clicked.connect(self.up)
            
		
    def up(self):
    	print("up")
    	exploit.execute(payload=payload_win)
    	x=client.sessions.list
    	liz=list(x.keys())
    	print(liz)
    	count=1
    	for i in liz:
           
	        val=x[str(i)]["info"]
	        self.tableWidget.setItem(0,1, QTableWidgetItem(str(val)))
	        count+=1
       

      

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
       	
        mainLayout = QVBoxLayout()
        #mainLayout.addStretch(1)
        #mainLayout.setSpacing(0);
        
#        mainLayout.addWidget(NoC);
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(WidgetButtons()) # index 0
        self.stackedWidget.addWidget(WidgetLineEdits()) # index 1
        self.stackedWidget.addWidget(WidgetRadioButtons()) # index 2
        buttonPrevious = QPushButton('Previous')
        buttonPrevious.clicked.connect(self.previousWidget)	
      
  
        buttonNext = QPushButton('Next')
       
        buttonNext.clicked.connect(self.nextWidget)
        
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(buttonPrevious,stretch=1)
        buttonLayout.addWidget(buttonNext,stretch=1)

        mainLayout.addWidget(self.stackedWidget)
        #mainLayout.addLayout(buttonLayout)
        
        self.setLayout(mainLayout)
        
       
        self.setStyleSheet(dictToCSS(CSS))

        self.rect = QPushButton("",self)
        self.rect.setStyleSheet("font-size:40px;\
        border: 1px solid #222222")
        self.rect.setGeometry(0, 205, 45, 175)
        self.rect.setObjectName("rect")
        self.rect.setFocusPolicy(QtCore.Qt.NoFocus)
        
        self.button = QPushButton("",self)
        self.button.setObjectName("button")
        self.button.clicked.connect(self.nextWidget)
        
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.setIcon(QIcon('h1.png'))
        self.button.setIconSize(QSize(35,35));
        self.button.setGeometry(4,220,35,35) 
        self.button1 = QPushButton("",self)
        self.button1.setObjectName("button")
        self.button1.clicked.connect(self.previousWidget)
        self.button1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button1.setIcon(QIcon('apk.png'))
        self.button1.setIconSize(QSize(35,35));
        self.button1.setGeometry(4,277,35,35) 
        self.button2 = QPushButton("",self)
        self.button2.setObjectName("button")
        self.button2.clicked.connect(self.previousWidget)
        self.button2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button2.setIcon(QIcon('f2.png'))
        self.button2.setIconSize(QSize(35,35));
        self.button2.setGeometry(4,325,35,35) 
        
        self.button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        
        
        
       

    def nextWidget(self):
        self.stackedWidget.setCurrentIndex(0)     
       
    
       
        


    def previousWidget(self):
    	global cc
    	cc+=1
    	
    	self.stackedWidget.setCurrentIndex(2)
    	WidgetRadioButtons()
             
        
        

app = QApplication(sys.argv)

demo = AppDemo()
demo.setFixedSize(650, 600)


demo.show()
sys.exit(app.exec_())
