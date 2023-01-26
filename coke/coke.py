def main():
    while True:
        cost = 50
        print(f"Amount Due: " {cost})
        coin_denom = int(input("Insert Coin: "))
        if coin_denom in [25, 10, 5]:
            cost = calculate_due_amount(cost - coin_denom)
            break

    print("yay")

def calculate_due_amount(remaining_amount, coin_denom):
    return remaining_amount - coin_denom


main()