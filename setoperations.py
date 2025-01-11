# s1 ={1,2,5,6}
# s2 = {7,4,6,2}

# print(s1.union(s2))
# print(s1,s2)
# s1.update(s2)
# print(s1)


cities = {"tokyo,madrid,japan,india,usa"}
cities2 ={"tokyo8,uk,newzeland,madrid,indiana,australia,delhi"}
cities4 = {"tokyo8,uk,newzeland,madrid"}
# cities3 = cities.union(cities2)
# cities3 = cities.intersection(cities2)
# cities3 = cities.symmetric_difference(cities2)
# cities3 = cities.difference(cities2)
# cities3 = cities.isdisjoint(cities2)
# cities3 = cities.issuperset(cities2)
# print(cities2.issuperset (cities4))
# print(cities3)

cities11 = {"ab","kk"}
cities11.add("helsinki")
print(cities11)

cities12 = {"ab","kk"}
cities12.remove("kk")
print(cities12)

cities13 = {"ab","ff","kk"}
item = cities13.pop()
print(cities13)
print(item)

# cities13 = {"ab","ff","kk"}
# del cities13 #deletes set
# print(cities13)
# print(item)

cities15 = {"ab","kk"}
cities15.clear()
print(cities15) 