import numpy as npp
import pandas as pdd
from sklearn.linear_model import LinearRegression as lrr
import matplotlib.pyplot as pltt

data = pdd.read_csv("linear.csv")
x = data["metrekare"]
y = data["fiyat"]
x = x.reshape(99,1)# Verileri 99x1 Martis olarak belitiyoruz
y = y.reshape(99,1)
lineerregresyon = lrr() # Lineer Regresyonu çağırdık.
lineerregresyon.fit(x,y) # Verilerimizi x ve y eksenine oturttuk.
lineerregresyon.predict(x) #x'e göre, yani metrekareye göre ev fiyatlarını tahmin edeceğiz.
m = lineerregresyon.coef_ # Coefficient - yani katsayı, bu komutla eğimimizi
                          # Yani m i buluyoruz.
b= lineerregresyon.intercept_ # Intercept - b dir. yani y = mx+b 'de x'e sıfır 
                              # verdiğimizde kalan değer.
a = npp.arange(150)
pltt.scatter(x,y) # Gerçek verilerimizi nokta nokta, scatter ile cizdiriyoruz.
pltt.scatter(a,m*a+b, c="red",marker=">")
pltt.show()

print('Eğim: ', lineerregresyon.coef_)
print('Y de kesiştiği yer: ', lineerregresyon.intercept_)
print("Denklem")
print("y=",m,"x+",b)




