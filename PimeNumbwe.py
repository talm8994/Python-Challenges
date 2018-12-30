number = int(input("enter a number"))

prime = True

for x in range(2, number - 1):
    if number % x == 0:
        prime = False
        break

if prime:
    print("this is a prime number!")
else:
    print("This is not a prime number!")
