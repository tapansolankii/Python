def maxSum(array, length):
    arraySize = len(array)
    if (arraySize<length):
        return -1
    maxSum = 0
    windowSum = 0
    for i in range(length):
        windowSum+=array[i]
    maxSum = windowSum
    for i in range(length, arraySize):
        windowSum = windowSum + array[i] - array[i-length]
        maxSum = max(maxSum, windowSum)
    return maxSum

array = [4,1,3,7,8,5,0,3]
output = maxSum(array, 3)
print(output)