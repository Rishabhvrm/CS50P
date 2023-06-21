def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            fraction = convert(fraction)
        except:
            pass
        else:
            print(gauge(fraction))
            break

def convert(fraction):
    # convert in percentage
    x, y = fraction.split('/')
    x, y = int(x), int(y)

    if y == 0:
        raise ZeroDivisionError

    if not isinstance(x, int) or not isinstance(y, int) or x > y:
        raise ValueError

    return round(100 * (x/y))


def gauge(percentage):
    # check 'Full' or 'Empty' conditions
    # add % sign if p is between (1,99)
    return(f"{percentage}%" if (1 < percentage < 99) else ('E' if percentage <= 1 else 'F'))


if __name__ == "__main__":
    main()