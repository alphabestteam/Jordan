import os
import json
from customers import Customer
import socket

class Bank:
    def __init__(self):
        self.customers = {}
        if not os.path.exists("customers"):
            os.mkdir("customers")
        
    def start_listen(self):
        server_host = "127.0.0.1"  
        server_port = 12345       
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_host, server_port))
        server_socket.listen(5)
        print(f"Bank server is listening on {server_host}:{server_port}")
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            data = client_socket.recv(1024).decode()
            command = data.split(' ')[0]
            print(command)
            if command == 'create_account':
                _, name, balance = data.split(' ')
                self.create_account(name, balance)
                client_socket.send("Account created successfully.".encode())
            elif command == "deposit":
                _, account_number, name, amount = data.split(' ')
                self.deposit(account_number, name, amount)
                client_socket.send("Deposit successful.".encode())
            elif command == "withdraw":
                _, account_number, name, amount = data.split(' ')
                self.withdraw(account_number, name, amount)
                client_socket.send("Withdrawal successful.".encode())
            elif command == "transfer":
                _, from_account, from_name, to_account, to_name, amount = data.split(' ')
                self.transfer(from_account, from_name, to_account, to_name, amount)
                client_socket.send("Transfer successful.".encode())
            elif command == "exit":
                client_socket.close()
                break
            else:
                print(command)
                client_socket.send("Invalid command. Please try again.".encode())
            client_socket.close()
    
    def create_account(self, name, balance):
        customer = Customer(name, balance)
        self.customers[customer.account_number] = customer
        print(f"Account for: {customer.name} with balance: {balance} and the account number is: {customer.account_number}")
        customer_data = {
                "name": customer.name,
                "balance": customer.balance,
                "account_number": customer.account_number
            }
        with open(f"customers/{customer.account_number}.json", "w") as file:
            json.dump(customer_data, file)
        return customer.account_number
    

    def deposit(self, account_number, name, amount):
        customer = self.customers.get(account_number)
        if customer and customer.name == name:
            customer.balance += amount
            print(f"Deposited {amount} to account of {customer.name}. New balance: {customer.balance}")
            self.update_customer_data(customer)  
        else:
            print("Account number and name do not match or account not found.")

    def withdraw(self, account_number, name, amount):
        customer = self.customers.get(account_number)
        if customer and customer.name == name:
            if customer.balance >= amount:
                customer.balance -= amount
                print(f"Withdrew {amount} from account of {customer.name}. New balance: {customer.balance}")
                self.update_customer_data(customer)  
            else:
                print("Insufficient balance.")
        else:
            print("Account number and name do not match or account not found.")


    def transfer(self, from_account, from_name, to_account, to_name, amount):
        from_customer = self.customers.get(from_account)
        to_customer = self.customers.get(to_account)
        if from_customer and from_customer.name == from_name and to_customer and to_customer.name == to_name:
            if from_customer.balance >= amount:
                from_customer.balance -= amount
                to_customer.balance += amount
                print(f"Transferred {amount} from {from_customer.name} to {to_customer.name}")
                self.update_customer_data(from_customer)  
                self.update_customer_data(to_customer)    
            else:
                print("Insufficient balance.")
        else:
            print("Invalid account number or name.")

    def update_customer_data(self, customer):
        customer_data = {
            "name": customer.name,
            "balance": customer.balance,
            "account_number": customer.account_number
        }
        with open(f"customers/{customer.account_number}.json", "w") as file:
            json.dump(customer_data, file)


def main():
    bank = Bank()
    bank.start_listen()


if __name__ == "__main__":
    main()