from cmath import sqrt

def is_prime(number):
    if number % 2 == 0 and number != 2:
        return False
    for n in range(3, int(sqrt(number).real) +1, 2):
        if number % n == 0:
            return False
    return True

n = int(input('Введіть чісло: '))
print(is_prime(n))
