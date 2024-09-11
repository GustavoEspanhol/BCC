import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-5, 2, 0.1)
print (x)              # mostra os valores de x
y = x*x*x-3*(x*x)+100      # calcula os valores de y = xˆ2 -2x +1
print (y) 

plt.plot(x,y)
plt.show()


