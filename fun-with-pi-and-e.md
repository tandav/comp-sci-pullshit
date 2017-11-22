# Fun with π and e
```py
>>> from math import e, pi

# e^π - π ≈ 20
>>> e**pi - pi
19.99909997918947

# √2 + √3 ≈ π
>>> 2**(1/2) + 3**(1/2)
3.1462643699419726

# ∛2 + ∛3 ≈ e 
>>> 2**(1/3) + 3**(1/3)
2.7021706202022813

# pi^4 + pi^5 ≈ e^6
>>> abs(pi**4 + pi**5 - e**6)
1.7673451168320753e-05
```

----------------------------------------

Take 100k digits of pi in binary:

`pi = 11.001001000011111101...`

Move from left to right on x-axis and plot line following algorithm:

```py
for digit in pi:
    if digit == 0: one_pixel_down()
    if digit == 1: one_pixel_up()
```
You'll get this plot:

![pi-binary](https://cloud.githubusercontent.com/assets/5549677/20464607/481212dc-af5b-11e6-99a4-1904672f90a5.png )
