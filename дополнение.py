primes = []
not_primes = []
k = 0

for i in range(1000):
    is_prime = True
    for j in range(2, i):
        k += 1
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)


print("кол во операций проделаных компьютером: ",k)
print("простые числа: ",primes)
print("сложные числа: ",not_primes)

# это дополнение к заданию по циклу for с выводом количества операций для поиска всех простых до любого значения(я написал 1000)