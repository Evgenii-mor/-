numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()

for i in numbers:
    if i == 1:  # число 1 является ни простым, ни составным числом, поэтому его пропускаем.
        continue
    is_prime = True
    if i < 2:
        is_prime = False
    else:
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                is_prime = False

    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)

print('Numbers:', numbers)
print('Primes:', primes)
print('Not Primes:', not_primes)
