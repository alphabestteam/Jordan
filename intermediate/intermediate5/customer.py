from product import Product
class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_list = {} 
        self.total_purchase_amount = 0 

    def add_product(self, product, quantity):
        if product.product_name in self.shopping_list:
           self.shopping_list[product.product_name] += quantity 
        else:
             self.shopping_list[product.product_name] = quantity
        self.total_purchase_amount += product.price * quantity

        """
    def remove_product(self, product_name, quantity):
        if product_name in self.shopping_list:
            existing_quantity = self.shopping_list[product_name]
            if quantity < existing_quantity:
                self.shopping_list[product_name] = existing_quantity - quantity
                self.total_purchase_amount -= price * quantity
            elif quantity == existing_quantity:
                del self.shopping_list[product.product_name]
                self.total_purchase_amount -= product.total_price
            else:
                del self.shopping_list[product.product_name]
                self.total_purchase_amount -= product.total_price
        else:
            print(f"{product.product_name} is not in the shopping list.")

"""   

