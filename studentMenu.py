from secrets import choice


while True:
    print("1. add student")
    print("2. view student")
    print("3. exit")
    choice=int(input("enter option"))
    student =[]
    if choice==1:
        getName=input("enter a name: ")
        getRoll=int(input("enter rollnumber: "))
        getAdmissionnum=int(input("enter admission number: "))
        getCollegename=input("enter college name: ")
        data={'name':getName,'roll':getRoll,'admiss':getAdmissionnum,'college':getCollegename}
        print(data)
        student.append(data)
        
    elif choice==2:
        print(student)
    else:
        break