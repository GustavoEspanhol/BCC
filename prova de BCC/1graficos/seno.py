import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10.1,0.1)
y = np.sqrt(np.sin(x)*np.cos(x)+2)
plt.plot(x,y)

z = np.arange(-5,5,0.1)
l = np.sin(z)*(np.sin(z)+np.cos(z))**2
plt.plot(z,l)
plt.show()
            