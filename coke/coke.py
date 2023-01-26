def main():

    # initialize amount due before enterinig any coins
    amount_due = 50

    # prompt the user repeatedly
    # until coin_denom is in [25, 10, 5]
    # or amount_due > 0
    while True:

        print(f"Amount Due: {amount_due}")
        coin_denom = int(input("Insert Coin: "))

        # continue if conditions met
        if coin_denom in [25, 10, 5] and amount_due > 0:

            # calculate amount due
            amount_due = calculate_due_amount(amount_due, coin_denom)

            # break if amount due goes 0 or negative
            # i.e. user has paid full amount or extra
            if amount_due <= 0:

                # print change owed and change the sign to make it +ve
                print(f"Change Owed: {-amount_due}")
                break

            continue



def calculate_due_amount(remaining_amount, coin_denom):
    return remaining_amount - coin_denom


main()