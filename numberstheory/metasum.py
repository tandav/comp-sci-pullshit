def meta(a, b, n):
    if n == 0:
        return a + b
    else:
        res = meta(a, a, n - 1)
        for x in xrange(1, b - 1):
            res = meta(res, a, n - 1)
        return res


def metam(a, b, n):
    if n == 0:
        return a + b
    else:
        res = metam(a, a, n + 1)
        for x in xrange(1, b - 1):
            res = metam(res, a, n + 1)
        return res

print meta(5, 0, 2)