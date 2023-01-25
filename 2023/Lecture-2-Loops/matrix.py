# making this file to demonstrate
# > a neat way of printing a matrix

def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print('#' * width)

main()