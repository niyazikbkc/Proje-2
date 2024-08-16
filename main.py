import json

def kisiekle():
    ad = input("Kişinin adını giriniz: ")
    no = input("Kişinin numarasını giriniz: ")
    kisi = {"Adi": ad, "Numarasi": no}

    try:
        with open("rehber.json", "r") as dosya:
            rehber = json.load(dosya)
    except (FileNotFoundError, json.JSONDecodeError):
        rehber = []

    rehber.append(kisi)

    with open("rehber.json", "w") as dosya:
        json.dump(rehber, dosya, indent=4)

def listele():
    try:
        with open("rehber.json", "r") as dosya:
            rehber = json.load(dosya)
        for kisi in rehber:
            print(f"Adı: {kisi['Adi']}, Numarası: {kisi['Numarasi']}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Rehber boş veya okunamıyor.")

def ara():
    aranan = input("Aranan isim: ")
    try:
        with open("rehber.json", "r") as dosya:
            rehber = json.load(dosya)
        for kisi in rehber:
            if kisi["Adi"] == aranan:
                print(f"Bulundu: Adı: {kisi['Adi']}, Numarası: {kisi['Numarasi']}")
                return
        print("Kişi bulunamadı.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Rehber boş veya okunamıyor.")

def duzelt():
    aranan = input("Düzeltilecek isim: ")
    try:
        with open("rehber.json", "r") as dosya:
            rehber = json.load(dosya)
        for kisi in rehber:
            if kisi["Adi"] == aranan:
                yeniAd = input("Yeni ad: ")
                yeniNo = input("Yeni numara: ")
                kisi["Adi"] = yeniAd
                kisi["Numarasi"] = yeniNo
                with open("rehber.json", "w") as dosya:
                    json.dump(rehber, dosya, indent=4)
                print("Kişi bilgileri güncellendi.")
                return
        print("Kişi bulunamadı.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Rehber boş veya okunamıyor.")

def sil():
    aranan = input("Silinecek isim: ")
    try:
        with open("rehber.json", "r") as dosya:
            rehber = json.load(dosya)
        rehber = [kisi for kisi in rehber if kisi["Adi"] != aranan]
        with open("rehber.json", "w") as dosya:
            json.dump(rehber, dosya, indent=4)
        print("Kişi silindi.")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Rehber boş veya okunamıyor.")

def menu():
    print("╔═══════════════════╗")
    print("║ REHBER UYGULAMASI ║")
    print("║ 1 - Kişi Ekle     ║")
    print("║ 2 - Listele       ║")
    print("║ 3 - Ara           ║")
    print("║ 4 - Düzelt        ║")
    print("║ 5 - Sil           ║")
    print("║ 0 - Çıkış         ║")
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
    else:
        print("Geçersiz seçim!")
        menu()

menu()
