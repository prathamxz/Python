marks = [4,5,6,"pratham",True]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
# print(marks[4]) # IndexError: list index out of range

print(marks[-3]) #Negative indexing
print(marks[len(marks)-3]) #Postive indexing
print(marks[4-2]) #Postive indexing
print(marks[2]) #Postive indexing



# Python Lists
# • Lists are ordered collection of data items.
# • They store multiple items in a single variable.
# • List items are separated by commas and enclosed within square brackets |].
# • Lists are changeable meaning we can alter them after creation.

# List Index
# Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index
# [0], second item has index [1], third item has index [2] and so on.

# Accessing list items
# We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give
# "Green" and so on...

# Positive Indexing:
# As we have seen that list items have index, as such we can access items using these indexes.

# Negative Indexing:
# Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-11, second last item has index [-2], third last item has index |-3] and so on.