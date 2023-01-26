def main():
    while True:
        print(f"Amount Due: " {amount_due()})
        coin_denom = int(input("Insert Coin: "))
        if coin_denom in [25, 10, 5]:
            break

        