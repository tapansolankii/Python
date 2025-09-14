# Question 3: Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid. An input string is valid if:

# Open brackets are closed by the same type of brackets.
# Open brackets are closed in the correct order.

from collections import deque

def is_valid_parentheses(s):
    q = deque()
    for char in s:
        if char in "({[":
            q.append(char)
        else:
            x = q.pop()
            if char==")" and x=="(":
                continue
            elif char=="}" and x=="{":
                continue
            elif char=="]" and x=="[":
                continue
            else:
                return False
    return True


# Example:
s = "({[]})"
print(is_valid_parentheses(s))  # Output: True
s = "(]"
print(is_valid_parentheses(s))  # Output: False

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\3_bracketsOrder.py
# True
# False
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice>








# ChatGPT
# Your implementation is close but needs some adjustments to handle 
# edge cases where the input string does not have balanced parentheses. 
# Specifically:
# Empty Stack Check: The code assumes that q.pop() will always work, 
# but if the stack is empty when calling pop(), it will throw an error. 
# This can happen when there are unmatched closing brackets.

# Final Stack Check: After processing the string, if the stack q is not 
# empty, it means there are unmatched opening brackets.

# def is_valid_parentheses(s):
#     q = deque()
#     for char in s:
#         if char in "({[":
#             q.append(char)  # Push opening brackets onto the stack
#         else:
#             if not q:  # Check if the stack is empty before popping
#                 return False
#             x = q.pop()
#             if char == ")" and x != "(":
#                 return False
#             elif char == "}" and x != "{":
#                 return False
#             elif char == "]" and x != "[":
#                 return False
#     # After processing, ensure the stack is empty
#     return len(q) == 0