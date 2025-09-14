class PointClass:
    def move(self):
        print(f'move')
    def draw(self):
        print(f'draw')

point1 = PointClass()
point1.move()

point1.x = 10
print(point1.x)

# Can randomly add a new variable without
# it being a attribute in the class (x)