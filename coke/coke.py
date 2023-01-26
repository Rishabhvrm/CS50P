def main():
    amount_due = 50
    while True:
        print(f"Amount Due: {amount_due}")
        coin_denom = int(input("Insert Coin: "))


        if coin_denom not in [25, 10, 5] and amount_due > 0:
            amount_due = calculate_due_amount(amount_due, coin_denom)
            continue

        if amount_due <= 0:
            print(f"Change Owed: {-amount_due}")
            print('check point')
            break



def calculate_due_amount(remaining_amount, coin_denom):
    return remaining_amount - coin_denom


main()