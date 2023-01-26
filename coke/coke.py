def main():
    amount_due = 50
    while True:
        print(f"Amount Due: {amount_due}")
        coin_denom = int(input("Insert Coin: "))

        amount_due = calculate_due_amount(amount_due, coin_denom)

        if coin_denom not in [25, 10, 5] or amount_due != 0:
            continue

        print('check point')
        break



def calculate_due_amount(remaining_amount, coin_denom):
    return remaining_amount - coin_denom


main()