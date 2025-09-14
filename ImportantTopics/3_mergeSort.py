# first break into smallest arrays - size 1 or 2.
# Then sort and merge together.

def mergeSort(arr: list[int]) -> list[int]:
    if(len(arr)<=1):
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    i = j = 0
    result = []
    while(i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr = [3, 1325, 82, 5, 92, 35, 24]
sortedArr = mergeSort(arr)
print(sortedArr)



def mergesort2(arr: list[int]) -> list[int]:
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = mergesort2(arr[:mid])
    right = mergesort2(arr[mid:])
    return merge2(left, right)


def merge2(left: list[int], right: list[int]) -> list[int]:
    i = j = 0
    result = []
    while (i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result