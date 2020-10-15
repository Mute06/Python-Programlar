
print("""
****************************
Sonsuz Sayı Toplama Programı

Çıkmak için 'q' yazınız.
****************************
""")




toplam = 0
while True:

    sayı = input("Sayı:")
    if sayı == "q":
        print("Toplam:",toplam)
        islem = input("Devam etmek için 'c'  Çıkmak için 'q' yazınız:")
        if islem == "c":
            toplam = 0
            continue

        elif islem== "q":
            break

    else:
        sayı = float(sayı)
        toplam+=sayı

