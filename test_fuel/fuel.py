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


if __name__ == "__main__":
    main()