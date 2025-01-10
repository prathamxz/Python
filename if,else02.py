a= int(input("Enter your age :"))
print("You are",a,"years old")
# conditional operators
# >,<,>=,<=,==,!=

if (a<18):
    print("You are a minor u cant drive")
else:
    print("You are an adult u can drive")
a= int(input("Enter your Budget :"))
appleprice = 200
budget = 100
if (appleprice<=budget):
    print("Alexa, Add 1 kg apples to the cart")
else:
    print("Alexa,do not add apples to the cart")

orangeprice = 230
budget1=330

if (budget1-orangeprice>=100):
    print("Alexa, Add 1 kg oranges to the cart")
elif (budget1-orangeprice<100):
    print("Alexa, Add 500 gms oranges to the cart")

else:(budget1-orangeprice<100)
print("Alexa,do not add oranges to the cart")
