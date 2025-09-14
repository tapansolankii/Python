# Question 4: Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a single sorted 
# list. The list should be made by splicing together the nodes of 
# the two lists.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(l1: ListNode, l2: ListNode)-> ListNode:
    dummy = ListNode()
    current = dummy
    while l1 and l2:
        if l1.val<l2.val:
            current.next = l1
            l1 = l1.next
        elif l2.val<=l1.val:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    
    return dummy



# Can initialize linked Lists in the below 2 ways.
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

# l3 = ListNode(1)
# l4 = ListNode(2)
# l3.next = l4
# print(l3.next.val)

result = merge_two_lists(l1, l2)
while result:
    print(result.val, end=" -> ")
    result = result.next





# BIN
# # Example:
# l1 = [1,2,4]
# l2 = [1,3,4]
# merge_two_lists(l1, l2)
# # Output: [1,1,2,3,4,4]


# ChatGPT program
# from typing import List
# import heapq

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def merge_two_lists(l1, l2):
#     # Initialize a dummy node to simplify list merging
#     dummy = ListNode()
#     current = dummy

#     # Merge the two lists while both have nodes
#     while l1 and l2:
#         if l1.val < l2.val:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#         current = current.next

#     # Attach the remaining nodes of l1 or l2
#     if l1:
#         current.next = l1
#     if l2:
#         current.next = l2

#     return dummy.next

# # Example Usage:
# # l1 = ListNode(1, ListNode(2, ListNode(4)))
# # l2 = ListNode(1, ListNode(3, ListNode(4)))
# # result = merge_two_lists(l1, l2)
# # while result:
# #     print(result.val, end=" -> ")
# #     result = result.next
