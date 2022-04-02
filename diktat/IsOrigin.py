x = int(input("Masukkan titik pertama = "))
y = int(input("Masukkan titik kedua = "))

def IsOrigin(x, y):
    if x == 0 and y == 0:
        return True
    else:
        return False

print(IsOrigin(x, y))