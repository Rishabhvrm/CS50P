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

    # time in 00:00 a.m. till 11:59 a.m (12 hour format)
    # is same to 00:00 to 11:59 (24 hour format)
    if "a.m" and "p.m." not in time:
        # split the time into hours and minutes
        hours, minutes = map(int, time.split(":"))

        # convert time to a float value
        return(hours + minutes/60)

    else:
        # time in 12:00 p.m. till 11:59 p.m.
        if "p.m." in time:
            hours_in_pm, minutes_with_pm = time.split(":")
            minutes_in_pm, pm = minutes_with_pm.split(" ")

            hours = int(hours_in_pm) + 12
            minutes = int(minutes_in_pm)

            return (hours + minutes/60)




if __name__ == "__main__":
    main()