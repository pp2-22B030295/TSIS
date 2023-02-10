def has_33(l):
    k = False
    for i in range(len(l)):
        if l[i] == 3 & (l[i + 1] == 3 | l[i - 1] == 3):
            print("True")
            break
        

l = []
x = 'df'
while x == "":
    x = str(input())
    l.append(int(x))
has_33(l)
