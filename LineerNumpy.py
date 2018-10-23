import numpy as npp #numpy matemetik kütüphanesi tüm işlemleri yapabiliyoruz
import pandas as pdd #düzgün veri çekmek için kullanılır
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as pltt # Verileri çizdirmek için kullanılır.

data = pdd.read_csv("linear.csv")  # Verimizi okuyoruz
print(data) # Veriyi inceleyelim.
x = data["metrekare"] # Metrekareleri bir axis' e çekelim, panda nın özelliği.
y = data["fiyat"] 

x = pdd.DataFrame.as_matrix(x) # NumPy matrisine dönüştürelim.
y = pdd.DataFrame.as_matrix(y) # NumPy matrisine dönüştürelim.

pltt.scatter(x,y) # Ne oluşturduğumuza 2 boyutlu grafikte bakalım.
				  #Doğrumuzun denklemi y = m*a+b , Biz ise en uygun m ve b yi arıyoruz. m Eğim, b kesim noktası
m,b = npp.polyfit(x,y,1)# NumPy bizim için grafiğe oturtuyor çizgimizi. Bunu matematiksel
						# npp.polyfit(x,y,1) formülü bizim için m ve b degeri buluyor.
						# npp.polyfit(x ekseni, y ekseni, kaçıncı dereceden polinom denklemi) ki biz birinci dereceden kullanacağız.

a = npp.arange(150) # Denklemimiz hazır. a nın aralığını ayarlayalım.
pltt.scatter(x,y) # Scatter ile nokta çizdirimi yapıyoruz.
pltt.plot(m*a+b)
yenideger = int(input("Kaç metrekare?"))
tahmin = m*yenideger+b
print(tahmin)
pltt.scatter(yenideger,tahmin,c="red",marker=">")
pltt.show()
print("y=",m,"x+",b)

