import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time() 
        result = func(*args,**kwargs) 
        end= time.time()
        print(f"{func.__name__} ran in {end-start} time.")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n) 


@timer
def addition(a,b):
    time.sleep(1)
    return a+b


# example_function(2)
print(addition(5,b=5))
