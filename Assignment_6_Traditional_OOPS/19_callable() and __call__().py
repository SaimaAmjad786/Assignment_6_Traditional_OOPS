class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)

print("Is 'double' callable?", callable(double))  # Output: True

result = double(5)  # 5 * 2 = 10
print("Result of calling double(5):", result)