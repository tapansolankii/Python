#string concatenation (how to put strings together)
print("Hello World")
def program():
    youtuber="Yashwanth"
    print(f"Subscribe to {youtuber}")
    #print("Subscribe to {}".format(youtuber))
    print("Subscribe to " + youtuber)
    #print("Subscribe to %s" % youtuber)

    adj = input("Please enter an Adjective: ")
    madlib = f"Computer programming is so {adj}"
    print(madlib)

if __name__ == "__main__":
    program()