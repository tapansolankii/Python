def match_function(y: int):
    match y:
        case 4:
            print(f"{y} is 4")
        case _:
            print(f"{y} is not 4")


x = 6
match_function(x)