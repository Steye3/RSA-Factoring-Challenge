import sys

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def factorize(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0 and is_prime(i):
            j = number // i
            if is_prime(j):
                return i, j
    return None

def process_file(filename):
    with open(filename, 'r') as file:
        number = int(file.read().strip())
        factors = factorize(number)
        if factors is not None:
            p, q = factors
            print(f"{number}={p}*{q}")
        else:
            print("No prime factorization found.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)
    filename = sys.argv[1]
    process_file(filename)

