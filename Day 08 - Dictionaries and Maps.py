"""
Day 08 - Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone
numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print
the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found,
print Not found instead.
--- Nguyen Van Duc ---
"""
n = int(input("Enter the value N: "))
d = {}
for i in range(n):
    x = input("Enter data: ").split()
    d[x[0]] = x[1]
while True:
    try:
        name = input("Enter value you want: ")
        if name in d:
            print(name + "=" + d[name])
        else:
            print("Not found!")
    except EOFError:
        break
