jawab = "NG190041"
password = "01234567891"

jawab = input("Masukkan nombor id anda: ")

while jawab != "NG190041":
    jawab = input("Nombor id anda tiada dalam sistem.")
    password = input("Masukkan kata laluan anda: ")
    while password != "01234567891":
        password = input("Kata laluan yang salah, sila cuba lagi.\nMasukkan kata laluan anda: ")
else:
    for i in range (3):
        print("Selamat Datang")