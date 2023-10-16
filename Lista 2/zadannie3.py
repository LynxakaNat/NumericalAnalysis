# We have numbers 0.01xxxx x = 0 or x = 1
# We have numbers 0.1xxxx x = 0 or x = 1
# We have numbers 1.xxxx x = 0 or x = 1
import itertools

def generate_permutations(n):
    list_perm = []
    for i in range(2 ** n):
        binary_string = bin(i)[2:].zfill(n)  # Convert to binary and pad with leading zeros
        list_perm.append(binary_string)
    return list_perm

def NumberGenerator(first):
    first_half = first
    perms = generate_permutations(4)
    numbers = []
    for x in perms:
        numbers.append(first_half + x)
    return numbers

print(NumberGenerator('0.1'))

# function that transforms binary to decimal
def BinToDec(x):
    value = 0
    i = 0
    for number in x:
        if number == ".":
            pass
        else:
            value += 2 ** i * int(number)
            i = i -1
    return value
#print(BinToDec("0.11"))

for y in NumberGenerator('0.1'):
    print(BinToDec(y))

for y in NumberGenerator('1.'):
    print(BinToDec(y))

for y in NumberGenerator('0.01'):
    print(BinToDec(y))
