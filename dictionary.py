# dict = {
#     "harry" : "Human being",
#     "Spoon" : "object"
# }
# print(dict["harry"])
# print(dict["Spoon"])

# dic = {
#     44 : "Hari",
#     66 : "Neha",
#     11 : "Nora",
#     1 : "Raj"
# }
# print(dic[1])

info = {
    'Name' : "Pratham", "Age" : 18 ,"Eligibile" : "True"
} 
# print(info)
# print(info['Name'])
# print(info.get('Name'))
print(info.keys())

for keys in info.keys ():
    print(f"The value corresponding to the keys {keys} is {info[keys]}")
print("\n")

for keys, value in info.items():
    print(f"The value corresponding to the keys {keys} is {value}")
print("\n")