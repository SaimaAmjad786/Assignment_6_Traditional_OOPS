# Define the decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

# Define the say_hello function with a new message
@log_function_call
def say_hello():
    print("How are you today?")

# Call the decorated function
say_hello()