# All keys have to be unique

month_full_names = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March"
    # you can either put or not put a comma for the last element
}

print(month_full_names["Jan"])
print(month_full_names.get("Jan"))
print(month_full_names.get("Jdh"))
print(month_full_names.get("Jdh", "Not a Valid Key"))

if (month_full_names.get("ggg") == None):
    print("No such month exists")

month_with_numbers={
    1:"January",
    2:"February",
}