#decision making -> menu driven program

a = int(input( "enter first number:"))
b = int(input("enter second number:"))

choice = int ( input("What is Calcutaion is to be DONEEE \n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n"))

if (choice == 1):
    print(a+b)

elif (choice == 2):
    print(a-b)

elif(choice == 3):
    print(a*b)

else:
    print(a%b)