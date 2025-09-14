from pathlib import Path

# path = Path()
# # takes current directory.

# # path = Path("..\Course")
# # Can also give absolute and relative paths
# print(path.exists())


# path2 = Path("temp")
# # path2.mkdir()
# print(path2.mkdir())
# # return None
# print(path2.rmdir())
# # return None



path3 = Path()
# print(path3.glob('*'))
# # <generator object Path.glob at 0x00000207078E2BD0>
# print(path3.glob('*.*'))
# print(path3.glob('*.py'))

for file in path3.glob('*'):
    print(file)
# prints all the files