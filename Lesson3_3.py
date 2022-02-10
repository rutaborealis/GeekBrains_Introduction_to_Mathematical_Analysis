# Lesson 1
# Task 2
import math

ACC = 0.0000001


def f(n):
    return n / math.factorial(n) ** (1 / n)


i = 2
while f(i) - f(i - 1) > 0.001:
    i = i + 1
    # print(i)
print(f(i))
