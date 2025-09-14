import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLUMNS = 3

symbol_count = {
    "A":5,
    "B":10,
    "C":15,
    "D":10
}

def deposit():
    while True:
        deposit = input("Enter a deposit amount: $")
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit>0:
                break
            else:
                print("Enter a deposit amount greater than 0")
        else:
            print("Enter a valid number.")
    return deposit


def get_number_of_lines():
    while True:
        lines = input("Enter a valid number of lines between 1 and " +str(MAX_LINES)+ "? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a value between 1 and " +str(MAX_LINES)+ " only.")
        else:
            print("Please enter only positive natural numbers.")
    return lines


def get_bet(balance, lines) -> int:
    while True:
        while True:
            bet = input("How much would you like to bet on each line? ")
            if bet.isdigit():
                bet = int(bet)
                if bet>0:
                    break
                else:
                    print("Enter a bet amount greater than 0")
            else:
                print("Enter a valid number to bet.")
        totalBet = bet*lines
        if totalBet> balance:
            print(f"Your total bet is {totalBet}. You can only bet a max of {balance}. You are overshooting by {totalBet - balance}")
        else:
            balance = balance - totalBet
            print(f"You bet a total of {totalBet}. Your remaining balance is {balance}")
            break
    return balance

#def get_slot_machine_spin(rows, columns, symbol_count):



def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)
    balance = get_bet(balance, lines)
    print(balance)

main()