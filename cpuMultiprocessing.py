import time
import math
import multiprocessing as mp

numlist = [101107157131,42962490869760,1252099518401,1268759440032,4666666666667,275311670611,
277535577223,
285311670733,
293826343073,
298999999999,
308457624821,
313191181151,
           6123456789101,
           6123584726269,
           6252893229398,
           6435409832617,
           6440261849537,
           6660000000001,
           6746328388801,
           6763998516837,
           6987191424553,
           7073313533333,
           7134354660743,
           7142857142857,
           7177111117717,
           7184500054817,
           7284717174827,
           7625597484960,
           7625597485003,
           7666466646667
           ]
numlist_ = [37889062373143906,
43142746595714191,
43157099231631693,
44444446666688899,
47784853865664217,
55350776431903243,
55453628211510631,
55555555555555999,
59604644783353249,
59649589127497217,
66555444443333333,
66606660666066601,
69668002914515347,
70000006660000007,
71117012721071117,
71828182828182817,
74747474747474747,
76912895956636885,
77777777977777777,
81615141210198641,
91521253335394951,
93487500801880185,
94350482728405349,
97654321012345679,
98764321012345789]

def isPrime(n):
    if n > 6 :
        if n % 6 == 1 or 5 :                                    #Wheel Factorization
            modList = []
            for i in range(2,int(math.sqrt(n))+1):              #Trial Division Method

                m =n % i
                modList.append(m)
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
                    #return True#print(n,"is Prime\n")
                    #PrimeList.append(n)
                else:
                    print(n, "is not Prime\n")
                    #return False#print(n, "is not Prime\n")
            else:
                print(n, "is not Prime\n")
                #return False#print(n,"is not Prime\n")
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

if __name__ == "__main__":
    start = time.time()

    numbers0 = numlist#list(range(0,24499999))
    numbers1 = numlist_
    #numbers2 = list(range(50000000, 74999999))
    #numbers3 = list(range(75000000, 100000000))

    processes = []

    p0 = mp.Process(target=isPrimeList,args=(numbers0,))
    p1 = mp.Process(target=isPrimeList, args=(numbers1,))
    #p2 = mp.Process(target=isPrimeList, args=(numbers2,))
    #p3 = mp.Process(target=isPrimeList, args=(numbers3,))

    p0.start()
    p1.start()
   # p2.start()
    #p3.start()

    processes.append(p0)
    processes.append(p1)
  #  processes.append(p2)
  #  processes.append(p3)

    for process in processes:
        process.join()


    finish = time.time()
    print("exectime : ", finish-start)