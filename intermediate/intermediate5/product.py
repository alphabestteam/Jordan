class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.total_price = price * quantity
    def print_product(self):
        print(f'{self.product_name}, {self.price}, {self.quantity}')

    