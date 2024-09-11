import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2,2.1,0.1)
y1 = np.exp(x)
y2 = 3*(x**2)

plt.plot(x,y1,'r')
plt.plot(x,y2,'b')
plt.grid()
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.show()
