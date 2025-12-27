# Transportation mode selection

# person distance < 3 = walk, distance<=15 = bike, distance > 15 = car

distance = 25
transport = ""

if distance < 3:   
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport ="Car"

print("AI recommends you the transport of : ",transport)


