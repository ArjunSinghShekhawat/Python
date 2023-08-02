# x = 90
# match x:
#     case 0:
#         print("X is zero")

#     case 4:
#         print("X is 4")
#     case _ if x!=90:
#         print("default :")
    
#     case _ if x!=80:
#         print("x is not 80")
#     case _:
#         print(x)

marks = int(input("Enter marks"))

match marks:
    case x if x>=90:
        print("Grade A")
    
    case x if x>=80 and x<90:
        print("Grade B")

    case x if x>=70 and x<80:
        print("Grade C")
    
    case x if x>=60 and x<70:
        print("Grade D")
    
    case x if x>=50 and x<60:
        print("Grade E")
    
    case _:
        print("fail")
        

