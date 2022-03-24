num = int(input("Enter a number: "))

prime_numbers = False



if num > 1:

    for i in range(num):

        if num % 2 == 0:

            prime_numbers = True

            break

            

if prime_numbers :

    print(num, "is not a prime number")

else:

    print(num, "is a prime number")