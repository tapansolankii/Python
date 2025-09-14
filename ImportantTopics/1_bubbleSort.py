print("Hello World!")

def bubbleSort(arr) -> list:
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# arr = [25, 13,314,9,56,354,23,6,8,4]
arr = [25, 6,8,4]

sortedArray = bubbleSort(arr)
print(sortedArray)