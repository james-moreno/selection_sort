from datetime import datetime
startTime = datetime.now()


def sorter(arr):
    for x in range(len(arr)-1, 0, -1):
        indexOfMax = 0
        for i in range(1, x+1):
            if arr[i]>arr[indexOfMax]:
                maxIndex = i

        temp = arr[x]
        arr[x] = arr[maxIndex]
        arr[maxIndex] = temp


a = [23, 50, 79, 28, 44, 16, 43, 11, 89, 88, 42, 65, 67, 23, 61, 43, 69, 42, 61, 10, 15, 7, 4, 65, 50, 53, 8, 13, 40, 7, 3, 96, 32, 47, 87, 17, 35, 15, 27, 87, 44, 29, 24, 89, 36, 56, 21, 46, 99, 23, 72, 99, 8, 62, 31, 4, 44, 18, 35, 51, 45, 52, 53, 40, 50, 76, 83, 29, 56, 81, 0, 85, 65, 15, 52, 47, 95, 79, 64, 20, 48, 54, 28, 49, 51, 98, 1, 65, 92, 77, 47, 64, 30, 47, 18, 51, 69, 50, 37, 21]

sorter(a)
print(a)

print(datetime.now() - startTime)
