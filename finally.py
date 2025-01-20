def func1():
    try:           # try block      
        l = [1,3,5,2,4] 
        i=int(input("Enter the index: ")) 
        print(l[i])
        return 1
    except:        # except block
        print("Invalid index")
        return 0

    finally:       # finally block
        print("Finally block is executed")

x = func1()
print(x)
