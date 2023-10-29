import numpy as np
def fun(x,a):
    return (1.5 * x) - 0.5*a*x*x*x
def NewtonMethod(x0, f, a,delta, steps):
    init = f(x0,a)
    step = 0
    error = abs((init - x0) / init)
    while(step<steps and error > delta):
        x0 = init
        init = f(x0,a)
        error = abs((init - x0) / init)
        step +=1
    return x0, step
#print(NewtonMethod(0.2,fun,100,0.0001,10000))
#print(NewtonMethod(0.01,fun,100,0.0001,10000))
#print(NewtonMethod(0.0001,fun,100,0.0001,10000))
#print(NewtonMethod(0.0001,fun,100,0.000001,10000))
# == TASK 7 ==
def fun7(x,m):
    return x - ((x**2 - m) / 2**x)
print(NewtonMethod(0.5,fun7,0.75,0.000001,100000))
print(NewtonMethod(1,fun7,0.75,0.000001,100000))
print(NewtonMethod(1.5,fun7,0.75,0.000001,100000))
#print(NewtonMethod(0.5,fun7,0.75,0.000001,100000))
def Question7():
    #for x0 in np.linspace(0.5,1,100): #works
        #print(NewtonMethod(x0,fun7,0.75,0.000001,100000))
    #for x0 in np.linspace(2,100,1000): # breaks around 24
    #    print(str(x0) + str(NewtonMethod(x0,fun7,0.75,0.000001,100000)))
    for x0 in np.linspace(-100,0,1000): # breaks around 0
        print(str(x0)+ '. ' + str(NewtonMethod(x0,fun7,0.75,0.000001,100000)))
Question7()

