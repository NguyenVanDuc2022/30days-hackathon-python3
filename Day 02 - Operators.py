"""
Day 02 - Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded results!
--- Nguyen Van Duc ---
"""
# !/bin/python
import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    # Write your calculation code here
    tip = (tip_percent / 100) * meal_cost  # calculate tip
    tax = (tax_percent / 100) * meal_cost  # calculate tax

    # cast the result of the rounding operation to an int and save it as total_cost
    total_cost = round(meal_cost + tip + tax)
    print(total_cost)


if __name__ == '__main__':
    meal_cost = float(input("Enter cost: "))
    tip_percent = int(input("Enter tip percent: "))
    tax_percent = int(input("Enter tax percent: "))
    solve(meal_cost, tip_percent, tax_percent)
