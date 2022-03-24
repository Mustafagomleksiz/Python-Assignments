liste = []

num1 = 0

num2 = 1



print("Fibonacci : ")

for i in range(10):

    liste.append(num2)

    fibonacci = num1 + num2

    num1 = num2

    num2 = fibonacci

print(liste)
