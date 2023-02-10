def filter_prime(l):
    l1 = []
    for i in l:
        k = False
        if int(i) > 1:
            for j in range(2, int(i)):
                if int(i) % j != 0:
                    k = True 
                else:
                    break
        if k:
            l1.append(int(i))  
        k = False             
    print(l1)

x = input().split(" ")
filter_prime(x)