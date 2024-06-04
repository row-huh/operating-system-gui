import sys

sum = 0
with open(sys.argv[1], 'r') as f:
    for i in range(10):
        sum += i


print(f"The sum of the numbers is : {sum}")