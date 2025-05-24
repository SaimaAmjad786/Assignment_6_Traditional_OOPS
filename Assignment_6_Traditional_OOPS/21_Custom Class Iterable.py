class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start  # Initialize current position for iteration

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # End iteration when below 0
        else:
            value = self.current
            self.current -= 1
            return value

# Example usage:
print(" Countdown starts:")
for number in Countdown(10):
    print(f"⏳ {number}")
print("Countdown complete!")