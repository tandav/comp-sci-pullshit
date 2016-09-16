import matplotlib.pyplot as plt 
import numpy as np

fig, ax = plt.subplots()

x = 1
y = 1

for t in range(100):
    if t == 0:
        # points, = ax.plot(x, y, marker='o', linestyle='None')
        points, = ax.plot(x, y, marker='o', linestyle='None')
        ax.set_xlim(0, 10) 
        ax.set_ylim(0, 10) 
    else:
        x += 00000.1*t
        y += 0.1*t + 0.01*t**2
        points.set_data(x, y)
    plt.pause(0.3)