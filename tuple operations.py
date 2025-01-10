countries = ('USA', 'UK', 'Canada', 'Australia', 'Germany','India','Japan','China')
print(countries)
temp = list(countries)
temp.append('France') #add item
temp.pop (2) #remove item
temp[2] = 'Italy' #replace item
countries=tuple(temp)
print(countries)   


