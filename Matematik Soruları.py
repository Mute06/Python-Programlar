import random
import time
islemler = ["+","-","x","/"]
hak = 3
puan = 0
print("""
Sana Sorular Sorulucak 3 yanlış bilme hakkın var hakların biterse oyun biter.

Pas geçmek için 'pas' yazınız.

Oyundan çıkmak için 'cık' veya 'çık' yazınız

Puanınızı görmek için 'puan' yazınız

""")



while True:
    sayı1 = random.randint(1,100)
    sayı2 = random.randint(2,20)
    islem = random.choice(islemler)
    if islem == "+":
        sonuc = str(sayı1+sayı2)
        print(sayı1,"+",sayı2,"=")
        cevap = input("Cevap:")
        if cevap == "pas":
            print("Pas Geçildi")
            continue

        elif cevap == sonuc:
            print("5 puan kazandınız!")
            puan+=5
            continue
        elif cevap == "çık" or cevap == "cık":
            print("Puanınız:",puan)
            time.sleep(4)
            break
        elif cevap == "puan":
            print("Şimdi ki puanınız:",puan)
        else:
            print("Yanlış Cevap.\nDoğru cevap:", sonuc, "\n3 puan kaybettiniz")
            puan-=3
            hak-=1
            continue

    elif islem == "-":
        sonuc = str(sayı1-sayı2)
        print(sayı1, "-", sayı2, "=")
        cevap = input("Cevap:")
        if cevap == "pas":
            print("Pas Geçildi")
            continue

        elif cevap == sonuc:
            print("5 puan kazandınız!")
            puan += 5
            continue
        elif cevap == "çık" or cevap == "cık":
            print("Puanınız:", puan)
            time.sleep(4)
            break
        elif cevap == "puan":
            print("Şimdi ki puanınız:",puan)
        else:
            print("Yanlış Cevap.\nDoğru cevap:", sonuc, "\n3 puan kaybettiniz")
            puan -= 3
            hak-=1
            continue

    elif islem == "*":
        sonuc = str(sayı1*sayı2)
        print(sayı1, "x", sayı2, "=")
        cevap = input("Cevap:")
        if cevap == "pas":
            print("Pas Geçildi")
            continue

        elif cevap == sonuc:
            print("5 puan kazandınız!")
            puan += 5
            continue
        elif cevap == "çık" or cevap == "cık":
            print("Puanınız:", puan)
            time.sleep(4)
            break
        elif cevap == "puan":
            print("Şimdi ki puanınız:",puan)
        else:
            print("Yanlış Cevap.\nDoğru cevap:",sonuc,"\n3 puan kaybettiniz")
            puan -= 3
            hak-=1
            continue

    elif islem == "/":
        if sayı1 % sayı2 == 0:

            sonuc = int(sayı1/sayı2)
            print(sayı1, "/", sayı2, "=")
            cevap = int(input("Cevap:"))
            if cevap == "pas":
                print("Pas Geçildi")
                continue

            elif cevap == sonuc:
                print("5 puan kazandınız!")
                puan += 5
                continue
            elif cevap == "çık" or cevap == "cık":
                print("Puanınız:", puan)
                time.sleep(4)
                break
            elif cevap == "puan":
                print("Şimdi ki puanınız:", puan)
            else:
                print("Yanlış Cevap.\nDoğru cevap:", sonuc, "\n3 puan kaybettiniz")
                puan -= 3
                hak-=1
                continue
        else:
            bolen_listesi = []
            for i in range(1,sayı1+1):
                if sayı1 % i == 0:
                    bolen_listesi.append(i)
            sayı2 = random.choice(bolen_listesi)
            
            sonuc = int(sayı1 / sayı2)
            print(sayı1, "/", sayı2, "=")
            cevap = int(input("Cevap:"))
            if cevap == "pas":
                print("Pas Geçildi")
                continue

            elif cevap == sonuc:
                print("5 puan kazandınız!")
                puan += 5
                continue
            elif cevap == "çık" or cevap == "cık":
                print("Puanınız:", puan)
                time.sleep(4)
                break
            elif cevap == "puan":
                print("Şimdi ki puanınız:", puan)
            else:
                print("Yanlış Cevap.\nDoğru cevap:", sonuc, "\n3 puan kaybettiniz")
                puan -= 3
                hak -= 1
                continue


