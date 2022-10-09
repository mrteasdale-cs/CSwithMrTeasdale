def primes(n):
    primesav = []
    primesav.append(1)
    primesav.append(2)

    for i in range(1, n + 1):
        counter = 0
        if i % 2 == 1:
            temp = i
        for j in range(1, temp + 1):
            if temp % j == 0:
                counter += 1

        if counter == 2:
            primesav.append(temp)

    tempor = []
    [tempor.append(x) for x in primesav if x not in tempor]
    print(tempor)

    return tempor


def stairs(n):
    dictionary = dict()
    for x in range(0, n+1):
        if x == 0:
            dictionary[x] = 1
        if x == 1:
            dictionary[x] = 1
        if x == 2:
            dictionary[x] = 2
        if x == 3:
            dictionary[x] = 4
        else:
            dictionary[x] = 0

    for u in dictionary.keys():
        if dictionary[u] == 0:
            for k in primes(u):
                temp = u - k
                print("temp is ", temp)
                if temp in dictionary.keys():
                    dictionary[u] += dictionary[temp]

    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return dictionary[n]


def main():
    n = int(input("Enter n: "))
    print(stairs(n))


main()
