import sys

def factorize(number):
    factors = []
    for i in range(2, number):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

def process_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            factors = factorize(number)
            for factor in factors:
                print(f"{number}={factor[0]}*{factor[1]}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    filename = sys.argv[1]
    process_file(filename)
