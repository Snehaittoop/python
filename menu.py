from re import sub


def addition(num1,num2):
    res=num1+num2
    return res
def sub(num1,num2):
    res=num1-num2
    return res
def mul(num1,num2):
    res=num1*num2
    return res
def div(num1,num2):
    res=num1/num2
    return res

while True:
    print("1. add : ")
    print("2. substract 2 numbers: ")
    print("3. multiply 2 number: ")
    print("4. divide 2 numbers: ")
    print("5. exit")
    choice=int(input("select an option"))
    if choice==1:
        num1=int(input("enter first number"))
        num2=int(input("enter second number"))
        result=addition(num1,num2)
        print(result)
    elif choice==2:
        num1=int(input("enter first number"))
        num2=int(input("enter second number"))
        result=sub(num1,num2)
        print(result)
    elif choice==3:
        num1=int(input("enter first number"))
        num2=int(input("enter second number"))
        result=mul(num1,num2)
        print(result)
    elif choice==4:
        num1=int(input("enter first number"))
        num2=int(input("enter second number"))
        result=div(num1,num2)
        print(result)
    else:
        break
