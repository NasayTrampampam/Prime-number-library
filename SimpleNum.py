def nextPrime(inputNum):
    for nextNumToChk in range(inputNum+1, inputNum +200):
        if nextNumToChk > 1:
            # If num is divisible by any number between 2 and val, it is not prime
            for i in range(2, nextNumToChk):
                if (nextNumToChk % i) == 0:
                    break
            else:
                #found the prime
                return nextNumToChk

def all_divisors(n: int) -> list:  # находем все делители число
    a = 1
    div = []
    div2 = []
    end = n**0.5  # мы идем до корня из числа потому-что у всех делителей до этого числа есть пара из оставшихся
    while a < end:  # проверяем каждое число, является ли делителем n
        if n % a == 0:  # если да то добавляем его в список и его пару в другой список
            div.append(a)
            div2.insert(0, n//a)
        a += 1
    if int(n**0.5) == n**0.5:
        div.append(n**0.5)
    return div+div2  # возвращаем списки


def isPrime(n: int) -> bool:  # проверяем на простоту
    c = len(all_divisors(n))
    if c == 2:  # если всего у числа два делителя то оно простое
        return True
    else:
        return False

def sieve_of_eratosthenes(last: int) -> list[int]:
    if last < 2:
        return list()
    sieve: list = list(range(2, last+1))
    marker = 0
    for a in range(int(len(sieve)**0.5)):
        if sieve[a] == marker:
            continue
        c = a+sieve[a]
        while c < len(sieve):
            sieve[c] = marker
            c += sieve[a]
    ret = list()
    for i in sieve:
        if i != marker:
            ret.append(i)
    return ret

