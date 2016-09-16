import matplotlib.pyplot as plt 
import numpy as np
from random import uniform

class Particle(object):
    x = 0
    y = 0
    vx = 0
    vy = 0

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

N = 70
mu = 0.8
fig, ax = plt.subplots()
points, = ax.plot(0, 0, marker='o', linestyle='None')
ax.set_xlim(0, 100) 
ax.set_ylim(0, 100) 

particles = []
for t in range(1000):
    for p in particles:
        if p.x + p.vx > 100 or p.x + p.vx < 0:
            p.vx = -mu*p.vx
        if p.y + p.vy > 100 or p.y + p.vy < 0:
            p.vy = -mu*p.vy


            # particles.remove(p)
        # if p.x > 100 or p.x < 0 or p.y < 0 or p.y > 100:
        #     p.vx = -p.vx
        #     p.vy = -p.vy
        #     # particles.remove(p)
        for p0 in particles:
            if (p0.x+p0.vx-p.x-p.vx)**2 + (p0.y+p0.vy-p.y-p.vy)**2 < 1 and p != p0:
                p.vx = -mu*p.vx
                p.vy = -mu*p.vy

        if p.x + p.vx > 100 or p.x + p.vx < 0:
            p.vx = -mu*p.vx
        if p.y + p.vy > 100 or p.y + p.vy < 0:
            p.vy = -mu*p.vy
            
        # near = [pt for pt in particles if (pt.x - p.x)**2 + (pt.y - p.y)**2 < 25]
        # p.vx = 0.9*p.vx + 0.1*sum([n.vx for n in near])/len(near)
        # p.vy = 0.9*p.vy + 0.1*sum([n.vy for n in near])/len(near)
        p.vy -= 0.3 # g
        p.x += p.vx
        p.y += p.vy
    for i in xrange(N - len(particles)):
        particles.append(Particle(0,uniform(95., 100.),uniform(0.01, 2.),uniform(-2., 2.)))
    # for i in xrange(1):
    #     particles.append(Particle(0,uniform(95., 100.),uniform(0.01, 2.),uniform(-2., 2.)))
    x = [p.x for p in particles]
    y = [p.y for p in particles]
    # ax.relim()
    # ax.autoscale_view(True,True,True)
    points.set_data(x, y)
    # plt.pause(3.)
    plt.pause(0.0001)