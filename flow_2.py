import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint


fig = plt.figure()

N = 10 # size of box
n = 20 # number of particles
box = np.zeros((N, N), np.int)
# box[0][0] = 10

class Particle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

particles = [Particle(0, randint(0, N - 1), 
            randint(1, 2), randint(-2, 2)) for x in range(n)]

for p in particles:
    box[p.y][p.x] += 1

def step():
    ar_prev = box
    for p in particles:
        box[p.y][p.x] = ar_prev[p.x][p.y] - 1
        p.x += p.vx
        p.y += p.vy
        if p.x < N - 1 and p.y < N - 1 and p.x > 0 and p.y > 0:
            box[p.y][p.x] = ar_prev[p.y][p.x] + 1
        else:
            particles.remove(p)
            # for i in xrange((n - len(particles))*10):
            for i in range(2):
                particles.append(Particle(0, randint(0, N - 1), randint(-1, 2), randint(-2, 2)))
                # print(len(particles))

im = plt.imshow(box, interpolation='none', cmap=plt.get_cmap('Blues'))

def updatefig(*args):
    global box
    step()
    # box = step(box)
    im.set_array(box)
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=False)
plt.show()




    