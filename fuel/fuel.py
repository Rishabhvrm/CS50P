def main():
    x, y = input("Fraction: ").strip().split('/')
    print(f"{round(100 * int(x)/int(y)}%"))




main()