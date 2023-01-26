def main():

    # initialize amount due before enterinig any coins
    amount_due = 50

    # prompt the user repeatedly until coin_denom is in [25, 10, 5]
    while True:
        print(f"Amount Due: {amount_due}")
        coin_denom = int(input("Insert Coin: "))

        # continue only if user enters correct coin denomination
        if coin_denom in [25, 10, 5]:

            # update amount_due
            amount_due = calculate_due_amount(amount_due, coin_denom)

            # break if amount due goes 0 or negative i.e. user has paid full amount or extra
            if amount_due <= 0:
                # print change owed and change the sign to make it +ve
                print(f"Change Owed: {-amount_due}")
                break





def calculate_due_amount(remaining_amount, coin_denom):
    return remaining_amount - coin_denom


main()