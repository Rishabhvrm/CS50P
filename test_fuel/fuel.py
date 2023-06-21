def main():
    try:
        fraction = input("Fraction: ").strip()
        convert(fraction)


def convert(fraction):
    # convert in percentage
    x, y = fraction.split('/')
    x, y = int(x), int(y)
    return round(100 * (x/y))


def gauge(percentage):


if __name__ == "__main__":
    main()