# Set Join
#update

# set1 = {'apple','pineapple','strawberry'} #order maintain, immutable, dublicate
# set2 = {"orange","kiwi",'apple'}
# set2.add("banana")
# set1.update(set2)
# print(set1)
# set3 = {11,55,88,84}
# # set1.update(set2,set3)  #set1 = set1+set2
# # set1 |= set2 | set3 #shortcut way to join  set1 = set1+set2+set3
# print(set2)

#union

# set1 = {'apple','pineapple','strawberry'}
# set2 = {"orange","kiwi",'apple'}
# set3 = {11,55,88,84}
# # result = set1.union(set2,set3) #variable = set1+set2
# result = set1 | set2 | set3  #variable = set1+set2

# print(result)

# # Intersection
# Intersection_update

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft","apple"}
# a = {"google", "microsoft","apple"}
# x.intersection_update(y,a)
# z = x.intersection(y)
# z = x & y & a #shortcut way

# print(z)
# print(x)


# difference()
# difference_update()

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft","apple"}
# a = {"apple","banana"}
# y.difference_update(x)
# # z = y.difference(x,a)
# z = x-a-y #shortcut way difference()
# x-=y #shortcut way of difference_update()  
# print(z)
# print(x)

#symentic difference

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft","apple"}

# # result = x.symmetric_difference(y)
# result = x^y #shortcut way
# print(result)


#frozenset 

# set1 = {"apple","banana"}
# set1.add("grabs")
# print(set1)

# set2=frozenset(("apple", "banana", "cherry","apple"))
# print((set2))