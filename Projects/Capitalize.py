name = input("Enter Your Name : ")

words = name.split(" ")   # split by space

capitalized_words = [] #["Shubham","Kumar"] "

for word in words:
    if word:  # check word is not empty
        capitalized_words.append(word[0].upper() + word[1:])
    else:
        capitalized_words.append(word)

result = " ".join(capitalized_words)
print(result)


