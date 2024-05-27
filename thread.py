import threading
import math
import time

startTime = time.time()

numbers = list(range(100000))

def isPrime(n):
    if n > 6 :
        if n % 6 == 1 or 5 :                                    #Wheel Factorization
            modList = []
            for i in range(2,int(math.sqrt(n))+1):              #Trial Division Method

                m =n % i
                modList.append(m)
                if m != 0:
                    break
            if modList.count(0) == 0:
                pass#print(n,"is Prime\n")
                #PrimeList.append(n)
            else:
                pass#print(n, "is not Prime\n")
        else:
            pass#print(n,"is not Prime\n")
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

def isPrimeList(numberList):
    for n in numberList:
        if n > 6 :
            if n % 6 == 1 or 5 :                                    #Wheel Factorization
                modList = []
                for i in range(2,int(math.sqrt(n))+1):              #Trial Division Method

                    m =n % i
                    modList.append(m)
                    if m == 0:
                        break
                if modList.count(0) == 0:
                    print(n, "is Prime\n")
                    return True#print(n,"is Prime\n")
                    #PrimeList.append(n)
                else:
                    print(n, "is not Prime\n")
                    return False#
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


"""t1 = threading.Thread(target=isPrime,args=(1976541,),daemon=True)
t2 = threading.Thread(target=isPrime,args=(24815323469403931728221172233738523533528335161133543380459461440894543366372904768334987264000000000000000000479,),daemon=True)
t3 = threading.Thread(target=isPrime,args=(139193,),daemon=True)
t4 = threading.Thread(target=isPrime,args=(489167,),daemon=True)

t1.start()
#t2.start()
t3.start()
t4.start()

t1.join()
#t2.join()
t3.join()
t4.join()"""

"""threads = []

for number in numbers:
    t = threading.Thread(target=isPrime,args=(number,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
"""

threads = []

numbers0 = list(range(0,24499999))
numbers1 = list(range(25000000,49999999))
numbers2 = list(range(50000000, 74999999))
numbers3 = list(range(75000000, 100000000))

t0 = threading.Thread(target=isPrimeList,args=(numbers0,))
t1 = threading.Thread(target=isPrimeList,args=(numbers1,))
t2 = threading.Thread(target=isPrimeList,args=(numbers2,))
t3 = threading.Thread(target=isPrimeList,args=(numbers3,))

t0.start()
t1.start()
t2.start()
t3.start()

threads.append(t0)
threads.append(t1)
threads.append(t2)
threads.append(t3)

for thread in threads:
    thread.join()

finishTime = time.time()
print("used time : ",(finishTime-startTime))