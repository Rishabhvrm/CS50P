import re

def main():
    print(convert(input("Hours: ")))

# allowed input
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
def convert(time):
    if matches := re.search(r"^(\d{1,2}):(\d{1,2}) (AM|PM) to (\d{1,2}):(\d{1,2}) (AM|PM)$", time):
        # print('Yayy')
        hour, minute, time_indicator = matches.group(1), matches.group(2), matches.group(3)
        start = convert_to_military_time(time_indicator, hour, minute)

        hour, minute, time_indicator = matches.group(4), matches.group(5), matches.group(6)
        end = convert_to_military_time(time_indicator, hour, minute)

        return f"{start} to {end}"

    elif matches := re.search(r"^(\d{1,2}) (AM|PM) to (\d{1,2}) (AM|PM)$", time):
        # print('Nayy')
        hour, time_indicator = matches.group(1), matches.group(2)
        start = convert_to_military_time(time_indicator, hour)

        hour, time_indicator = matches.group(3), matches.group(4)
        end = convert_to_military_time(time_indicator, hour)

        return f"{start} to {end}"


def convert_to_military_time(time_indicator, h, m="00"):
    if time_indicator == "PM":
        h = str(int(h) + 12)
    return f"{h}:{m}"




if __name__ == "__main__":
    main()