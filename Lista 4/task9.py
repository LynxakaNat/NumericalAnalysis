# == TASK 9 ==
# f(x) = a
def NewtonMethodWithR(x0, f, a,r,delta, steps):
    init = f(x0,a,r)
    step = 0
    error = abs((init - x0) / init)
    while(step<steps and error > delta):
        x0 = init
        init = f(x0,a,r)
        error = abs((init - x0) / init)
        step +=1
    return x0, step
def funA(x,a,r):
    return x - ((x**r - a) / (r*x**(r-1)))
print(NewtonMethodWithR(4,funA,12,50,0.0001,10000))
print(NewtonMethodWithR(50,funA,12,50,0.0001,10000))
print(NewtonMethodWithR(500,funA,12,50,0.0001,10000))
print(NewtonMethodWithR(50000,funA,12,50,0.0001,10000))
def funB(x,a,r):
    return x -((x**r - a*x) / (r*x**(r-1) - a))
print(NewtonMethodWithR(4,funB,1,50,0.0001,10000))
print(NewtonMethodWithR(1,funB,12,50,0.0001,10000)) # nie dziala dla <0
print(NewtonMethodWithR(1,funB,12,51,0.0001,10000))
def funC(x,a,r):
    return x - ((x**r - a*x**2 - a*x) / (r*x**(r-1) - 2*a*x - a*x))
print(NewtonMethodWithR(1,funC,1,51,0.0001,10000))
print(NewtonMethodWithR(2,funC,1,52,0.0001,10000))
