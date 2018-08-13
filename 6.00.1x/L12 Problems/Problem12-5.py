def genPrimes():
    primes = []
    newprime = 1
    while 1:
        newprime += 1
        for i in primes:
            if newprime % i == 0:
                break
        else:
            primes.append(newprime)
            yield newprime


prime = genPrimes()
print prime.next()
print prime.next()
print prime.next()
print prime.next()
print prime.next()

'''
for i in genPrimes():
    print i
'''
