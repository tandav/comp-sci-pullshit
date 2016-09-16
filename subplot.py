import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)
plt.subplot(2, 1, 1)  # 2x1 grid, first plot
plt.plot(x, np.sin(x))
plt.title('Trig is easy.')

plt.subplot(2, 1, 2)  # 2x1 grid, second plot
plt.plot(x, np.cos(x))
plt.xlabel('x')
plt.show()