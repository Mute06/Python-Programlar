print("""
****************************
Hesap makinesi programı

İşlemler:

1.Toplama: '+' , 'topla , '1'

2.Çıkarma: '-' , 'eksi' , '2'

3.Çarpma: 'x' , 'kere' , 'çarpı' , '3'

4.Bölme: '/' , 'bölü' , '4'

Çıkmak için 1. sayı  yerine 'q' yazınız
****************************
""")
while True:
    sayı1 = input("1. Sayı:")

    if sayı1 == "q":
        print("Yine Bekleriz.")
        break
    else:
        sayı1 = int(sayı1)
        islem = input("İşlem:")
        sayı2 = int(input("2.Sayı:"))
        if islem == "+" or islem == "topla" or islem == "1":
            sonuc = sayı1 + sayı2
            print("{} + {} = {}".format(sayı1,sayı2,sonuc))

        elif islem == "-" or islem == "eksi" or islem == "2":
            sonuc = sayı1 - sayı2
            print("{} - {} = {}".format(sayı1,sayı2,sonuc))

        elif islem == "x" or islem == "kere" or islem == "3":
            sonuc = sayı1 * sayı2
            print("{} x {} = {}".format(sayı1,sayı2,sonuc))
        elif islem == "/" or islem == "bölü" or islem == "4":
            sonuc = sayı1 / sayı2
            print("{} / {} = {}".format(sayı1,sayı2,sonuc))
        else:
            print("Geçersiz işlem")






