import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2,4.1,0.1)
y = x**4 - 4* x**3 + x**2 +1

plt.plot(x,y)
plt.grid()
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.show()


