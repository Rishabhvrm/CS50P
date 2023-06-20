def main():
    word = input()
    print(shorten(word))

user_input = input("Input: ")

# create a list of vowels
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

out_str = []

for c in user_input:
    if c not in vowels:
        out_str.append(c)

print(f"Output: {''.join(out_str)}")