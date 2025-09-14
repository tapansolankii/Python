# put smaller elements in left and bigger elements
# in right based on pivot.

def quickSort(arr: list[int]) -> list[int]:
    if len(arr)<=1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x<=pivot]
    right = [x for x in arr[:-1] if x>pivot]
    return quickSort(left) + [pivot] + quickSort(right)

arr = [3,1325,82,5,92,35,24]
sortedArr = quickSort(arr)
print(sortedArr)




def quick(arr: list[int]) -> list[int]:
    if len(arr)<=1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x<=pivot]
    right = [x for x in arr[:-1] if x>pivot]
    return quick(left) + [pivot] + quick(right)