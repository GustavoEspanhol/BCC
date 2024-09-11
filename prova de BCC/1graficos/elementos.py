import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10,10)
y1 = x*x
y2 = -x*x
y3 = x
plt.plot(x,y1,'b.-',label='B')
plt.plot(x,y2,label='C')
plt.plot(x,y3, label='C')
plt.title("sifude prova de BCC")
plt.grid() 
plt.xlabel("de boné")
plt.ylabel("meu pau")
plt.legend()
plt.axis('equal') #eixos em mesma escala
plt.show()