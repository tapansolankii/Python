import random

# for i in range(3):
#     print(random.random())

# for i in range(3):
#     print(random.randint(10, 20))

# names = ["A", "B", "C"]
# leader = random.choice(names)
# print(leader)

# Output
# 0.4610685901350293
# 0.5225127508407427
# 0.667593871752641
# 19
# 14
# 15
# B


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second
        # return (first, second)
        # Both the above are same - 
        # python knows both are tuples (while returning only)


dice = Dice()
print(dice.roll())


# Output
# (4, 3)