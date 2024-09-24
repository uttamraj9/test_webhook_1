# Write a function that prints a multiplication table to the screen.
# For example, the output for n=5 should look like:-

# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25

import math

def multiplication(n):
    max_number = n * n
    width = math.floor(math.log10(max_number)) + 2  
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:{width}}", end="")
        print()

# Test with n = 10
multiplication(10)

