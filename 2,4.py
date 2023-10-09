from math import sqrt, cos,pi, log
import numpy as np

# task 2
x = 0.001
f = 4046 * ((sqrt(pow(x, 14) + 1.00) - 1.00) / (pow(x, 14)))
#print("==Task 2==")
#print(f)


# task 4

def Task4():
    y0 = 1
    y1 = -1 / 9
    for i in range(0, 51):
        yn = 80 / 9 * y1 + y0
        print(str(i) + '. ' + str(yn))
        y0 = y1
        y1 = yn

#print("==Recursion==")
#Task4()


def Task6():
    error = 1e-6
    sum = 0
    k = 0
    while abs(sum - pi) > error:
        sum += 4 * (pow(-1,k)) /(2*k+1)
        k += 1
    print(k)

#print("==Error is less than 0.000001==")
#Task6()


def Task5():
    arr = []
    Iprevious = log(2024/2023)
    arr.append(Iprevious)
    for i in range(1,21):
        Inew = 1/i - 2023*Iprevious
        Iprevious = Inew
        arr.append(Inew)
        #print(str(i) + '. '+ str(Inew))
    return arr

def Task5Odd():
    odd_list = Task5()[1::2]
    i = 1
    for x in odd_list:
        print(str(i) + '. ' +str(x))
        i += 2

def Task5Even():
    odd_list = Task5()[0::2]
    i = 0
    for x in odd_list:
        print(str(i) + '. ' +str(x))
        i += 2

def AddedOddLists(): # In + 2023 In-1 = 1/n
    even_list = Task5()[0::2]
    odd_list = Task5()[1::2]
    result = [x + (2023*y) for x, y in zip(odd_list, even_list)]
    print(result)
def AddedEvenLists(): # In + 2023 In-1 = 1/n
    even_list = Task5()[2::2]
    odd_list = Task5()[1::2]
    result = [x + (2023*y) for x, y in zip(even_list, odd_list)]
    print(result)


print('==Integrals 1 through 20==')
Task5()
print('==Odd Integrals==')
Task5Odd()
print('==Even Integrals==')
Task5Even()
AddedOddLists()
AddedEvenLists()
