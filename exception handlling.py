a = input("Enter a number: ")
print(f"multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except Exception as e:
    print("Inavalid input")

print("Some imp lines of code")
print("End of program")