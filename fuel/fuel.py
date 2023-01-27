def main():
    x, y = input("Fraction: ").strip().split('/')
    p = str(calculate_percent(x,y)) + "%"

    # check 'Full' or 'Empty' conditions
    if p < 1:
        p = 'E'
    elif p > 99:
        p = 'F'

    print(f"{p}")


def calculate_percent(x,y):
    return round(100 * int(x)/int(y))

main()