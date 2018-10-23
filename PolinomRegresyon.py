import numpy as npp
import pandas as pdd
from sklearn.preprocessing import PolynomialFeatures as pff
import matplotlib.pyplot as pltt
from sklearn.linear_model import Perceptron
from sklearn import linear_model

data = pdd.read_csv("linear.csv")

x = data["metrekare"]
y = data["fiyat"]

x = npp.array(x)#Numpy ile matrisleri olusrutalım.
y= npp.array(y)

a,b,c,d,e,f =  npp.polyfit(x,y,5)# ax^5+bx^4+cx^3+dx^2+ex+f denkelmini 5. dereceden olması için
yeni = npp.arange(150)
pltt.scatter(x,y)# Scatter ile nokta çizdirimi yapıyoruz.

pltt.plot(yeni,a*(yeni**5)+b*(yeni**4)+c*(yeni**3)+d*(yeni**2)+e*yeni+f)#
pltt.show()


