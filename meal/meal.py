def main():
    time = input("What time is it? ").strip()
    print(convert(time))

def convert(time):
    hours, minutes = map(int, time.split(":"))
    t =  hours + minutes/60

    if 7 <= t <= 8:
        meal_time = "breakfast time"
    elif 12 <= t <= 13:
        meal_time = "lunch time"
    elif 18 <= t <= 19:
        meal_time = "dinner time"

    return meal_time

    # map the float time to what meal it is

if __name__ == "__main__":
    main()