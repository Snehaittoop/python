from secrets import choice


def areaCircle(r):
    r=int(input("enter radius"))
    area=3.14*r*r
    print(area)
def perimeterCircle(r):
    r=int(input("enter radius"))
    perimeter=2*3.14*r
    print(perimeter)
def arearRect(len,bredth):
    len=int(input("enter length"))
    bredth=int(input("enter bredth"))
    area=len*bredth
    print(area)
def periRect(len,bredth):
    len=int(input("enter length"))
    bredth=int(input("enter bredth"))
    perimeter=2(len*bredth)
    print(perimeter)
def areaSqure(len):
    len=int(input("enter length"))
    area=len*len
    print(area)
def perimeterSqu(len):
    len=int(input("enter length"))
    perimeter=4*len
    print(perimeter)






while True:
    print("select option")
    print("1. calculate area of circle")
    print("2.calculate perimeter of circle")
    print("3. calculate area of rectangle")
    print("4.calculate perimeter of rectangle")
    print("5. calculate area of squre")
    print("6.calculate perimeter of squre")
    print("7.exit")
    choice=int(input("select option"))
    if choice==1:
        areaCircle(r)
    elif choice==2:
        perimeterCircle(r)
    elif choice==3:
        arearRect(len,bredth)
    elif choice==4:
        periRect(len,bredth)
    elif choice==5:
        areaSqure(len)
    elif choice==6:
        perimeterSqu(len)
    else:
        break


    
