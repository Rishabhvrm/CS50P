def main():
    while True:
        try:
            x, y = input("Fraction: ").strip().split('/')
            x, y = int(x), int(y)

            # convert in percentage
            p =  round(100 * x/y)

            # prompt again if x > y
            if (x > y):
                continue
        # if user enters non-integer value 
        except (ValueError, ZeroDivisionError):
            pass

        else:
            # check 'Full' or 'Empty' conditions
            # add % sign if p is between (1,99)
            print(f"{p}%" if (1 < p < 99) else ('E' if p <= 1 else 'F'))
            break

main()