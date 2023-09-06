import math 
total_sum = 0
for number in range(1, 101):
    total_sum += number
print(total_sum)

def find_nearest_integer(number):
    return round(number)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    print(find_nearest_integer(5))
    print(find_nearest_integer(6))
    print(find_nearest_integer(7))
    print(find_nearest_integer(8))
    
    print(is_prime(5))
    print(is_prime(6))
    print(is_prime(7))
    print(is_prime(14))
    print(is_prime(152))
    print(is_prime(60693))

if __name__ == "__main__":
    main()
