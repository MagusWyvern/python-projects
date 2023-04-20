print("Selamat datang ke portal e-keputusan 2020!")
print("============")
namas=input("Masukkan nama pelajar: ")
print("============")
nama=namas.upper()
subjeks=input("Masukkan Subjek: ")
print("============")
subjek=subjeks.title()
markah=int(input("Masukkan markah: "))

if markah <= 34:
    gred = "F"
elif markah <= 39:
    gred = "E"
elif markah <= 44:
    gred = "D"
elif markah <= 49:
    gred = "C-"
elif markah <= 54:
    gred = "C"
elif markah <= 59:
    gred = "C+"
elif markah <= 64:
    gred = "B-"
elif markah <= 69:
    gred = "B"
elif markah <= 74:
    gred = "B+"
elif markah <= 79:
    gred = "A-"
elif markah <= 84:
    gred = "A"
else:
    gred = "A+"

try:
    print("============")
    print("", nama, "\n", subjek, "\n", markah, "\n", gred)
    print("============")
except:
    print("An Error occured")

forsa = input()
