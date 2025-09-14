def smallestArray(array, target):
    start = 0
    currentSum = 0
    minWindowSize = float('inf')  # Initialize to a very large value
    for end in range(len(array)):
        currentSum+=array[end]
        while currentSum>=target:
            minWindowSize = min(minWindowSize, end-start+1)
            currentSum-=array[start]
            start+=1
    # return windowSize
    return minWindowSize if minWindowSize != float('inf') else 0

array = [3,6,7,3,9,6,0,4]
target = 10
output = smallestArray(array, target)
print(output)