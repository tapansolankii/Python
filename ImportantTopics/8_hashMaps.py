# hash_map = {}

# hash_map['name'] = 'Yashwanth'
# hash_map['age'] = 25
# hash_map['role'] = 'Software Engineer'

# print(hash_map)
# print(hash_map['name'])
# print(hash_map.get('nameeeee', 'Not Found!!'))


# hash_map['age'] = 35
# hash_map.pop('role')
# print(hash_map)



# Iterating through keys
# for key in hash_map:
#     print(key, hash_map[key])

# # Iterating through key-value pairs
# for key, value in hash_map.items():
#     print(key, value)


# if 'name' in hash_map:
#     print('Key exists!')



# # Get all keys
# print(hash_map.keys())

# # Get all values
# print(hash_map.values())

# # Get all key-value pairs
# print(hash_map.items())

# # Default value if key not present
# print(hash_map.get('address', 'N/A'))



# ////////////////////////////////////////


sentence = "this is a test this is only a test"

# letter_count = {}

# for word in sentence:
#     letter_count[word] = letter_count.get(word, 0) + 1

# print(letter_count)
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\8_hashMaps.py
# {'t': 6, 'h': 2, 'i': 4, 's': 6, ' ': 8, 'a': 2, 'e': 2, 'o': 1, 'n': 1, 'l': 1, 'y': 1}



# words
# words = sentence.split()
# print(words)

# word_count = {}

# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# print(word_count)
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\8_hashMaps.py
# ['this', 'is', 'a', 'test', 'this', 'is', 'only', 'a', 'test']
# {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> 







# ////////////////////////////////////////////////////////
# Hash Map finding the target = 2 numbers sum in an array.


# def two_sum(nums, target):
#     hash_map = {}  # To store numbers and their indices
#     print(hash_map)
    
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in hash_map:
#             return [hash_map[complement], i]
#         hash_map[num] = i
#     print(hash_map)
#     return []

# # Example
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))




# def find_total(arr:list[int], total:int) -> list[int]:
#     hash_map = {}
#     for i, num in enumerate(arr):
#         complement = total-num
#         if complement in hash_map:
#             return [hash_map[complement], i]
#         hash_map[num] = i
#     return []



# arr = [2,7,11,15,8,3]
# total = 23
# result = find_total(arr, total)
# print(result)

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\8_hashMaps.py
# [3, 4]






# ///////////////////////////////////////////////////////


# from collections import defaultdict

# def group_anagrams(words):
#     hash_map = defaultdict(list)

#     for word in words:
#         # Use sorted word as key
#         sorted_word = ''.join(sorted(word))
#         hash_map[sorted_word].append(word)
#     print(hash_map)
#     print(hash_map.values())
#     return list(hash_map.values())

# # Example
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(words))





# Using a list because we have to return a lists inside dict.

from collections import defaultdict

def group_anagrams(words:list[str]) -> list:
    hash_map = defaultdict(list)

    for word in words:
        sorted_word = ''.join(sorted(word))
        hash_map[sorted_word].append(word)
    print(hash_map)
    print(hash_map.values())
    return list(hash_map.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))

# Output
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\8_hashMaps.py
# defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})
# dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]