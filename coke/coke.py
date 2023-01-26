def main():
    cost = 50
    while True:
        print(f"Amount Due: {cost}")
        coin_denom = int(input("Insert Coin: "))
        if coin_denom in [25, 10, 5] and cost == 0:
            print(f"cost - {cost}")
            cost = calculate_due_amount(cost, coin_denom)
            print(f"Amount Due: {cost}")
            break

    print("yay")

def calculate_due_amount(remaining_amount, coin_denom):
    return remaining_amount - coin_denom


main()