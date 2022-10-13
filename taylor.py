# *** Forma iterativa ***
# import math

# x = 3
# suma = 0
# for i in range(100):
#     actual = (x**i) / math.factorial(i)
#     suma = suma + actual

# print(suma)
# print(math.exp(x))

# Bono: Factorial propio
def factorial(n):
    if n < 1:
        return 1

    return n * factorial(n - 1)


# # Incremental
# # n = 50
# def exp_taylor(x, i=0):
#     actual = (x**i) / factorial(i)
#     # Caso base
#     if i == 50:
#         return actual

#     return actual + exp_taylor(x, i + 1)


# Decremental
# n = 50
def exp_taylor_dec(x, i=50):

    actual = (x**i) / factorial(i)
    # Caso base
    if i == 0:
        return actual

    return actual + exp_taylor_dec(x, i - 1)


# print(exp_taylor_dec(1, 50))
# %%
def factorial(n):
    if n < 1:
        return 1

    return n * factorial(n - 1)


# # Incremental
# # n = 50
# def exp_taylor(x, i=0):
#     actual = (x**i) / factorial(i)
#     # Caso base
#     if i == 50:
#         return actual

#     return actual + exp_taylor(x, i + 1)


# Decremental
# n = 50
def exp_taylor_dec(x, i=50):

    actual = (x**i) / factorial(i)
    # Caso base
    if i == 0:
        return actual

    return actual + exp_taylor_dec(x, i - 1)


import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 50, 1)

y = []
for i in range(50):
    y.append(exp_taylor_dec(2, i))

plt.plot(x, y, ".r")
plt.xlabel("x")
plt.ylabel("e^x")
# %%
