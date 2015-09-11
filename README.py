# projet-euler
Question 1

resultat = 0

for i in range(1, 1000):

    if i%3 == 0 or i%5 == 0:

        resultat += i

print(resultat)

R :233168

Question 2

a, b = 1, 2

resultat = 0

while b <= 4000000:

    if b % 2 == 0:

        resultat += b

    a, b = b, a + b

print(resultat)

R :4613732

Question 3 

def is_prime(nb):

    if nb == 1:

        return False

    if nb == 2:

        return True

    elif nb%2 == 0:

        return False

    for i in range(3, int(nb**0.5)+1, 2):

        if nb%i == 0:

            return False

    return True

def divisors(nb, extremum = False):

    divisors = []

    inf = 1 if extremum else 2

    for i in range(inf, int(nb**0.5)+1):

        q, r = divmod(nb, i)

        if r == 0:

            if q >= i:

                divisors.append(i)

                if q > i:

                    divisors.append(nb//i)

    return divisors

#Tri des diviseurs dans l'ordre décroissant

divs = divisors(600851475143)

divs.sort(reverse=True)

#Lit un par un les diviseurs et teste s'ils sont premiers.

#Si c'est le cas, on affiche le diviseur et sort de la boucle.

for i in divs:

    if is_prime(i):

        print(i)

        break

 R :  6857

Question 4

def has_2factors_3digits(nb):

    for i in range(int(nb**0.5)+1, 99, -1):

        q, r = divmod(nb, i)

        if r == 0:

            if len(str(q)) == 3:

                return True

            elif len(str(q)) > 3:

                return False

    return False

i = 997799

j = 1

while i > 10000:

    if has_2factors_3digits(i):

        print(i)

        break

    if j%10 == 8:

        i -= 110

    else:

        i -= 1100

    j += 1

R : 906609

Question 5

print(2*2*2*2*3*3*5*7*11*13*17*19)

R : 232792560
