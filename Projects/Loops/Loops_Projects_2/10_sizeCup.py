available_sizes = ["small", "medium", "large","cutting"]

if (requested_size:= input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size} chai")
else:
    print(f"Size is unavailable - {requested_size}")
