import ast, time

def kisiekle():
    time.sleep(1)
    ad = input("Rehbere Eklenecek Kişinin Adı: ")
    time.sleep(1)
    soyad = input("Rehbere Eklenecek Kişinin Soyadı: ")
    time.sleep(1)
    no = input("Rehbere Eklenecek Kişinin Numarası: ")
    kisi = {"ADI": ad, "SOYADI": soyad, "NUMARASI": no}
    with open("rehber.listesi", "a") as dosya:
        dosya.write(str(kisi) + "\n")

def listele():
    time.sleep(1)
    with open("rehber.listesi", "r") as dosya:
        bbb = dosya.read()
        print(bbb)

def ara():
    time.sleep(1)
    with open("rehber.listesi", "r") as dosya:
        okunan = dosya.read()
        cevirilen = ast.literal_eval("[" + okunan.replace("\n", ",")[:-1] + "]")
        time.sleep(1)
        aranan = input("Aranan İsim: ")
        for a in cevirilen:
            if a["ADI"] == aranan:
                print(a)

def duzelt():
    time.sleep(1)
    with open("rehber.listesi", "r") as dosya:
        okunan = dosya.read()
        cevirilen = ast.literal_eval("[" + okunan.replace("\n", ",")[:-1] + "]")
        time.sleep(1)
        aranan = input("Düzeltilecek İsim: ")
    
    with open("rehber.listesi", "w") as dosya:
        for a in cevirilen:
            if a["ADI"] == aranan:
                print(a)
                time.sleep(1)
                a["ADI"] = input("Düzeltilen Kişinin Rehberdeki Yeni İsmi: ")
                time.sleep(1)
                a["SOYADI"] = input("Düzeltilen Kişinin Rehberdeki Yeni Soyadı: ")
                time.sleep(1)
                a["NUMARASI"] = input("Düzeltilen Kişinin Rehberdeki Yeni Numarası: ")
            dosya.write(str(a) + "\n")

def sil():
    time.sleep(1)
    with open("rehber.listesi", "r") as dosya:
        okunan = dosya.read()
        cevirilen = ast.literal_eval("[" + okunan.replace("\n", ",")[:-1] + "]")
    
    time.sleep(1)
    aranan = input("Silinecek isim: ")
    with open("rehber.listesi", "w") as dosya:
        for a in cevirilen:
            if a["ADI"] != aranan:
                dosya.write(str(a) + "\n")
            else:
                print(f"{aranan} kişisi başarıyla silinmiştir.")

def menu():
    time.sleep(1)
    print("╔═══════════════════╗")
    print("║ REHBER UYGULAMASI ║")
    print("║1-Kişi Ekle        ║")
    print("║2-Listele          ║")
    print("║3-Ara              ║")
    print("║4-Düzelt           ║")
    print("║5-Sil              ║")
    print("║0-Çıkış            ║")
    print("╚═══════════════════╝")
    
    secim = input("Seçiminiz nedir? ")
    if secim == "1":
        kisiekle()
        menu()
    elif secim == "2":
        listele()
        menu()
    elif secim == "3":
        ara()
        menu()
    elif secim == "4":
        duzelt()
        menu()
    elif secim == "5":
        sil()
        menu()
    elif secim == "0":
        print("Çıkış yapılıyor...")
        time.sleep(1)

menu()




          


            




    