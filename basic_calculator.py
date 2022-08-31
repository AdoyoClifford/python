def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + "=" + str(answer) + "\n")

def subtract(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + "=" + str(answer)+ "\n")

def multiply(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + "=" + str(answer)+ "\n")

def divide(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + "=" + str(answer)+ "\n")

while True:
    print("A. Addition")
    print("B. Subtractionn")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choice ")

    if choice == 'a' or choice == 'A':
        print('Addition')
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        add(a,b)

    elif choice == 'b' or choice == 'B':
        print('Subtraction')
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        subtract(a,b)

    if choice == 'c' or choice == 'C':
        print('Multiplication')
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        multiply(a,b)

    if choice == 'd' or choice == 'D':
        print('Divide')
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        divide(a,b)

    if choice == 'e' or choice == 'E':
        print('Program Ended')
        quit()