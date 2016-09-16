from math import pi

seconds_phase = 0
minutes_phase = 0
hours_phase = 0

k = 0.1 # 0.1 in fut
accur = 20
seconds_w = k * accur / 60 
minutes_w = k * accur / 3600
hours_w = k * accur / 216000

def clock(phase, w):
    phase_temp = phase
    phase += w
    if phase > 12:
        phase = 12 - phase_temp
    return phase

import matplotlib.pyplot as plt
S = []
M = []
H = []


for t in xrange(100000):
    S.append(seconds_phase)
    M.append(minutes_phase)
    H.append(hours_phase)
    seconds_phase = clock(seconds_phase, seconds_w)
    minutes_phase = clock(minutes_phase, minutes_w)
    hours_phase = clock(hours_phase, hours_w)
    if seconds_phase == minutes_phase == hours_phase:
        print seconds_phase

plt.plot(S, 'k-')
plt.plot(M, 'b-')
plt.plot(H, 'r-')
plt.show()

