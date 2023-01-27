def main():
    while True:
        try:
            x, y = input("Fraction: ").strip().split('/')
            x, y = int(x), int(y)
        except ValueError:
            pass
        else:
            p = calculate_percent(x,y)

            # check 'Full' or 'Empty' conditions
            print(f"{p}%" if (1 <= p <= 99) else ('E' if p < 1 else 'F'))
            break


def calculate_percent(x,y):
    try:
        return round(100 * x/y)
    except ZeroDivisionError:
        pass

main()