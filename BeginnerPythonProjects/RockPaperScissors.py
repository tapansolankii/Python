import random

def game():
    print("Hey there! We are playing Rock Paper and Scissors!")
    while(1):
        user = input("Enter your input as 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()
        choices = ['r', 'p', 's']
        if user not in choices:
            print("Please enter the correct value.")
        else:
            break
    computer = random.choice(['r','p','s'])
    i=1
    while(i):
        if user == computer:
            print(f"Both entered the same choice. The game is a draw.")
        elif user == 'r' and computer == 'p':
            print(f"The computer chose Paper and you chose Rock. Computer wins!")
        elif user == 'p' and computer == 'r':
            print(f"The computer chose Rock and you chose Paper. User wins!")
        elif user == 'r' and computer == 's':
            print(f"The computer chose Scissors and you chose Rock. User wins!")
        elif user == 's' and computer == 'r':
            print(f"The computer chose Rock and you chose Scissors. Computer wins!")
        elif user == 'p' and computer == 's':
            print(f"The computer chose Scissors and you chose Paper. Computer wins!")
        elif user == 's' and computer == 'p':
            print(f"The computer chose Paper and you chose Scissors. User wins!")
        
        choice = ['y','n']
        p=1
        while(p):
            j = input("Would you like to play again? If yes, type 'y'. Else, type 'n': ").lower()
            if j == 'y':
                while(1):
                    user = input("Enter your input as 'r' for rock, 'p' for paper, or 's' for scissors: ").lower()
                    choices = ['r', 'p', 's']
                    if user not in choices:
                        print("Please enter the correct value. ")
                    else:
                        computer = random.choice(['r','p','s'])
                        p=0
                        break
            elif j=='n':
                print("Thank you! Have a wonderful day!")
                i=0
                break
            elif j not in choice:
                print("Please enter the correct value. ")
            
if __name__ == "__main__":
    game()