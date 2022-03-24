from collections import Counter

numbers = [3, 1, 2, 6, 3, 8, 3, 5, 3]

numbers = Counter(numbers)

res = numbers.most_common(1)[0][0]

repeated_items =  numbers.most_common(1)[0][1]

print("The most frequent number is "  + (str(res)) + " and it was {} times repeated.".format(repeated_items))