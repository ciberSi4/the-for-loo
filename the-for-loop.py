# Цикл for. Элементы списка. Полезные функции в цикле

numbers : list= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes : list = []
not_primes : list = []

for i in numbers:
    is_prime: bool = True
    for j in range (2, numbers[i-1]):
        if i % j != 0:
           continue
        elif i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(numbers[i])
    elif is_prime == False:
        not_primes.append(numbers[i-1])

print("Дан список чисел:", numbers)
print("Список простых чисел:", list(primes))
print("Список составных чисел:",list(not_primes))