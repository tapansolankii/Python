def binarySearch(arr: list[int], num: int) -> int:
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (right+left)//2
        if arr[mid]==num:
            return mid
        elif arr[mid]<num:
            left=mid+1
        else:
            right=mid-1
    return -1


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def main():
    arr = [1,3,5,7,9,11,13,15]
    result = binarySearch(arr,5)
    print(result)
    result = linear_search(arr,9)
    print(result)
    

if __name__=="__main__":
    main()



# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\5_binarySearch.py
# 2
# 4
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> 