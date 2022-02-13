import requests
import json
import time
import re
import textwrap

class Film:
    def __init__(self):
        self.dongu = True

    def program(self):
        secim = self.menu()
        if secim=="1":
            self.top250()
        if secim=="2":
            self.populer()
        if secim=="3":
            self.sinemalarda()
        if secim=="4":
            self.yakında()
        if secim=="5":
            self.arama()
        if secim=="6":
            self.cıkıs()
        
    def menu(self):
        def kontrol(secim):
            if re.search("[^1-6]",secim):
                raise Exception("Lütfen 1 ve 6 arasında geçerli bir sayı giriniz!!!")
        while True:
            try:
                secim=input("Merhabalar, Lütfen Yapmak İstediğiniz İşlemi Seçiniz...\n\n[1]-En İyi 250 Film\n[2]-En Popüler Filmler\n[3]-Sinemalarda\n[4]-Yakında\n[5]-Film Ara\n[6]-Çıkış\n\n...:")
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(2)
            else:
                break
        return secim
        
    def top250(self):
        print("En İyi 250 film listesine ulaşılıyor..\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_63e6m63r")
        sonuc = url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()
    
    def populer(self):
        print("En Popüler film listesine ulaşılıyor..\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/MostPopularMovies/k_63e6m63r")
        sonuc = url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()
    
    def sinemalarda(self):
        print("Sinemalardaki film listesine ulaşılıyor..\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/InTheaters/k_63e6m63r")
        sonuc = url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()
    
    def yakında(self):
        print("Yakında Çıkacak Olacak filmler listesine ulaşılıyor..\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/ComingSoon/k_63e6m63r")
        sonuc = url.json()
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()
        
    def arama(self):

        print("Film Arama Menüsüne Ulaşılıyor..\n")
        time.sleep(2)
        film=input("Lütfen Film Adını Giriniz...:")

        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_63e6m63r")
        sonuc = url.json()

        Id=list()
        for i in sonuc["items"]:
            Id.append(i["id"])

        Ad=list()
        for i in sonuc["items"]:
            Ad.append(i["title"])
        
        cevir=zip(Ad,Id)
        veri=dict(cevir)
        key=veri.get(film)

        url2=requests.get("https://imdb-api.com/tr/API/Wikipedia/k_63e6m63r/{}".format(key))
        sonuc2=url2.json()
    
        print(textwrap.fill(sonuc2["plotShort"]["plainText"]),130)      
    
        self.menudon()


    def cıkıs(self):
        print("Çıkış Yapılıyor...")
        time.sleep(2)
        self.dongu=False
        exit()

    def menudon(self):
        while True:
            x=input("Ana menüye dönmek için 7'e çıkmak için lütfen 6'a basınız...:")
            if x=="7":
                print("Ana menüye dönülüyor...")
                time.sleep(2)
                self.program()
                break
            elif x=="6":
                self.cıkıs()
                break
            else:
                print("Lütfen Geçerli Bir Seçim Yapınız...")



Sistem=Film()
while Sistem.dongu:
    Sistem.program()