def main():
    x, y = input("Fraction: ").strip().split('/')
    p = calculate_percent(x,y)

    # check 'Full' or 'Empty' conditions
    if p < 1:
        print('E')
    elif p > 99:
        print('F')

    print(f"{p}%")



def calculate_percent(x,y):
    return round(100 * int(x)/int(y))

main()