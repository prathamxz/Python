# s1 ={1,2,5,6}
# s2 = {7,4,6,2}

# print(s1.union(s2))
# print(s1,s2)
# s1.update(s2)
# print(s1)


cities = {"tokyo,madrid,japan,india,usa"}
cities2 ={"tokyo8,uk,newzeland,madrid,indiana,australia,delhi"}
cities4 = {"tokyo8"}
# cities3 = cities.union(cities2)
# cities3 = cities.intersection(cities2)
# cities3 = cities.symmetric_difference(cities2)
# cities3 = cities.difference(cities2)
# cities3 = cities.isdisjoint(cities2)
cities3 = cities.issuperset(cities2)
print(cities4.issuperset )

print(cities3)