def main():
    word = input("Input: ")
    print("Output:", shorten(word))

def shorten(word):
    # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels = ['A', 'E', 'I', 'O', 'U']
    output = []
    for _ in word:
        if _ not in vowels:
            output.append(_)
    return ''.join(output)

if __name__ == "__main__":
    main()
# user_input = input("Input: ")

# # create a list of vowels
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# out_str = []

# for c in user_input:
#     if c not in vowels:
#         out_str.append(c)

# print(f"Output: {''.join(out_str)}")