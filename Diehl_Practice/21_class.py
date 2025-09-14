class Person:
    species = "Homosapiens"

    @staticmethod
    def add(a, b):
        return a+b

    @classmethod
    def set_species(cls, s):
        cls.species = s

print(Person.species)
Person.set_species("Homofuturus")
print(Person.species)
print(Person.add(4,5))


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\21_class.py
# Homosapiens
# Homofuturus
# 9
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 