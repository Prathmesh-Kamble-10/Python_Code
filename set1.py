thistuple = ("apple", "banana", "cherry","apple") #modification 
thislist = ["apple", "banana", "cherry",{"apple", "banana", "cherry","apple"}]
thisset = {"apple", "banana", "cherry","Apple"} 

newset = set(("apple", "banana", "cherry","Apple")) #str() , int(), float(), bool(), set(), tuple(), list(), dict() -->

# print(thistuple)
# print(thislist[3])
# print(thisset)

thislist =["apple", "banana", "cherry"]
thislist.pop()
print(thislist)