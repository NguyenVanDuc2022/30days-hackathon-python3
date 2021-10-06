"""
Day 11 - Given 6x6 2D array, A.
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
--- Nguyen Van Duc --- 
"""

if __name__ == "__main__":
    arr = []
    maximum = -99
    for i in range(6):
        tmp = [int(x) for x in str(input("Enter your row {}: ".format(i+1))).split(" ")]
        arr.append(tmp)

    for i in range(6):
        for j in range(6):
            if j + 2 < 6 and i + 2 < 6:
                result = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][
                    j + 1] + arr[i + 2][j + 2]
                if result > maximum:
                    maximum = result

    print("The maximum is: ", maximum)
