def changeCase(func):
    def case(x):
        return func(x).upper()
    return case

@changeCase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))
