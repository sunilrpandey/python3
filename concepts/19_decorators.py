import time

def generic_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed before {}".format(original_function.__name__))
        result = original_function(*args, **kwargs)
        print("Wrapper executed after {}".format(original_function.__name__))
        return result
    return wrapper_function

@generic_decorator
def display():
    print("Display function executed")

@generic_decorator
def add(a, b):
    print("Adding:", a, b)
    return a + b

def execution_time_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {original_function.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper_function

@execution_time_decorator
def slow_function():
    print("Slow function started...")
    time.sleep(1)
    print("Slow function finished.")

if __name__ == "__main__":
    print("Demoing decorators:")
    
    print("Demoing simple decorator:")
    display()
    result = add(2, 3)
    print("Result:", result)

    print("Demoing a real world decorator:")
    slow_function()
