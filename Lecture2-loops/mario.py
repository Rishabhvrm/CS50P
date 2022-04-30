def main():
    print_square(3)
    print_square2(3)


def print_square(size):
    for _ in range(size):
        print("#" * size)

def print_square2(size):
    # for each row in square
    for i in range(size):

        # for each brick in a row
        for j in range(size):

            # Print brick
            print("#", end = "")
        print()

main()