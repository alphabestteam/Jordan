from customer import Customer
class Register:
    def __init__(self):
        self.profit = 0
        self.total_shopping_list = []

    def checkout_customer(self,customer): 
        self.profit =+ customer.total_purchase_amount
        self.total_shopping_list.append(customer.shopping_list)

    def print_summary(self):
        print(f'total profit for the day: {self.profit}, total shopping list fo the day: {self.total_shopping_list}')

 