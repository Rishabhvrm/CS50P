def main():
    x, y = input("Fraction: ").strip().split('/')
    p = calculate_percent(x,y)

    # check 'Full' or 'Empty' conditions
    print(f"{p}%" if (1 <= p <= 99) else ('E' if p < 1 else 'F'))



def calculate_percent(x,y):
    return round(100 * int(x)/int(y))

main()