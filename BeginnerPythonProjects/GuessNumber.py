#https://docs.python.org/3/library/random.html
import random

def guess(x):
    random_number = random.randint(1,x)
    print(random_number)
    y = -1
    while(random_number != y):
        y = int(input("Enter a Number: "))
        if y != random_number:
            print("Schade! Try again please.")
    print(f"Yayy you guessed that the number is {random_number} correctly.")

def computerGuess():
    x = 25
    rand = random.randint(1,100)
    print(rand)
    while x != rand:
        if x < rand:
            rand -= 1
            print(rand)
        else:
            rand += 1
            print(rand)
    print(f"Yay! You guessed {x} to be {rand} correctly.")

if __name__ == "__main__":
    #xx = int(input("Enter a number range to start from to this range: "))
    #guess(xx)
    computerGuess()

#guess(10)