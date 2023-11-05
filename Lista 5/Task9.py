import numpy as np
import math
def Ord(x0, f, steps):
    init = f(x0) # <- Olver
    step = 0
    arr_of_x = []
    while(step<steps):
        x0 = init
        init = f(x0)
        arr_of_x.append(init)
        step +=1
    return arr_of_x

def fun(x): # (x - 2)(x + 1) = x**2 -x -2 = 2x - 1 = 2
    F = x - (((x-2)*(x+1))/(2*x -1 )) - 0.5 *(2/(2*x -1 )) * (((x-2)*(x+1))/(2*x -1 ))**2
    return F

arrx = Ord(200000,fun,100)
arry = Ord(-2000,fun,100)
print(arry)
def alpha(arrr):
    x_list = np.array(arrr)
    diff_1 = x_list[3:] - x_list[2:-1] # xn+1 - xn
    diff_2 = x_list[2:-1] - x_list[1:-2] # xn - xn-1
    diff_3 = x_list[1:-2] - x_list[0:-3] # xn-1 - xn-2
    p = (np.log(abs((diff_1 / diff_2)))) / (np.log(abs(diff_2/diff_3)))
    mask_p = np.isnan(p) + np.isinf(p)
    p = p[~mask_p]
    return p
print(alpha(arrx))
print(alpha(arry))
