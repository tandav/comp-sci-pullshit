import numpy as np
import matplotlib.pyplot as plt
# from pylab import imshow, show
import matplotlib.animation as animation



fig = plt.figure()

N = 40 # World Size
nutrients = np.random.uniform(0., 1., [N, N])


epicentr =  list(np.unravel_index(nutrients.argmax(), nutrients.shape))
nutrients[epicentr[0], epicentr[1]] = 0
pets = np.zeros((N, N))
pets[epicentr[0], epicentr[1]] = pets[epicentr[0]][epicentr[1]]
pets[N/2][N/2] = 20

for i in range(1, pets.shape[0] - 1):
    pets[i][0] = 200.


def delta(arr):
    global epicentr, pets
    if epicentr[0] < N - 1 and epicentr[1] < N - 1:
        arr[epicentr[0]+1][epicentr[1]+1] = arr[epicentr[0]][epicentr[1]]
        arr[epicentr[0]][epicentr[1]] = 0
        epicentr[0]+=1
        epicentr[1]+=1
# imshow(nutrients, interpolation='nearest', cmap='BuGn')
# imshow(pets, alpha=.5, interpolation='nearest', cmap='hot_r')

# imshow(nutrients, cmap='BuGn')
# show()
# im = plt.imshow(arr, interpolation='nearest', cmap=plt.get_cmap('coolwarm'))
# im1 = plt.imshow(nutrients, interpolation='nearest', cmap='BuGn')
im2 = plt.imshow(pets, alpha=.5, interpolation='nearest', cmap='hot_r')
def updatefig(*args):
    global nutrients, pets
    # arr = nakal(arr)
    pets = delta(pets)
    # nutrients = delta(nutrients)
    # im1.set_array(nutrients)
    im2.set_data(pets)
    # return im1,

ani = animation.FuncAnimation(fig, updatefig, interval=1, blit=False)
plt.show()