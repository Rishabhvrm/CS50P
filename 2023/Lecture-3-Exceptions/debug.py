def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(h):
    for i in range(h):
        print("#" * i)

main()