def car(model, speed, color):
    return {
        "model": model,
        "speed": str(speed)+"km/hr",
        "color": color
    }

print(car("bmw x1", 1000, "black-red"))

print(car("ferrari", 1100, "red"))