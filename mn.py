from termcolor import colored
import sys

# def inmand(c):
#     z = c
#     for i in xrange(21):
#         z = z * z + c
#         if z.real * z.real + z.imag * z.imag > 4:
#             return False
#     return True

def inmand(c):
    z = c
    for i in xrange(21):
        z = z * z + c
        if z.real * z.real + z.imag * z.imag > 4:
            return i
    return 20


def color(n):
    # colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'white']
    colors = ['grey','red','yellow','green','cyan','blue','magenta','white']
    j = 0
    for i in xrange(21):
        if i % 3 == 0:
            cl = colors[j]
            j += 1
        if i == n:
            return cl

# for c in colors:
#     print colored('hello', c)


# print colored('*','red'),
# sys.stdout.softspace=False
# print '%s' % ('*')

m = 70
n = 170
dx = 3. / n
dy = 2. / m

for j in xrange(m):
    for i in xrange(n):
        c = complex(-2 + dx * i, -1 + dy * j)
        print colored('*', color(inmand(c))),
        sys.stdout.softspace=False

        # if inmand(c):
        #     print colored('*','red'),
        #     sys.stdout.softspace=False
        # else:
        #     print colored(' ','red'),
        #     sys.stdout.softspace=False
    print ''