f0 = 261.625565301
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

import matplotlib.pyplot as plt

from math import *
import numpy as np
# def f(i):
#     return f0 * 2**(i / 12.)

def note(f):
    # return notes[int(round(12 * log(f / f0 ,2))) % 12]
    return int(round(12 * log(f / f0 ,2))) % 12

def h(f, n):
    for i in xrange(1, n + 1):
        f += f / i
    return note(f)


# for i in xrange(30):
#     print h(f0, i),
# harmonics = [h(f0, i) for i in xrange(100)]

x = np.linspace(0, 1000, 100)
h = [sin(i) for i in x]
# print harmonics
plt.plot(x, h, 'ko-')
plt.show()
