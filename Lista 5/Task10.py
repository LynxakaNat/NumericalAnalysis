import numpy as np
import matplotlib.pyplot as plt
Ern = np.array([0.763907023, 0.543852762, 0.196247370, 0.009220859])
Ean = np.array([0.605426053, 0.055322784, 0.004819076, 0.000399783])
n = np.array([0,1,2,3])
n_r = np.linspace(0,5,100)
plt.xlim(-1,5)
n_a = np.linspace(1,5,100)
#plt.plot(n,Ern,color="black",label="Rus") # f(x) = ax + b, almost linear
# a = y1-y2 / x1 - x2
a_rus = np.mean(np.diff(Ern))
a_am = np.mean(Ean[:-1] / Ean[1:])
est_R = a_rus*n_r + Ern[0]
est_A = 1/(a_am*n_a) * Ean[1] #will only work for 1 onwards
plt.ylim(0,0.01)
plt.plot(n_r,est_R,color="purple",label="Function of Rus")
#plt.plot(n,Ean,color="blue",label="Amer")
plt.plot(n_a,est_A,color="magenta",label="Function of Amer")
plt.plot(n_r,np.zeros(len(n_r)), color="black")
plt.legend()
plt.show()
