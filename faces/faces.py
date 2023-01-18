# define main function
def main():
    # get user input
    user_input = input()

    # call convert function and print the output
    print(convert(user_input))

# define convert function
def convert(s):
    # replace the smiley faces with emojis
    return s.replace(":)","🙂").replace(":(","🙁")

main()