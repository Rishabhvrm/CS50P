# making a temprory file
lst = [1, 3, 1, 3, 5, 1, 4, 7, 7]
def find_duplicates(lst):
    counter = {}

    for val in lst:
        if val not in counter:
            counter[val] = 0
            print(counter)
        counter[val] += 1

    print(counter)


    result = []
    for val, count in counter.items():
        if count > 1:
            result.append(val)

    return result

print(find_duplicates(lst))
print(find_duplicates(lst))