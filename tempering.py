f0 = 100.
steps = 12
h = f0 / steps
f = [round(f0 + h*i) for i in xrange(steps + 1)]
print f