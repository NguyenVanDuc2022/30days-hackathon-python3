"""
Day 07 - Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated
numbers.
Input format:
- The first line contains an integer, N (the size of our array).
- The second line contains N space-separated integers describing array A's elements.

Constraints:
- 1 <= N <= 1000
- 1 <= Ai <= 10000, where Ai is the ith integer in the array.

Output format:
- Print the elements of array A in reverse order as a single line of space-separated numbers.
--- Nguyen Van Duc ---
"""

if __name__ == "__main__":
    n = int(input("Enter N: "))
    arr = list(map(int, input("Enter your string: ").rstrip().split(" ")))
    print(*arr[::-1], sep=" ")
