import random


def gen(n):
    if n <= 0:
        print("Number of digits must be positive")
        return

    digit1 = random.randint(1, 9)
    num = str(digit1)

    for i in range(n - 1):
        num += str(random.randint(0, 9))

    return int(num)


n = int(input("Enter the number of digits:"))
random_num = gen(n)
print("Random", n, "-digit number:", random_num)
