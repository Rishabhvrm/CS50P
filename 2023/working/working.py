import re

def main():
    print(convert(input("Hours: ")))

# allowed input
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
def convert(time):
    if matches := re.search(r"^(\d{1,2}):(\d{1,2}) AM to (\d{1,2}):(\d{1,2}) PM$", time):
        print('Yayy')
        h_am, m_am, h_pm, m_pm = matches.group(1), matches.group(2), matches.group(3), matches.group(4)
        return convert_to_military_time(h_am, h_pm, m_am, m_pm)
    elif matches := re.search(r"^(\d{1}) AM to (\d{1}) PM$", time):
        print('Nayy')
        h_am, h_pm = matches.group(1), matches.group(2)
        return convert_to_military_time(h_am, h_pm)


def convert_to_military_time(a, b, c = "00", d = "00"):
    z = str(int(b) + 12)
    return(f"{a}:{c} to {z}:{d}")




if __name__ == "__main__":
    main()