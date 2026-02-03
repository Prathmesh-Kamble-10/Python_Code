import re

txt = "The rain in the Spain"
# print(len(txt))
# x = re.search("^The.*Spain$",txt)
# x = re.findall("R",txt)
# x = re.split(" ",txt)
# x = re.sub("rain","main",txt)
x = re.search("\s",txt)
print(x.span())