from secrets import choice


while True:
    print("1. add two number")
    print("2. substract 2 numbers")
    print("3. multiply 2 number")
    print("4. divide 2 numbers")
    print("5. exit")
    choice=int(input("select an option"))
    if choice==1:
        num1=int(input("enter first number"))
        num2=int(input("enter second number"))
        result=num1+num2
        print(result)
    elif choice==2:
        num1=int(input("enter first number"))
        num2=int(input("enter second number"))
        result=num1-num2
        print(result)
    elif choice==3:
        num1=int(input("enter first number"))
        num2=int(input("enter second number"))
        result=num1*num2
        print(result)
    elif choice==4:
        num1=int(input("enter first number"))
        num2=int(input("enter second number"))
        result=num1/4num2
        print(result)
    else:
        break
