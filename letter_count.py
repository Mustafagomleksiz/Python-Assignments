sentence = input("Please enter word : ")



dict = {}



for char in sentence:

    if char in dict:

        dict[char] += 1

        

    else:

        dict[char] = 1

        

print(dict)