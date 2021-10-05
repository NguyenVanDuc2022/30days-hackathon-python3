"""
Day 03 - Given an integer, n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
Complete the stub code provided in your editor to print whether or not is weird.
--- Nguyen Van Duc ---
"""
# !/bin/python3

if __name__ == '__main__':
    N = int(input("Enter number N: "))
    if N % 2 != 0:
        print("Weird")
    elif N % 2 == 0 and N in range(1, 6):
        print("Not Weird")
    elif N % 2 == 0 and N in range(5, 21):
        print("Weird")
    elif N % 2 == 0 and N > 20:
        print("Not Weird")
