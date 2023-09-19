class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.total_price = price * quantity

    def __repr__(self):
        return f"Product: {self.product_name}, Price per Unit: {self.price}, Quantity: {self.quantity}, total Price: {self.total_price}"

    