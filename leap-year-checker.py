tahun = int(input("Masukkan tahun untuk semakan: "))

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print(str(tahun),"ialah tahun lompat.")
        else:
            print(str(tahun),"bukan tahun lompat.")
    else:
        print(str(tahun),"ialah tahun lompat.")
else:
    print(str(tahun),"bukan tahun lompat.")