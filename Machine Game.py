import math
import random

print("Welcom to the sSlot Machine Game!")
starting_balance = 100
current_balance = starting_balance
item_list=["Cherry","Bell","Lemon","Bottle","Pen"]

#random Symbols
first_symbol = random.choice(item_list)
second_symbol = random.choice(item_list)
third_symbol=random.choice(item_list)

#calculating
def cal():
    wager = int(input("Enter your bet(1-10): "))
    if wager <=10:
        if first_symbol==second_symbol==third_symbol:
            multiple = 10
            total_wins = multiple*wager
            new_balance = total_wins+current_balance
            print("[",first_symbol,"] [",second_symbol,"] [",third_symbol,"]")
            print("Congratulations! You won ",multiple,"times your bet!")
            print("New balance: ",new_balance)
        elif  first_symbol==second_symbol or first_symbol==third_symbol or second_symbol == third_symbol:
            multiple = 3
            total_wins = multiple*wager
            new_balance = total_wins+current_balance
            print("[",first_symbol,"] [",second_symbol,"] [",third_symbol,"]")
            print("Congratulations! You won ",multiple,"times your bet!")
            print("New balance: ",new_balance)
        else:
            print("No match.")
            print("[",first_symbol,"] [",second_symbol,"] [",third_symbol,"]")
            print("Opps!, better luch next time.")
    else:
        print("Invalid bet amount, Please enter a bet between 1 to 10.")
#yes or no 
def main():
    cal()
    while True:
        yes_no = input("Do you want to play again? yes/no: ")
        if yes_no.lower()=='yes':
            cal()
        else:
            print("Game Over.!")
        break
main()
