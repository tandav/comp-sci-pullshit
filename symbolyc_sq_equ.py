def otric(x):
    return '-' + x

def add(a, b):
    return str(int(a) + int(b))

def sub(a, b):
    if int(a) % int(b) == 0:
        return int(a) / int(b)
    else:
        return a + '/' + b

def lineq(k, b):
    return sub(otric(b), k)

print lineq('12','24')
print add('12', '24')