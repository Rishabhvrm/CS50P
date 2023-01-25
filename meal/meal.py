def main():
    time = input("What time is it? ").strip()
    print(convert(time))

def convert(time):
    # split the time into hours and minutes
    hours, minutes = map(int, time.split(":"))

    # convert time to a float value
    t =  hours + minutes/60

    # map the float time to what meal it is
    if 7 <= t <= 8:
        return "breakfast time"
    elif 12 <= t <= 13:
        return "lunch time"
    elif 18 <= t <= 19:
        return "dinner time"


if __name__ == "__main__":
    main()