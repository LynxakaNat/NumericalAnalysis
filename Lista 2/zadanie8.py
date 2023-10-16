import math
import numpy as np
def Taylor1():
    for x in range(11,21):
        f = 14 * (1/2*(17 ** 2) - (1/24 * (17 ** 4) * ((10**(-x))**2))) # we are not accurate enough in our approximation
        print(f)
Taylor1()

def Taylor2():
    for x in np.arange(1,21,dtype=np.longdouble):
        f = 14 * (1/2*(17 ** 2) - (1/24 * (17 ** 4) * ((10**(-x))**2)) + (1/720 * (17 ** 6) * ((10**(-x))**4)))
        print(f-2023) # not enough precision still the reason its exactly 2023 because we would need a 44bit mantissa
        #even be able to write the first term precisely
Taylor2()
