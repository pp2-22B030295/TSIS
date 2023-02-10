def reverse(s):
    for i in range(-1 , -(len(s)) ,-1):
        print(s[i] , end = " ")
        

x = input().split(" ")
reverse(x)
print("\b" , x[0])