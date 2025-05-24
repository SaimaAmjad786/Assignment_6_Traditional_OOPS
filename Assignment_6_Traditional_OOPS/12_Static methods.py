class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Call the static method without creating an object
temp_in_f = TemperatureConverter.celsius_to_fahrenheit(25)
print(f"25°C = {temp_in_f}°F")