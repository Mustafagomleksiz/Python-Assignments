num = input("Enter a number: ")



if num.isdigit():

    new_num = int(num)

    num_list = []

    

    while new_num > 0:

        digit = new_num % 10

        num_list.append(digit)

        new_num //= 10

    order = len(num_list)

    new_list= 0

    

     

    for i in num_list:

         new_list += i ** order

    if new_list== int(num):

        print(num,"is an Armstrong number")

    else:

        print(num,"is not an Armstrong number")



else :

    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")