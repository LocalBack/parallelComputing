import math
import time

startTime = time.time()
numbers = list(range(100000000))
def isPrime(n):
    if n > 6 :
        if n % 6 == 1 or 5 :                                    #Wheel Factorization
            modList = []
            for i in range(2,int(math.sqrt(n))+1):              #Trial Division Method

                m =n % i
                modList.append(m)
                if m == 0:
                    break
            if modList.count(0) == 0:
                return True#print(n,"is Prime\n")
                #PrimeList.append(n)
            else:
                return False#print(n, "is not Prime\n")
        else:
            return False#print(n,"is not Prime\n")
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

for number in numbers:
    isPrime(number)

finishTime = time.time()
print("used time : ",(finishTime-startTime))
