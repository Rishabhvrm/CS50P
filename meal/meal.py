def main():
    time = input("What time is it? ").strip()
    t = convert(time)

    # map the float time to what meal it is
    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")

def convert(time):
    # split the time into hours and minutes
    hours, minutes = map(int, time.split(":"))

    # convert time to a float value
    return(hours + minutes/60)



if __name__ == "__main__":
    main()