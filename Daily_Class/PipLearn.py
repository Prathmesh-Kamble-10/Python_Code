import camelcase as c
name = "shubham kumar, happy birth day"

def nameToCamel(name1):
    # 2. Initialize the tool
    tool = c.CamelCase()
    # 3. Use the .hump() method to actually change the text
    return tool.hump(name1)


result = nameToCamel(name)
print(result)