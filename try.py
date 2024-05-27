import math
import time
import threading

def is_prime_threading(n):
    if n > 6 :
        if n % 6 == 1 or 5 :                                    #Wheel Factorization
            modList = []
            for i in range(2,int(math.sqrt(n))+1):              #Trial Division Method

                m =n % i
                modList.append(m)
                if m != 0:
                    break
            if modList.count(0) == 0:
                print(n,"is Prime\n")
                return True
                #PrimeList.append(n)
            else:
                print(n, "is not Prime\n")
                return False
        else:
            print(n,"is not Prime\n")
            return False

def isPrime(n):
    if n > 6:
        if n % 6 == 1 or 5:  # Wheel Factorization
            modList = []
            for i in range(2, int(math.sqrt(n)) + 1):  # Trial Division Method

                m = n % i
                modList.append(m)
                if m != 0:
                    break
            if modList.count(0) == 0:
                print(n, "is Prime\n")
                return True
                # PrimeList.append(n)
            else:
                print(n, "is not Prime\n")
                return False
        else:
            print(n, "is not Prime\n")
            return False
    elif n > 1:
        modList = []
        for i in range(2, int(math.sqrt(n)) + 1):  # Trial Division Method

            m = n % i
            modList.append(m)
        if modList.count(0) == 0:
            print(n, "is Prime")
            #PrimeList.append(n)
        else:
            print(n, "is not Prime")
    else:
        print(n, "is not Prime")