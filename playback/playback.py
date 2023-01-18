# get user input
user_input = input()

# split user input by space into a list
word_list = user_input.split(' ')

# join the elements in the list with '...' (a period)
print('...'.join(word_list))