#class A:
#    def g(self):
#         return 'hello world'
#         
#class Point A:
#    a = 0
#    b = 0
#    c = 0
#    data = 42
#    def method(self): pass
from random import randint
#randint(2,9)
class My:
    x = None
    y = None
    w = None
    wo = None
    t = None

S = []
for i in range(20):         #robit norm
    S.append(My())
    S[i].w = randint(0, 10)


####### Massiv ekzemplyarov klassa:
class T:
    x = None
    y = None
    w = None
    wo = None
    t = None

D = []
for i in range(5):
    D.append(T())
    D[i].x = i**2
print(D[3].x)
