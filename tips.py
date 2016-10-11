import webbrowser
webbrowser.open('www.youtube.com')

#float in for
def frange(x, y, jump):
  while x < y:
    yield x
    x += jump
for i in frange(0, 5, 0.1):
    print(i)

# 2 - dim array / exist drugie varianty sozdaniya
Matrix = [[0 for x in range(m)] for x in range(n)] # 0-s

M= [[0 for x in range(7)] for x in range(7)] 
for i in range(7):
    for j in range(7):
        M[i][j] = i+j

x = xrange(10)
y = map(lambda z: z*z, x)
print y

# в функции можно юзать глобальные переменные, но если хочешь изменять, то нужно писать
x = 1
y = 2
def f():
  global x, y
  x = 2
  y = 3
