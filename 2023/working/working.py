import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except:
        sys.exit('Not a valid time')

def convert(time):
    # allowed input - 9:00 AM to 5:00 PM
    if matches := re.search(r"^(\d{1,2}):(\d{1,2}) (AM|PM) to (\d{1,2}):(\d{1,2}) (AM|PM)$", time):
        # print('Yayy')
        hour, minute, time_indicator = matches.group(1), matches.group(2), matches.group(3)
        start = convert_to_military_time(time_indicator, hour, minute)

        hour, minute, time_indicator = matches.group(4), matches.group(5), matches.group(6)
        end = convert_to_military_time(time_indicator, hour, minute)

        return f"{start} to {end}"

    # allowed input - 9 AM to 5 PM
    elif matches := re.search(r"^(\d{1,2}) (AM|PM) to (\d{1,2}) (AM|PM)$", time):
        # print('Nayy')
        hour, time_indicator = matches.group(1), matches.group(2)
        start = convert_to_military_time(time_indicator, hour)

        hour, time_indicator = matches.group(3), matches.group(4)
        end = convert_to_military_time(time_indicator, hour)

        return f"{start} to {end}"


def convert_to_military_time(time_indicator, h, m="00"):
    # validate time
    validate_time(h,m)

    # add 12 for every case except 12
    # don't need 24:00 for 12 PM
    if time_indicator == "PM" and h != "12":
        h = str(int(h) + 12)

    # 12 AM is 00
    if time_indicator == "AM" and h == "12":
        h = "00"

    # 9 -> 09
    if len(h) == 1: h = f"0{h}"
    return f"{h}:{m}"

def validate_time(h,m):
    if not 0 <= int(h) <= 12 or not 0 <= int(m) <= 59:
        raise ValueError


if __name__ == "__main__":
    main()