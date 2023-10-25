import math
def Function1(x):
    f = 1 / (x**3 + math.sqrt(x**6 + 2023**2))
    return f

#for i in range(1000, 2000):
  #  print(str(i)+ '. ' + str(Function1(-i) - Function1(-(i-1))))
# we get issues bc of floating point representation
# minus terms go to infinity, plus terms go to zero
def Function1fix(x):
    f = (x ** 3 - math.sqrt(x**6 + 2023**2)) / -2023
    return f
print(Function1fix(-2000))


def Fun2(x):
    F = math.log2(x) - 2
    return F
def Fun2Tay(x):
    F = (x-4) / (4*math.log(2))
    return F

print(Fun2(3.9999))
print(Fun2Tay(3.9999))

def Fun3(x):
    F = (-x + math.atan(x)) / x**3
    return F
print(Fun3(0.1))


# ==== TASK 2 ====
def Normal(a,b,c):
    delta = b**2 - 4*a*c
    if delta>0:
        x1 = -b + math.sqrt(delta) / 2*a
        x2 = -b - math.sqrt(delta) / 2*a
        return x1,x2
    else:
        return "we cry"

print(Normal(2**-30, 1000.0, 2**-30))

def Improved(a,b,c):
    delta = b**2 - 4*a*c
    if b > 0:
        x1 = (-(b + math.sqrt(delta))) / 2*a
    if b< 0:
        x1 = (-(b - math.sqrt(delta))) / 2*a
    x2 = c / (a * x1)
    return x1,x2
print(Improved(2**-30, 1000.0, 2**-30))
