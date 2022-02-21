import json
import re
import time
import random

class Site:
    def __init__(self):
        self.dongu=True
        self.veriler=self.verial()

    def program(self):
        secim = self.menu()

        if secim =="1":
            self.giris()
        if secim =="2":
            self.kayıtol()
        if secim =="3":
            self.cıkıs()

    def menu(self):
        def kontrolsecim(secim):
            if re.search("[^1-3]",secim):
                raise Exception("Lütfen 1 ve 3 arası bir sayı giriniz!!!")
            elif len(secim)!=1:
                raise Exception("Lütfen 1 ve 3 arası bir sayı giriniz!!!")
        while True:
            try:
                secim = input("AliBahşi.com'a Hoşgeldiniz...\nLütfen Yapmak İstediğiniz İşlemi Seçiniz:\n[1]-Giriş\n[2]-Kayıt Ol\n[3]-Çıkış\n...:")
                kontrolsecim(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim

    def giris(self):
        print("Girişe Yönlendiriliyorsunuz...")
        time.sleep(2)
        Kullanıcıadı=input("Lütfen Kullanıcı Adınızı Giriniz:")
        Sifre=input("Lütfen Şifrenizi Giriniz:")

        sonuc = self.giriskontrol(Kullanıcıadı,Sifre)
        if sonuc == True:
            self.girisbasarili()
        else:
            self.girisbasarisiz()

    def giriskontrol(self,Kullanıcıadı,Sifre):
        self.veriler = self.verial()
        try:
            for kullanıcı in self.veriler["Kullanıcılar"]:
                if kullanıcı["Kullanıcıadı"]==Kullanıcıadı and kullanıcı["Şifre"]==Sifre:
                    return True
        except KeyError:
            return False
        return False

    def girisbasarili(self):
        print("Giriş Başarılı...")
        time.sleep(1)
        self.dongu=False
        self.sonuc=False

    def girisbasarisiz(self):
        print("Giriş Başarısız.. Ana Menüye Yönlendiriliyorsunuz...")
        time.sleep(2)
        self.menudon()

    def kayıtol(self):
        def kontrolka(Kullanıcıadı):
            if len(Kullanıcıadı)<6:
                raise Exception("Kullanıcı Adını en az 6 karakterden oluşmalıdır")
        while True:
            try:
                Kullanıcıadı = input("Lütfen Kullanıcı Adınızı Giriniz:")
                kontrolka(Kullanıcıadı)
            except Exception as hataad:
                print(hataad)
                time.sleep(2)
            else:
                break
        def kontrolsifre(Sifre):
            if len(Sifre)<8:
                raise Exception("Şifreniz en az 8 karakterden oluşmalıdır.")
            elif not re.search("[^0-9]",Sifre):
                raise Exception("Şifreniz en az bir rakamdan oluşmalıdır. ")
            elif not re.search("[^A-Z]",Sifre):
                raise Exception("Şifreniz en az bir Büyük Harf içermelidir.")
            elif not re.search("[^a-z]",Sifre):
                raise Exception("Şifreniz en az bir Küçük Harf içermelidir.")
        while True:
            try:
                Sifre = input("Lütfen Şifreniz Giriniz: ")
                kontrolsifre(Sifre)
            except Exception as hataad:
                print(hataad)
                time.sleep(2)
            else:
                break

        def kontrolmail(Mail):
            if not re.search("@" and ".com", Mail):
                raise Exception("Geçersiz Mail lütfen mailinize @ ve .com ekleyin")
        while True:
            try:
                Mail = input("Lütfen Mail Adresinizi Giriniz:")
                kontrolmail(Mail)
            except Exception as hataad:
                print(hataad)
                time.sleep(2)
            else:
                break

        sonuc = self.kayıtvarmı(Kullanıcıadı,Mail)
        if sonuc == True:
            print("Kullanıcı adı ve Mail Sisteme Kayıtlı!!")
        else:
            aktivasyonkodu = self.aktivasyongonder()
            durum = self.aktivasyonkontrol(aktivasyonkodu)
        while True:
            if durum == True:
                self.verikaydet(Kullanıcıadı,Mail,Sifre)
                break
            else:
                print("Aktivasyon Kodunuz Yanlış...")
                time.sleep(2)
        self.menudon()

            
    def kayıtvarmı(self,Kullanıcıadı,Mail):
        self.veriler = self.verial()
        try:
            for kullanıcı in self.veriler["Kullanıcılar"]:
                if kullanıcı["Kullanıcıadı"]==Kullanıcıadı and kullanıcı["Mail"]==Mail:
                    return True
        except KeyError:
            return False
        return False
            
    def aktivasyongonder(self):
        with open("C:/Users/Ali/Desktop/JsonKayıtVerileri/AktivasyonKodu.txt","w") as Dosya:
            aktivasyon = str(random.randint(100000,999999))
            Dosya.write("Aktivasyon Kodunuz:"+aktivasyon)
        return aktivasyon

    def aktivasyonkontrol(self,aktivasyon):
        aktivasyonkodual=input("Lütfen Aktivasyon kodunuzu giriniz:")
        if aktivasyon == aktivasyonkodual:
            return True
        else:
            return False

    def verial(self):
        try:
            with open("C:/Users/Ali/Desktop/JsonKayıtVerileri/Kullanıcılar.json","r") as Dosya:
                veriler = json.load(Dosya)
        except FileNotFoundError:
            with open("C:/Users/Ali/Desktop/JsonKayıtVerileri/Kullanıcılar.json","w") as Dosya:
                Dosya.write("{}")
            with open("C:/Users/Ali/Desktop/JsonKayıtVerileri/Kullanıcılar.json","r") as Dosya:
                veriler = json.load(Dosya)
        return veriler


    def verikaydet(self,Kullanıcıadı,Mail,Sifre):
        self.veriler = self.verial()
        
        try:
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı":Kullanıcıadı,"Şifre":Sifre,"Mail":Mail})
        except KeyError:
            self.veriler["Kullanıcılar"]=list()
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı":Kullanıcıadı,"Şifre":Sifre,"Mail":Mail})
        with open("C:/Users/Ali/Desktop/JsonKayıtVerileri/Kullanıcılar.json","w") as Dosya:
            json.dump(self.veriler,Dosya,ensure_ascii=False,indent=4)
            print("Kayıt Başarılı...")
            time.sleep(2)
        self.menudon()
        
    def cıkıs(self):
        print("Çıkış Yapılıyor...")
        time.sleep(2)
        self.dongu=False
        exit()
    def menudon(self):
        while True:
            x=input("Lütfen çıkmak için 5 e ana menüye dönmek için 4 e basınız...")
            if x == "5":
                print("Çıkış yapılıyor...")
                time.sleep(2)
                self.cıkıs()
                break
            elif x =="4":
                print("Ana menüye dönülüyor...")
                time.sleep(2)
                self.program()
                break
            else:
                print("Geçerli bir sayı giriniz...")

Sistem = Site()
while Sistem.dongu:
    Sistem.program()