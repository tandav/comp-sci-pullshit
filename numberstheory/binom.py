def binadd(a, b):
    if a == b:
        return 0
    else:
        return 1

# def binom(n, k):
#     if n < k:
#         print "error"
#         return
#     if n == k or k == 0:
#         return 1
#     else:
#         return binom(n - 1, k - 1) + binom(n - 1, k) 

def dr(n):
    res = n % 9
    if res == 0:
        return 9
    else:
        return res

def binom(n, k):
    if n < k:
        print "error"
        return
    if n == k or k == 0:
        return 1
    else:
        return binadd(binom(n - 1, k - 1), binom(n - 1, k))
n = 100
for i in xrange(n):
    for j in xrange(i + 1):
        print binom(i, j),
    print '\n',
