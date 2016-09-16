def k23(x, y):
    w = []
    w.append(4*x+y)
    w.append(3*y+x)
    return w

optima = [0, 0]
opt_w = 1000

for x in range(30):
    for y in range(30):
        A = [4*x + y, 3*y + x]
        if A[0] >= 90 and A[1] >=80:
            waste = 2*A[0] + 3*A[1]#|90 - A[0] + 80 - A[1]
            if waste < opt_w:
                optima = A
                opt_w = waste
                XY = [x, y] 
                print(opt_w, A, XY)   
# print(XY)