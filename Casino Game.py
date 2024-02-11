import random
import time
max_num = 100
min_bet = 10
balance=0
def deposit():
    while True:
        amount = input("What would you like to deposit?The deposit should be at least more than 10. :")
        if amount.isdigit():
            amount = int(amount)
            if amount > 10:
                break
            else:
                print("Amount must be greater than ten")
        else:
            print('Please enter a number')
    return amount

def choose_the_bet():
    while True:
        bet = input("What would you like to bet? The bet should be at least " + str(min_bet) + ": ")
        if bet.isdigit():
            bet = int(bet)
            if bet >= min_bet:
                break
            elif bet<=balance:
                break
            elif balance==0:
                print("You have insufficient balance. This ends the game.")
            else:
                print("Enter the bet amount more than or equal to " + str(min_bet))
        else:
            print('Please enter a number')
    return bet

def choose_the_number():
    while True:
        number = input("Enter a number between 1 to " + str(max_num) + ": ")
        if number.isdigit():
            number = int(number)
            if 1 <= number <= max_num:
                break
            else:
                print("Number must be between (1-" + str(max_num) + ")")
        else:
            print('Please enter a number')
    return number

def main():
    global balance
    if answer == 'y':
        n=1
        balance=deposit()
        while balance>0:
            print(n,"round of bet has started")
            bet = choose_the_bet()
            number = choose_the_number()
            while True:
                if bet>=balance:
                    print("You do not have enough money to bet. You have only", balance)
                    bet = choose_the_bet()
                else:
                    print("Your bet is", bet, "on", number, "with current balance", balance)
                    time.sleep(2)
                    break
            random_number = random.randint(1, 100)
            print("Roll! The winning number is", random_number, "and your number is", number)
            time.sleep(2)
            if random_number == number:
                winning_amount = (number * bet)+balance
                print("Your winning amount is", winning_amount)
                break
            else:
                balance=balance-bet
                print("You have lost the bet. Now your current balance is",balance)
                time.sleep(2)
            print("Are you ready to start another round with your current balance as",balance)
            answer2=input("Enter'y' or 'n': ")
            answer2=answer2.lower()
            if answer2=='y':
                 n=n+1
            else:
                print("You have got Rs",balance,"Thanks for visiting!")
                break
    elif answer == 'n':
        print("Thanks for visiting us!")
    else:
        print("Enter a valid option.")
        
print("Hello! Welcome to the casino game?")
print("1) Type 'y' to start the game")
print("2) Type 'n' to end the game")
answer = input("Enter your answer: ")
answer = answer.lower()
main()


         
