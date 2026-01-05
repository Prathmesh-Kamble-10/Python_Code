urFood = input("Enter your food name : " ).capitalize()

menu = [
    "Samosa",
    "Samosa chat",
    "Vadapav",
    "Franki",
    "Bhaji pav"
]


fastFood = [food for food in menu if urFood in food]  #vadpav--> ['Vadapav']
print(fastFood)


# print("Vadapav" in menu )

# foodlist = []
# for food in menu:
#     if(urFood in food):
#         foodlist=food
#     print(foodlist)
