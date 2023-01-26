def main():
    cost = 50
    while True:
        coin_denom = int(input("Insert Coin: "))
        cost = calculate_due_amount(cost, coin_denom)

        if coin_denom not in [25, 10, 5] and cost != 0:




def calculate_due_amount(remaining_amount, coin_denom):
    return remaining_amount - coin_denom


main()