"""
Day 09 - Write a factorial function that takes a positive integer, N as a parameter and prints the result of N!
(N factorial).
--- Nguyen Van Duc ---
"""
import os


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    N = int(input("Enter value of N: "))
    result = factorial(N)
    print(N, "! =", result)

