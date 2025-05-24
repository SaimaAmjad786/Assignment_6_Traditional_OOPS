# Class A with a method show
class A:
    def show(self):
        return "Class A: show() method"

# Class B inherits from A and overrides show
class B(A):
    def show(self):
        return "Class B: show() method"

# Class C inherits from A and overrides show
class C(A):
    def show(self):
        return "Class C: show() method"

# Class D inherits from both B and C
class D(B, C):
    pass  # No need to override show, we'll observe MRO behavior

# Create an object of D
obj = D()

# Call show() method on D object and observe MRO
print(obj.show())

print(D.__mro__)

