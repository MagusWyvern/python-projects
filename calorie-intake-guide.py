print("**CADANGAN JUMLAH KALORI YANG DIBENARKAN BERDASARKAN JANTINA DAN UMUR**")

jantina = input("Adakah jantina anda lelaki? (Ya atau Tidak): ")


if jantina == "Ya" or "ya" or "y" or "Y":
    umur = int(input("Berapakah Umur Anda? "))
    
    if (umur >= 60):
        print("Nilai kalori yang dibenarkan ialah 2010")
        
    elif (umur >= 30):
        print("Nilai kalori yang dibenarkan ialah 2460")
        
    elif (umur >= 19):
        print("Nilai kalori yang dibenarkan ialah 2440")
        
    elif (umur >= 16):
        print("Nilai kalori yang dibenarkan ialah 2840")
        
    elif (umur >= 13):
        print("Nilai kalori yang dibenarkan ialah 2690")
        
    else:
        print("Maaf, had umur perlu 13 tahun ke atas.")
        
elif jantina == "Tidak" or "tidak" or "T" or "Tak" or "tak":
    umur = int(input("Berapakah Umur Anda? "))
    
    if (umur >= 60):
        print("Nilai kalori yang dibenarkan ialah 1780")
        
    elif (umur >= 30):
        print("Nilai kalori yang dibenarkan ialah 2180")
        
    elif (umur >= 19):
        print("Nilai kalori yang dibenarkan ialah 2000")
        
    elif (umur >= 16):
        print("Nilai kalori yang dibenarkan ialah 2050")
        
    elif (umur >= 13):
        print("Nilai kalori yang dibenarkan ialah 2180")
        
    else:
        print("Maaf, had umur perlu 13 tahun ke atas.")
        
else:
    print("Terima Kasih")
    