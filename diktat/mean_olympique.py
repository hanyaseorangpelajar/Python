u = int(input("u = "))
v = int(input("v = "))
w = int(input("w = "))
x = int(input("x = "))

def max2(a,b):
    if a > 0 and b > 0:
        return (a + b + abs(a - b))/2
    else:
        return("Integer harus positif")

def min2(a,b):
    if a > 0 and b > 0:
        return (a + b - abs(a - b))/2
    else:
        return ("Integer harus positif")

def max4(i,j,k,l):
    if i > 0 and j > 0 and k > 0 and l > 0:
        return int(max2(max2(i, j), max2(k, l)))
    else:
        return ("Integer harus positif")

    
def min4(i,j,k,l):
    if i > 0 and j > 0 and k > 0 and l > 0:
        return int(min2(min2(i, j), min2(k, l)))
    else:
        return ("Integer harus positif")

def MO(u,v,w,x):
    if u > 0 and v > 0 and w > 0 and x > 0:
        return ((u+v+w+x-min4(u,v,w,x)-max4(u,v,w,x))/2)
    else:
        return ("Integer harus positif")

print("MO = " + str(MO(u,v,w,x)))

