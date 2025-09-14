def insertionSort(arr: list) -> list:
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

arr = arr = [25, 6,8,4]

sortedArray = insertionSort(arr)
print(sortedArray)



# Cleaner
# def insertionSort(arr: list) -> list:
#     for i in range(1, len(arr)):
#         j = i
#         while j > 0 and arr[j - 1] > arr[j]:
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap directly
#             j -= 1
#     return arr




# def insertion(arr: list[int]):
#     for i in range(1,len(arr)):
#         j=i-1
#         key = arr[i]
#         while(j>=0 and arr[j]>key):
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     return arr





# practice
def insertion3(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
