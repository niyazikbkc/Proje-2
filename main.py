import ast,time

def kisiekle():
    ad = input("Rehbere Eklenecek Kişinin Adı")
    soyad = input("Rehbere Eklencek Kişinin Soyadı")
    no = input("Rehbere Eklenecek Kişinin Numaası")
    kisi = {ad=="ADI",soyad=="Soyadı",no=="NUMARASI"}
    dosya = open("rehber.listesi","a")
    dosya.write(str(kisi)),
    dosya.close()


def listele() 
    aaa=open("rehber.listesi","r")
    bbb=read()
    print(bbb)



def ara ()
        with open ("rehber.listesi","r") as dosya :
            okunan = dosya.read()
            cevirilen = ast.literal_eval(dosya)
            aranan = input (" Aranan İsim : ")
            for a in cevirilen
            if a ["ADI"]== aranan :
                print (a)

def duzelt ()
     with open ("rehber.listesi","r") as dosya :
          okunan = dosya.read()
          cevirilen = ast.literal_eval(dosya)
          aranan = input (" Düzeltilecek İsim : ")
          dosya.close()

          with open ("rehber.list","r") as dosya
          for a in cevirilen 
          if a ["ADI"]== aranan :
               print(a)
          yenisim = input (" Düzeltilen Kişinin Rehberdeki Yeni İsmi : ")     
          yenisoyad = input ("Düzeltilen Kişinin Rehberdeki Yeni Soyadı :")
          yenino = input ("Düzeltilen Kişinin Rehberdeki Yeni Numarası : ")
          a["ADI"]=yeniAd
          a["NUMARASI"]=yeniNo
     dosya.write(f"{str(a)},")


def sil():
    with open("rehber.xx","r") as dosya:
        okunan = dosya.read()
    cevirilen = ast.literal_eval(okunan)
    aranan = input("Silinecek isim:")
    dosya.close()
    with open("rehber.listesi","w") as dosya:
        for a in cevirilen:
            if a["ADI"] != aranan:
                dosya.write(f"{str(a)},")
                






          


            




    