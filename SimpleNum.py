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

def all_divisors(n: int) -> list:  # find all divisors of a number
    a = 1
    div = []
    div2 = []
    end = n**0.5  # we go to the root of the number because all divisors up to this number have a pair of the remaining
    while a < end:  #  check each number to see if it's a divisor of n
        if n % a == 0:  # if so, add it to the list and its pair to another list
            div.append(a)
            div2.insert(0, n//a)
        a += 1
    if int(n**0.5) == n**0.5:
        div.append(n**0.5)
    return div+div2 


def isPrime(n: int) -> bool:  # checking for simplicity
    c = len(all_divisors(n))
    if c == 2:  # If a number has two divisors, then it is prime.
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

