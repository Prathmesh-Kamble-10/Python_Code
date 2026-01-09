userInput = int(input("Enter your nth number: "))
for num in range(1,userInput+1):
    if(num%2!=0):
        print("odd no = ",num)
    else:
        print("even no = ",num)