import re

def main():
    print(convert(input("Hours: ")))

# allowed input
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
def convert(time):
    if matches := re.search(r"^(\d{1,2}):(\d{1,2}) AM to (\d{1,2}):(\d{1,2}) PM$", time)):
        print('Yayy')
        h_am, m_am, h_pm, m_pm = matches.group(1), matches.group(2), matches.group(3), matches.group(4)
    elif matches := re.search(r"", time)
    print('Nayy')




if __name__ == "__main__":
    main()