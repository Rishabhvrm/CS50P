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

    AM = "a.m."
    PM = "p.m."

    # if time is in (24 hour format)
    if AM not in time and PM not in time:
        # split the time into hours and minutes
        hours, minutes = map(int, time.split(":"))

        # convert time to a float value
        return(hours + minutes/60)

    # if time in (12 hour format)
    else:
        # split hours and mins along with am/pm
        hours_in_am_pm, minutes_with_am_pm = time.split(":")
        # split mins and am/pm
        minutes_in_am_pm, am_pm = minutes_with_am_pm.split(" ")

        # add 12 if hour is in pm and convert to int
        hours = (int(hours_in_am_pm) + 12) if am_pm == PM else int(hours_in_am_pm)
        minutes = int(minutes_in_am_pm)

        return (hours + minutes/60)




if __name__ == "__main__":
    main()