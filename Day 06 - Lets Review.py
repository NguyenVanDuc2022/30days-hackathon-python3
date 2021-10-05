"""
Day 06 - given a string, S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters
as 2 space-separated strings on a single line.
Note: 0 is considered to be an even index.
--- Nguyen Van Duc ---
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT.
t = int(input("Enter your value: "))
for i in range(t):
    s = str(input("Enter your string: "))
    print(s[::2], s[1::2])
