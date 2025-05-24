# Engine class definition
class Engine:
    def run(self):
        return "Vroom! The engine is now active."

# Car class using composition
class Car:
    def __init__(self, name, engine):
        self.name = name          # Car's name
        self.engine = engine      # Car has an Engine

    def start(self):
        # Include the car's name in the message
        return f"{self.name}: {self.engine.run()}"

# Create an Engine object
my_engine = Engine()

# Create a Car object with a name and engine
my_car = Car("Toyota Corolla", my_engine)

# Start the car
print(my_car.start())