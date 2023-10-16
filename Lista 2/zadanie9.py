import math

def SequenceToPi1(x,ran):
    x1 = x
    for i in range(2,ran+1):
        seq = pow(2,(i-1)) * math.sqrt(2*(1 - math.sqrt(1 - ((x1/2**(i-1))**2))))
        x1 = seq
        print(str(i) + '. ' + str(seq - math.pi)) # we are experiencing a significant digit loss a tthe 15th

SequenceToPi1(2,50)

def SeqToPi(x,ran):
    x1 = x
    for i in range(2,ran+1):
        seq = math.sqrt((2* (x1 ** 2))/ (1+ math.sqrt(1 - (x1/2** (i -1))** 2)))
        x1 = seq
        print(seq)
        print(str(i) + '. ' + str(seq - math.pi))
SeqToPi(2,50)
