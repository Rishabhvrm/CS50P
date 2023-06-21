def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            fraction = convert(fraction)
            print(gauge(fraction))
            break

def convert(fraction):
    # convert in percentage
    try:
        x, y = fraction.split('/')
        x, y = int(x), int(y)
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