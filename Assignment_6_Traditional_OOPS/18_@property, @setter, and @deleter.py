class Product:
    def __init__(self, price):
        self._price = price

    # Getter using @property
    @property
    def price(self):
        print("Getting price...")
        return self._price

    # Setter using @price.setter
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        print("Setting price...")
        self._price = value

    # Deleter using @price.deleter
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Example usage
product = Product(1000)

# Get price
print(product.price)

# Set price
product.price = 500
print(product.price)

# Delete price
del product.price