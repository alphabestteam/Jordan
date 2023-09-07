from product import Product
from customer import Customer

def main():
    product1 = Product("milk", 10.0, 3)
    product2 = Product("eggs", 5.0, 2)
    customer1 = Customer("Jordan")
    customer1.add_product(product1, 2)
    customer1.add_product(product2, 4)
    product1.print_product()
if __name__ == "__main__":
    main()