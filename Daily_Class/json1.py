# authentication = {
# "user":{
#     "name" : "prathmesh",
#     "pwd" : 12345
# },
# "newuser":{
#     "name" : "shubham",
#     "pwd" : 123456
# }}

# print(authentication["user"]["pwd"])


# import json

# # y ='{ "name":"John", "age":30, "city":"New York"}'
# # z =json.loads(y)
# # print(z["city"])

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)
# print(y[0])

# # the result is a JSON string:
# print(type(y))



# import json

# print(type(json.dumps({"name": "John", "age": 30})))
# print(type(json.dumps(["apple", "bananas"])))
# print(type(json.dumps(("apple", "bananas"))))
# print(type(json.dumps("hello")))
# print((json.dumps(42))) #'42'
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# # convert into JSON:
# y = json.dumps(x,indent = 2,separators=(". ", " = "),sort_keys=True)

# # the result is a JSON string:
# print((y))

# x = None
# print(type(x))

# print(bool(None))