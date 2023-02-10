def solve(numheads, numlegs):
    hr , hc = 0 , 0
    lr , lc = 4 * hr , 2 * hc
    hr + hc == numheads
    hr = (numlegs - 2 * numheads) / 2
    hc = numheads - hr 
    print("There are" , hr , "rabbits")
    print("There are" , hc , "chickens")
h = int(input()) #35
l = int(input()) #94
solve(h , l)