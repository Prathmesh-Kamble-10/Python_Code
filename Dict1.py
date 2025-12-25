# Dictionary
# z = dict( {
#     "name": "prathmesh kamble",
#     "roll_no":34,
#     "add":"mumbai",
#     "std":15
# })
# print(len(z))

# student_profile = {
#     "student1":{
#     "name": "shubham kumar",
#     "roll_no":60,
#     "add":"pune",
#     "std":11
#     },
#     "student2":{
#     "name": "Prathmesh Kamble",
#     "roll_no":34,
#     "add":"mumbai",
#     "std":15
#     },
# }
# print(type(student_profile))
# print(student_profile["student2"]["name"])

# dict2 = dict({
#     "name": "shubham kumar",
#     "roll_no":34,
#     "add":"mumbai",
#     "std":11
# })

# for key,value in dict2.items():
#     print(key," = ",value)

# for x in dict2:
#     # print("keys ",x)
#     print("values ",dict2[x])

# for shubham in dict2.keys():
#     print(shubham)

# for shubham2 in dict2.values():
#     print(shubham)

# dict2["subject"]="science" #without method
# dict2.update({"Division":"A"}) #with method update
# ways of remove element from dictionary

# clear()
# pop()
# popitem()
# del

# dict2.pop("std") #pop
# dict2.popitem()
# del dict2["name"]
# dict2.clear()
# print(dict2)


#copy dictionary method()

# dict3 = {
#     "name":"shubham kumar",
#     "std":11
# }

# dict4 = dict3 # memory location
# dict4 = dict3.copy()
# dict4.update({"name":"prathmesh kamble","std":15})
# print("dictionary 3 data : ",dict3)
# print("dictionary 4 data : ",dict4)

# account = {
#     "user":{
#     "name": "shubham kumar",
#     "roll_no":34,
#     "add":"mumbai",
#     "std":11
# },
# "emp":{
#     "name": "adarsh kumar",
#     "roll_no":14,
#     "add":"varanasi",
#     "std":11
# },
# "student":{
#     "name": "messi",
#     "roll_no":10,
#     "add":"argentia",
#     "file": "stringFormate.py",
#     "std":3
# }
# }
# # print(account["student"]["file"])
# x = account.get(student["name"])
# print(x)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
# }

# x = car.get("year")
# print(x)