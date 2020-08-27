from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import mysql.connector

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

baglanti = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='sinema')


class program(QDialog):
    def __init__(self,ebeveyn=None):
        #(ebeveyn(parent)bir alt sayfa açmasını engelliyor.)
        super(program,self).__init__(ebeveyn)

        izgara=QGridLayout()

        self.yazi_alani1 = QLabel("komedi")
        self.yazi_alani2 = QLabel("korku")
        self.yazi_alani3 = QLabel("drama")
        self.yazi_alani4 = QLabel("aksiyon")
        
        self.yazi_alani5 = QLabel("2017")
        self.yazi_alani6 = QLabel("2018")
        self.yazi_alani7 = QLabel("2019")
        
        self.giris1 = QLineEdit()
        self.giris2 = QLineEdit()
        self.giris3 = QLineEdit()
        
        self.giris4 = QLineEdit()
        self.giris5 = QLineEdit()
        self.giris6 = QLineEdit()
        
        self.giris7 = QLineEdit()
        self.giris8 = QLineEdit()
        self.giris9 = QLineEdit()
        
        self.giris10 = QLineEdit()
        self.giris11 = QLineEdit()
        self.giris12 = QLineEdit()
        
        self.button = QPushButton("Ekle")
        self.sonuc = QLabel("")
        self.bos = QLabel("")
        self.button2 = QPushButton("Veritabanından Tahminle")
        
        self.komedi = QLabel("Komedi")
        self.komedi1 = QLabel("")
        
        self.korku = QLabel("Korku")
        self.korku1 = QLabel("")
        
        self.drama = QLabel("Drama")
        self.drama1 = QLabel("")
        
        self.aksiyon = QLabel("Aksiyon")
        self.aksiyon1 = QLabel("")
        
        
        izgara.addWidget(self.yazi_alani1,1,0)
        izgara.addWidget(self.yazi_alani2,2,0)
        izgara.addWidget(self.yazi_alani3,3,0)
        izgara.addWidget(self.yazi_alani4,4,0)
        
        izgara.addWidget(self.yazi_alani5,0,1)
        izgara.addWidget(self.yazi_alani6,0,2)
        izgara.addWidget(self.yazi_alani7,0,3)
        
        izgara.addWidget(self.giris1,1,1)
        izgara.addWidget(self.giris2,1,2)
        izgara.addWidget(self.giris3,1,3)
        
        izgara.addWidget(self.giris4,2,1)
        izgara.addWidget(self.giris5,2,2)
        izgara.addWidget(self.giris6,2,3)
        
        izgara.addWidget(self.giris7,3,1)
        izgara.addWidget(self.giris8,3,2)
        izgara.addWidget(self.giris9,3,3)
        
        izgara.addWidget(self.giris10,4,1)
        izgara.addWidget(self.giris11,4,2)
        izgara.addWidget(self.giris12,4,3)
        
        izgara.addWidget(self.button,5,3)
        izgara.addWidget(self.sonuc,6,3)
        izgara.addWidget(self.bos,7,3)
        izgara.addWidget(self.button2,8,3)
        
        izgara.addWidget(self.komedi,9,1)
        izgara.addWidget(self.komedi1,9,2)
        
        izgara.addWidget(self.korku,10,1)
        izgara.addWidget(self.korku1,10,2)
        
        izgara.addWidget(self.drama,11,1)
        izgara.addWidget(self.drama1,11,2)
        
        izgara.addWidget(self.aksiyon,12,1)
        izgara.addWidget(self.aksiyon1,12,2)
        
        
        self.button.clicked.connect(self.fonksiyon)
        self.button2.clicked.connect(self.fonksiyon2)

        self.setLayout(izgara)

        self.setWindowTitle("Ülke Ekleme")

       

    def fonksiyon(self):

        isaretci=baglanti.cursor()
        
        komedi1 = int(self.giris1.text())
        komedi2 = int(self.giris2.text())
        komedi3 = int(self.giris3.text())
        
        korku1 = int(self.giris4.text())
        korku2 = int(self.giris5.text())
        korku3 = int(self.giris6.text())
        
        drama1 = int(self.giris7.text())
        drama2 = int(self.giris8.text())
        drama3 = int(self.giris9.text())
        
        aksiyon1 = int(self.giris10.text())
        aksiyon2 = int(self.giris11.text())
        aksiyon3 = int(self.giris12.text())
        
        
        

        isaretci.execute("INSERT INTO komedi (yil17,yil18,yil19) VALUES ('%s','%s','%s')"%(komedi1,komedi2,komedi3))
        isaretci.execute("INSERT INTO korku (yil17,yil18,yil19) VALUES ('%s','%s','%s')"%(korku1,korku2,korku3))
        isaretci.execute("INSERT INTO drama (yil17,yil18,yil19) VALUES ('%s','%s','%s')"%(drama1,drama2,drama3))
        isaretci.execute("INSERT INTO aksiyon (yil17,yil18,yil19) VALUES ('%s','%s','%s')"%(aksiyon1,aksiyon2,aksiyon3))
        
        baglanti.commit()

        baglanti.close()

        self.sonuc.setText("Veriler Eklendi")
        
    def fonksiyon2(self):
        
        def fonk1():
            isaretci=baglanti.cursor()
            
            isaretci.execute("Select * From komedi")
            liste = isaretci.fetchall()
            
            
            yil17 = 17
            yil18 = 18
            yil19 = 19
            
            
            for i in liste:
               
                yil17 = i[0]
                yil18 = i[1]
                yil19 = i[2]
                
            d={'yillar':[1,2,3],'degerler':
                [yil17,yil18,yil19,]}
            
            df = pd.DataFrame(data=d)
            
            yillar=df[['yillar']]
            degerler=df[['degerler']]
            
            from sklearn.model_selection import train_test_split
            
            x_train,x_test,y_train,y_test=train_test_split(yillar,degerler,test_size=0.33,random_state=0)
            
            from sklearn.linear_model import LinearRegression
            
            lr = LinearRegression()
            lr.fit(x_train,y_train)
            
            tahmin=str(lr.predict([[4]]))
            
            self.komedi1.setText(tahmin)
            
        def fonk2():
            isaretci=baglanti.cursor()
            
            isaretci.execute("Select * From korku")
            liste = isaretci.fetchall()
            
            
            yil17 = 17
            yil18 = 18
            yil19 = 19
            
            
            for i in liste:
               
                yil17 = i[0]
                yil18 = i[1]
                yil19 = i[2]
                
            d={'yillar':[1,2,3],'degerler':
                [yil17,yil18,yil19,]}
            
            df = pd.DataFrame(data=d)
            
            yillar=df[['yillar']]
            degerler=df[['degerler']]
            
            from sklearn.model_selection import train_test_split
            
            x_train,x_test,y_train,y_test=train_test_split(yillar,degerler,test_size=0.33,random_state=0)
            
            from sklearn.linear_model import LinearRegression
            
            lr = LinearRegression()
            lr.fit(x_train,y_train)
            
            tahmin=str(lr.predict([[4]]))
            
            self.korku1.setText(tahmin)
            
        def fonk3():
            isaretci=baglanti.cursor()
            
            isaretci.execute("Select * From drama")
            liste = isaretci.fetchall()
            
            
            yil17 = 17
            yil18 = 18
            yil19 = 19
            
            
            for i in liste:
               
                yil17 = i[0]
                yil18 = i[1]
                yil19 = i[2]
                
            d={'yillar':[1,2,3],'degerler':
                [yil17,yil18,yil19,]}
            
            df = pd.DataFrame(data=d)
            
            yillar=df[['yillar']]
            degerler=df[['degerler']]
            
            from sklearn.model_selection import train_test_split
            
            x_train,x_test,y_train,y_test=train_test_split(yillar,degerler,test_size=0.33,random_state=0)
            
            from sklearn.linear_model import LinearRegression
            
            lr = LinearRegression()
            lr.fit(x_train,y_train)
            
            tahmin=str(lr.predict([[4]]))
            
            self.drama1.setText(tahmin)
            
        def fonk4():
            isaretci=baglanti.cursor()
            
            isaretci.execute("Select * From aksiyon")
            liste = isaretci.fetchall()
            
            
            yil17 = 17
            yil18 = 18
            yil19 = 19
            
            
            for i in liste:
               
                yil17 = i[0]
                yil18 = i[1]
                yil19 = i[2]
                
            d={'yillar':[1,2,3],'degerler':
                [yil17,yil18,yil19,]}
            
            df = pd.DataFrame(data=d)
            
            yillar=df[['yillar']]
            degerler=df[['degerler']]
            
            from sklearn.model_selection import train_test_split
            
            x_train,x_test,y_train,y_test=train_test_split(yillar,degerler,test_size=0.33,random_state=0)
            
            from sklearn.linear_model import LinearRegression
            
            lr = LinearRegression()
            lr.fit(x_train,y_train)
            
            tahmin=str(lr.predict([[4]]))
            
            self.aksiyon1.setText(tahmin)
            
        Fonk1 = fonk1()
        Fonk2 = fonk2()
        Fonk3 = fonk3()
        Fonk4 = fonk4()
        
        
        
        
        
uyg = QApplication([])
pencere = program()
pencere.show()
uyg.exec_()
