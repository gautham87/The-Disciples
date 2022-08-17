class Calculator():
    num1 = 0
    num2 = 0

    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    choice = int(input("Enter 1 for addition, 2 for multiplication, 3 for division, 4 for subtraction"))
    
    if (choice == 1):
        print(num1+num2)

    elif (choice == 2):
        print(num1*num2)
    
    elif (choice==3):
        print(num1/num2)

    elif (choice==4):
        print(num1-num2)



