# lists with []

# friends = ["Kevin", 2, True, "Anusha"]
# print(friends[1:3])
# print(friends[-1])
# print(friends)
# print(friends[1:])
# print(friends[-3:])


# friends[0] = "Yashwanth"
# print(friends)
# friends[0] = True
# print(friends)

friends = ["Anusha", "Yashwanth", "Us"]
numbers = [24, 2, 4]
friends.append("Anu")
friends.append(numbers)
print(friends)
print(friends[4][2])
# friends.count()
friends.insert(1, "Yash")
print(friends)
friends.remove("Anu")
print(friends)
# friends.pop() removes the last element
# friends.clear()

friends.index("Us")
# friends.index("ergshrtgrt") will give an error
friends.append("Anusha")
print(friends.count("Anusha"))

friends.sort(key=len)
print(friends)
# friends.sort() won't work since there are both list and str inside friends list

friends.reverse()
print(friends)

friends2 = friends.copy()
friends2.pop()
print(friends)
print(friends2)