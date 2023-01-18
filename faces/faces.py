def main():
    user_input = input()
    print(convert(user_input))

def convert(s):
    return s.replace(":)","🙂").replace(":(","🙁")

main()