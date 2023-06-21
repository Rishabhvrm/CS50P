def main():
    while True:
        fraction = input("Fraction: ").strip()
        fraction = convert(fraction)
        print(gauge(fraction))
        break

def convert(fraction):
    # convert in percentage
    try:
        x, y = fraction.split('/')
        x, y = int(x), int(y)

        # prompt again if x > y
        if (x > y):
            continue

    except(ValueError, ZeroDivisionError):
        pass
    else:
        return round(100 * (x/y))


def gauge(percentage):
    # check 'Full' or 'Empty' conditions
    # add % sign if p is between (1,99)
    return(f"{percentage}%" if (1 < percentage < 99) else ('E' if percentage <= 1 else 'F'))


if __name__ == "__main__":
    main()