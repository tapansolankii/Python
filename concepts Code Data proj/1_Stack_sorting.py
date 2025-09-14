# sort a stack using another temporary stack

def myStackSort():
    stack = [34, 9, 23, 6, 11]
    tempStack = []
    while stack:
        num = stack.pop()
        while tempStack and tempStack[-1]<num:
            stack.append(tempStack.pop())
        tempStack.append(num)
    for num in tempStack:
        print(num)

if __name__ == "__main__":
    myStackSort()

# Output
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python> py .\LeetCode_AllPatterns\1_Stack_sorting.py  
# 34
# 23
# 11
# 9
# 6
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python> 