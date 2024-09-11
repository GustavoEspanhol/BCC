import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi+0.1,0.1)
y = 1+np.sin(2*x)


plt.plot(x,y)
plt.show()