# from collections import deque

# stack = deque()

# stack.append(1)
# stack.append('a')
# # print(stack.count(stack))
# # stack.pop()
# stack.appendleft(0)
# print(stack)



# print(f'Stack: {stack}')
# print(f'Top element: {stack[-1]}')

# print(f'Stack output as a list: {list(stack)}')

# print(f'Is Stack Empty? {len(stack) == 0}')
# print(f'Len of Stack: {len(stack)}')


# stack.pop()
# print(stack)
# stack.popleft()
# print(stack)


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\9_stack.py
# deque([0, 1, 'a'])
# Stack: deque([0, 1, 'a'])
# Top element: a
# Stack output as a list: [0, 1, 'a']
# Is Stack Empty? False
# Len of Stack: 3
# deque([0, 1])
# deque([1])



from queue import LifoQueue

# stack = LifoQueue() 
stack = LifoQueue(maxsize=5)  # Optional: Set maxsize, or use infinite size by default

print(f'Is stack full? {stack.full()}')

stack.put(5)
stack.put(10)
stack.put(20)
stack.put(30)
print(stack.qsize())

# Pop an element
print("Popped Element:", stack.get())

print(stack.qsize())

print(stack.get())  # Removes and returns the top element

print(stack.empty())  # Returns True if stack is empty, else False

print(stack.full())  # Returns True if stack is full (reaches maxsize)

print(stack.qsize())  # Returns the number of elements in the stack


try:
    print(stack.get(block=False))  # Raises an exception if empty
except:
    print("Stack is empty!")

# OR use a timeout
try:
    print(stack.get(timeout=2))  # Waits for 2 seconds, then raises an exception
except:
    print("Timeout: No element to pop!")



try:
    stack.put(40, block=False)  # Raises an exception if full
except:
    print("Stack is full!")

# OR use a timeout
try:
    stack.put(50, timeout=2)  # Waits for 2 seconds, then raises an exception
except:
    print("Timeout: Stack is full!")



while not stack.empty():
    print("Popped:", stack.get())
