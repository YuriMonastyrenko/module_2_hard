import random
from random import randint

first_number = random.randint(3, 20)
key_number = ""

for i in range(1, first_number):
    for j in range(i+1, first_number):
        if first_number % (i + j) == 0:
            key_number = key_number + str(i) + str(j)
print(first_number, "-", key_number)



