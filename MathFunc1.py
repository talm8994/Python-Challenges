def subtract (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

print ("select an operation -\n "
       "1. Add\n"\
       "2. subtract\n"\
       "3. multipy\n"\
       "4. divide\n")

select: str = input("Select operations form 1, 2, 3, 4 :")

number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter second number: "))

if select == '1':
    print(number_1, "+", number_2, "=", number_1 + number_2)

elif select == '2':
    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))

elif select == '3':
    print (number_1, "*",number_2, "=",
           multiply (number_1, number_2))

elif select == '4':
    print (number_1, "/", number_2, "=",
          divide(number_1, number_2))

else:
    print("Invalid input")