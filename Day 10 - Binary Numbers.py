"""
Day 10 - Given a base-10 integer, n, convert it to binary (base-2). Then find and  print the base-10 integer denoting
the maximum number of consecutive 1's in n's binary representation.
--- Nguyen Van Duc ---
"""
if __name__ == "__main__":
    n = int(input("Enter value of n: "))
    numbers = str(bin(n)[2:]).split('0')
    lengths = [len(num) for num in numbers]
    print(max(lengths))
