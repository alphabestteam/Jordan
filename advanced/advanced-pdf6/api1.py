import socket
import json

class BankClientAPI:
    def __init__(self, server_host, server_port):
        self.server_host = server_host
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_host, self.server_port))

    def send_request(self, request):
        try:
            self.client_socket.send(request.encode('utf-8'))
            response = self.client_socket.recv(1024).decode('utf-8')
            return response
        except Exception as e:
            return f"Error: {str(e)}"

    def create_account(self, name, balance):
        request = f"create_account {name} {balance}"
        return self.send_request(request)
    def deposit(self, account_number, name, amount):
        request = f"deposit {account_number} {name} {amount}"
        return self.send_request(request)

    def withdraw(self, account_number, name, amount):
        request = f"withdraw {account_number} {name} {amount}"
        return self.send_request(request)

    def transfer(self, from_account, from_name, to_account, to_name, amount):
        request = f"transfer {from_account} {from_name} {to_account} {to_name} {amount}"
        return self.send_request(request)

    def close_connection(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = BankClientAPI('127.0.0.1', 12345)
    while True:
        command = input("Enter command (create_account, deposit, withdraw, transfer, exit): ")
        if command == "create_account":
            name = input("Enter name: ")
            balance = float(input("Enter initial balance: "))
            response = client.create_account(name, balance)
            print(response)
        elif command == "deposit":
            account_number = int(input("Enter account number: "))
            name = input("Enter your name: ")
            deposit_amount = float(input("Enter deposit amount: "))
            response = client.deposit(account_number, name, deposit_amount)
            print(response)
        elif command == "withdraw":
            account_number = int(input("Enter account number: "))
            name = input("Enter your name: ")
            withdraw_amount = float(input("Enter withdrawal amount: "))
            response = client.withdraw(account_number, name, withdraw_amount)
            print(response)
        elif command == "transfer":
            from_account = int(input("Enter your account number: "))
            from_name = input("Enter your name: ")
            to_account = int(input("Enter recipient's account number: "))
            to_name = input("Enter recipient's name: ")
            amount = float(input("Enter transfer amount: "))
            response = client.transfer(from_account, from_name, to_account, to_name, amount)
            print(response)
        elif command == "exit":
            client.close_connection()
           

