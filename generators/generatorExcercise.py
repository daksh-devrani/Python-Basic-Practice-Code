def prime_generator(bound):
    i = 2
    while i < bound:
        j = 2
        while j <= i:

            if i % j == 0 and i != j:
               break

            j += 1
        else :
            yield i

        i += 1

g = prime_generator(20)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))