#  f(x) = x - 0.49
#  a0 = 0
#  b0 = 0
import math
def singleBisect(a,b,f): #we are assuming the lecture definition
    middle = (a + b) / 2
    if (f(middle) > 0):
        a,b = a, middle
    elif (f(middle) < 0):
        a,b = middle,b
    return [a,b, middle]
def fun(x):
    F = x - 0.49
    return F
def bisect(a0,b0,f,step):
    zero = 0.49
    for iter in range(0,step):
        bis = singleBisect(a0,b0,f)
        a0 = bis[0]
        b0 = bis[1]
        middle = bis[2]
        print("Our error is", str(abs(middle - zero)))
bisect(0,1,fun,6)
# TASK 4
# ranges [-3,0] + [0,100]
def fun1(x):
    F = x**4 - math.log(x+4)
    return F
def BisectTask4(a0,b0,f):
    err = abs((b0 + a0) / 2)
    while(err > 10**-8):
        err = err /2 #from theory
        bis = singleBisect(a0,b0,f)
        a0 = bis[0]
        b0 = bis[1]
        middle = bis[2]
    return middle

print(BisectTask4(0,-3,fun1)) # we switch it around bc in our
#assump from the lecture f(a) <0, f(b) >0
print(BisectTask4(0,100,fun1))
