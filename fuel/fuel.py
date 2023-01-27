def main():
    while True:
        try:
            x, y = input("Fraction: ").strip().split('/')
            x, y = int(x), int(y)
            p =  round(100 * x/y)
        except ValueError or ZeroDivisionError:
            pass
        else:


            # check 'Full' or 'Empty' conditions
            print(f"{p}%" if (1 <= p <= 99) else ('E' if p < 1 else 'F'))
            break



main()