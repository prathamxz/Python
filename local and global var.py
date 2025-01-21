x =4

print(x)

def hello():
    global x
    x = 5
    print(f"local x is {x}")
    print(x) 
    print("helloww")


print(f"global x is {x}")
hello()
print(f"global x is {x}")