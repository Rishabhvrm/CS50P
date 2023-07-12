def main():
    student = get_student()

    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house          # we're actually returning one tuple
    # return (name, house)      # same as above


if __name__ == "__main__":
    main()


"""
Notes:

return multiple values
tuple - immutable, similar to list

"""