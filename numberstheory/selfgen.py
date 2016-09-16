import matplotlib.pyplot as plt

def listing(start, n):
    arr = [[start], [sum([int(d) for d in str(start)])]]
    for x in xrange(n):
        nexte = sum([int(d) for d in str(start)]) + start
        # print sum([int(d) for d in str(start)])
        arr[0].append(nexte)
        arr[1].append(sum([int(d) for d in str(start)]))
        start = nexte
    return arr

# maxes = []

# for x in xrange(1000):
#     maxes.append(listing(x, 100)[-1])
# # print maxes.index(max(maxes))
# # y = listing(108, 100)
# # print y
# plt.plot(maxes,'g-')
# # plt.axis('equal')
# plt.show()
a = listing(22, 1000)
plt.plot(a[0],a[1],'.-')
# plt.axis('equal')
plt.show()