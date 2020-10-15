import random

print("""
*****************************************************************
Sayı Tahmin Etme Oyunununa Hoşgeldiniz!

1 ile 100 arasında rastgele bir sayı sayı belirlenecek
O sayıyı tahmin etmeye çalış tahminine göre ipuçları verilececek

Puanın başlangıçta 100 her yanlış tahminin 5 puan götürecek

Çıkmak için tahmin yerine 'q' yazınız
*****************************************************************
""")
while True:
    sayı = random.randint(1,100)
    puan = 100
    while True:
        tahmin = input("Tahmin Et:")
        if tahmin == 'q':
            print("Çıkılıyor...")
            exit()
        else:
            tahmin = int(tahmin)
            if tahmin < sayı:
                print("Az oldu, büyüt")
                puan -= 5
            elif tahmin > sayı:
                print("Fazla oldu, Küçült")
                puan -=5
            else:
                print("Doğru Bildin\nPuanın:{}".format(puan))
                break




