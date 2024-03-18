pieces = int(input("Pieces:"))
shirt_price = float(input("Shirt Price:"))
logocal = 0
namacal = 0
a4cal = 0
a3cal = 0
namejerseycal = 0
jerseynoscal = 0
jerseynodcal = 0

def main(pcs, sp, 
    logocal = 0,
    namacal = 0,
    a4cal = 0,
    a3cal = 0,
    namejerseycal = 0,
    jerseynoscal = 0,
    jerseynodcal = 0):

    n = (logocal+namacal+a4cal+a3cal+namejerseycal+jerseynoscal+jerseynodcal+sp)*pcs

    print("Total Price:", n)
    print("Price per piece:", n / pcs)



def logo(pcs, logos):
    global logocal
    if pcs <= 9:
        logocal = float(5.0 * logos)

    elif pcs <= 29:
        logocal = float(4.5 * logos)

    elif pcs <= 49:
        logocal = float(4.0 * logos)

    elif pcs >= 50:
        logocal = float(3.5 * logos)


def nama(pcs, namas):
    global namacal
    if pcs <= 9:
        namacal = float(3.5 * namas)

    elif pcs <= 29:
        namacal = float(3.0 * namas)

    elif pcs <= 49:
        namacal = float(2.7 * namas)

    elif pcs >= 50:
        namacal = float(2.5 * namas)

def a4(pcs, a4s):
    global a4cal
    if pcs <= 9:
        a4cal = float(13.5 * a4s)

    elif pcs <= 29:
        a4cal = float(13.0 * a4s)

    elif pcs <= 49:
        a4cal = float(12.0 * a4s)

    elif pcs >= 50:
        a4cal = float(11.0 * a4s)
    

def a3(pcs, a3s):
    global a3cal
    if pcs <= 9:
        a3cal = float(19.5 * a3s)

    elif pcs <= 29:
        a3cal = float(19.0 * a3s)

    elif pcs <= 49:
        a3cal = float(17.5 * a3s)

    elif pcs >= 50:
        a3cal = float(16.5 * a3s)

def namejersey(pcs, namejerseys):
    global namejerseycal
    if pcs <= 9:
        namejerseycal = float(5.0 * namejerseys)

    elif pcs <= 29:
        namejerseycal = float(4.7 * namejerseys)

    elif pcs <= 49:
        namejerseycal = float(4.5 * namejerseys)

    elif pcs >= 50:
        namejerseycal = float(4.3 * namejerseys)

def jerseynos(pcs, nosjersey):
    global jerseynoscal
    if pcs <= 9:
        jerseynoscal = float(8.0 * nosjersey)

    elif pcs <= 29:
        jerseynoscal = float(7.5 * nosjersey)

    elif pcs <= 49:
        jerseynoscal = float(7.2 * nosjersey)

    elif pcs >= 50:
        jerseynoscal = float(7.0 * nosjersey)

def jerseynod(pcs, nodjersey):
    global jerseynodcal
    if pcs <= 9:
        jerseynodcal = float(12.0 * nodjersey)

    elif pcs <= 29:
        jerseynodcal = float(11.5 * nodjersey)

    elif pcs <= 49:
        jerseynodcal = float(11.0 * nodjersey)

    elif pcs >= 50:
        jerseynodcal = float(10.5 * nodjersey)


while True:
    try:
        pil = input("1- Logo\n2- Nama\n3- A4 Size\n4- A3 Size\n5- Jersey (Name)\n6-Jersey NO (Single Digit)\n7- Jersey NO (Double Digit)\n")
        if pil == "1":
            logos = int(input("Logo count: "))
            logo(pieces, logos)
            continue
        elif pil == "2":
            namas = int(input("Name count: "))
            nama(pieces, namas)
            continue
        elif pil == "3":
            a4s = int(input("A4 Image count: "))
            a4(pieces, a4s)
            continue
        elif pil == "4":
            a3s = int(input("A3 Image count: "))
            a3(pieces, a3s)
            continue
        elif pil == "5":
            namejerseys = int(input("Jersey Name count: "))
            namejersey(pieces, namejerseys)
            continue
        elif pil == "6":
            nosjersey = int(input("Jersey Number (Single Digit) count: "))
            jerseynos(pieces, nosjersey)
            continue
        elif pil == "7":
            nodjersey = int(input("Jersey Number (Double Digit) count: "))
            jerseynod(pieces, nodjersey)
            continue
        elif pil == "cal" or "CAL" or "Calculate":
            print(main(pieces, shirt_price, logocal, namacal, a4cal, a3cal, namejerseycal, jerseynoscal, jerseynodcal))
            
    except:
        print("System break!")
        

