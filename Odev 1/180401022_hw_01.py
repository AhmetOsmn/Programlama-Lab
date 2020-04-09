"""
Aşagıdaki metodlar OzgurKucet'ten yazılmıştır.
Amacım sadece bir şeyler öğrenmeye çalışmak.

"""

def kelime_sayisi(cumle):
    for kelimeler in cumle:
        for kelime in kelimeler:
            kelime = kelimeler.split()
            if(len(kelime) > 5):
                return -1
    return 1

def input_oku(dosya_ismi):
    with open(dosya_ismi,"r") as dosya:
        cumleler = dosya.readlines()
        return cumleler

def dosya_oku(dosya_adi):
    with open(dosya_adi,"r") as dosya:
        tum_kelimeler = []
        dosya_icerik  = dosya.read()                  #dosyadan verileri aldık
        kelimeler = dosya_icerik.split()              #split fonksiyonu liste döndürecek

        for kelime in kelimeler:                      #split ile ayırdıgımız kelimelerden olusan "kelimeler" listesindeki elemanları "tum_kelimeler" listesine atıyoruz.
            tum_kelimeler.append(kelime)

        tum_kelimeler = sembol_temizle(tum_kelimeler) #en sonunda "tum_kelimeler" listesindeki sembolleri sildik.
    return tum_kelimeler


def sembol_temizle(tum_kelimeler):
    temiz_kelimeler = []
    semboller = "!'^+%&/()=?_>£#$½{[]}\|,.:;/*"

    for kelime in tum_kelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime = kelime.replace(sembol,"")  #replace fonksiyonunun görevi girilen ilk kavramı girilen ikinci kavram ile her yerde değiştiriyor.
        if(len(kelime) > 0):
            temiz_kelimeler.append(kelime)

    return temiz_kelimeler


def sozluk_olustur(tum_kelimeler):
    kelime_sayilari = {}

    for kelime in tum_kelimeler:
        if kelime in kelime_sayilari:
            kelime_sayilari[kelime] += 1 #eğer sözlüğümüzde daha onceden var ise valuesini 1 arttır
        else:
            kelime_sayilari[kelime] = 1 #eğer sözlükte yok ise,sözlüğe ekle ve valuesini 1 yap

    return kelime_sayilari

def sonraki_kelime(tum_kelimeler,kelime):
    liste = kelime.split()
    liste2 = []

    for i in range(len(tum_kelimeler)-1):
        for j in range(len(liste)):
            if tum_kelimeler[i] == liste[j]:
                i += 1
                if(j == len(liste)-1):
                    liste2.append(tum_kelimeler[i])
    return liste2

def sozlukte_buyuk_olan(sozluk):
    en_buyuk = 0

    try:
        for kelime,value in sozluk.items():
            if(value > en_buyuk):
                en_buyuk = value
                en_cok_gecen = kelime

        return en_cok_gecen

    except UnboundLocalError:
        print("hata")

def kelimeyi_oner(input_cumleler):
    out_put = open("output.txt","w")
    for kelimeler in input_cumleler:

        kelime = kelimeler.split()
        kelime1 = str()

        for i in range(len(kelime)):
            if i != len(kelime)-1:
                kelime1 += str(kelime[i] + " ")
            else:
                kelime1 += str(kelime[i])

        try:
            liste = sonraki_kelime(tum_kelimeler,kelime1)
            kelime_sayisi = sozluk_olustur(liste)
            en_cok_gecen = sozlukte_buyuk_olan(kelime_Sayisi)
            out_put.write(kelime1+" "+kelimeyi_oner + "/n") #output dosyasına en çok kullanılan kelimeyi yazdık

        except TypeError:
            dosya_output.write("Kelime bulunamadı.")
