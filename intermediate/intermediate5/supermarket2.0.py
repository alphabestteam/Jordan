from product import Product
from customer import Customer
from register import Register
def main():
    product1 = Product("milk", 10.0, 3)
    product2 = Product("eggs", 5.0, 2)
    customer1 = Customer("Jordan")
    customer1.add_product(product1)
    customer1.add_product(product2)
    customer1.remove_product("milk",1)
    print(f"Customer: {customer1.name}")
    register1 = Register()
    register1.checkout_customer(customer1)
    register1.print_summary()
    print(f"Total Purchase Amount: {customer1.total_purchase_amount}")

if __name__ == "__main__":
    main()