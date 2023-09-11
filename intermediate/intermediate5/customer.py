from product import Product
class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_list = []
        self.total_purchase_amount = 0 

    def add_product(self, product):
        for existing_product in self.shopping_list:
            if existing_product.product_name == product.product_name:
                existing_product.quantity += product.quantity
                existing_product.total_price += product.total_price
                break
        else:
            self.shopping_list.append(product)
            self.total_purchase_amount += product.total_price

    def remove_product(self, product_name, quantity):
            for product in self.shopping_list:
                if product.product_name == product_name:
                    if product.quantity <= quantity:
                        self.shopping_list.remove(product)
                        self.total_purchase_amount -= product.total_price
                    else:
                        product.quantity -= quantity
                        product.total_price -= product.price * quantity
                        self.total_purchase_amount -= product.price * quantity
                    break

