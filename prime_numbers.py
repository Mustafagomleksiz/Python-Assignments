num = int(input("Please enter number : "))

liste = []



for num in range(1,num):

    

    if num > 1 :

        

        for i in range(2,num):

            

            if num % i == 0:

                break

        else :

            liste.append(num)

            

print(liste)