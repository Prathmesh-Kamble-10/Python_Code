# x = [355,"Shubham",True,89.5]
# x[0]=4
# (x[1:-1])=["ram",False,77]
# print(x)


# typecasting
# x = "22"
# y = 20
# result = (y)+int(x)
# print(result)

# string / tuple --> immutable
# list --> mutable

# insertion in list

# chips = ["potato","banana","onion"] #potato, banana, onion, palak, corn
# chips.append("palak") 
# chips.insert(2,"corn") 
# chips.remove("banana")
# chips.pop(1)
# del chips
# chips.clear()
# print(chips)

# brandChips = {"bingo":1,"diomand":2,"balaji":3,"lays":4,"halke-phulke":5}
# chips.extend(brandChips)
# print(chips)

# remove()
# pop() 
# del - 
# clear()


# list comphresion
# short hand
# list=["apple","orange","nose","rose","mahesh","men","strawberry","sugar"]
# newlist = [x for x in list if "se" in x]
# print(newlist)

# full hand for loop
# list=["apple","orange","nose","rose","mahesh","men","strawberry","sugar"]
# listNew=[]
# for l in list:
#     if "se" in l:
#         listNew.append(l)
# print(listNew)

        #   0               1                                      2
# li1 =["student_profile",["name",["shubham","adarsh","soham"]],["rollno",[45,12,33]]]
                                    # 0           1       2                0   1  2 
                            # 0           1                       0           1
# print(li1[2][1][2])
