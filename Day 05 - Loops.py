"""
Day 05 - Given an integer, n, print its first 10 multiples. Each multiple n x i (where 1 <= i <= 10) should be printed
on a new line in the form: n x i = result.
--- Nguyen Van Duc ---
"""
# !/bin/python3
import math
import os
import random
import re
import sys

if __name__ == "__main__":
    n = int(input("Enter n:"))
    for i in range(1, 10):
        print(n, "x", i, "=", n * i)
