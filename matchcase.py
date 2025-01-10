x = int(input("Enter the value of x: "))
# x is the variable to match
match x :
    #if x is 0
    case 0:
        print("x is zero.")
    #case with if condition
    case 4 if x% 2 == 0 :
        print ("x % 2 == 0 and case is 4")
        #Empty case with if condition
    case _ if x < 10:
        print("x is less than 10")
        #default case will only be matched f the above cases were not matched so it basically just an else statement
    case _ :    
        print ("X")
    
