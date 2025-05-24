# Define the class decorator with updated greeting message
def add_greeting(cls):
    # Add greet method to the class
    def greet(self):
        return "Greetings from the Decorator!"  # New greeting message

    cls.greet = greet  # Add the greet method to the class
    return cls

# Apply the class decorator to the updated Person class
@add_greeting
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

    def birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."

# Create a Person object with both name and age
person = Person("SAIMA", 23)

# Call the new greet method added by the decorator
print(person.greet())

# Call the introduce method
print(person.introduce())

# Call the birthday method
print(person.birthday())