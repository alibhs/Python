import json
import re
import time
import random

class Site:
    def __init__(self):
        self.dongu=True
        self.veriler = self.verial() #veritabanındaki bilgileri okumak ve veriler isimli objeye tanımlamak

    def program(self):
        secim=self.menu()
        if secim=="1":
            self.giris()
        if secim=="2":
            self.kayıtOl()
        if secim=="3":
            self.cıkıs()

    def menu(self):
        def kontrolsecim(secim):
            if re.search("[^1-3]",secim):
                raise Exception("Lütfen 1 ve 3 arasında geçerli bir seçim yapınız!!!!")
            elif len(secim)!=1:
                raise Exception("Lütfen 1 ve 3 arasında geçerli bir seçim yapınız!!!!")
        while True:
            try:
                secim=input("Merhabalar ali.com'a Hoş Geldiniz.\n\n Lütfen Yapmak İstediğiniz İşlemi Seçiniz..\n\n[1]-Giriş\n[2]-Kayıt Ol\n[3]-Çıkış\n")
                kontrolsecim(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim
        
    def giris(self):
        print("Giriş Menüsüne Yönlendiriliyorsunuz....")
        time.sleep(2)
        Kullaniciadi=input("Lütfen Kullanıcı Adınızı Giriniz:")
        Sifre=input("Lütfen Şifrenizi Giriniz:")
        
        sonuc = self.girisKontrol(Kullaniciadi,Sifre)
        if sonuc == True:
            self.girisBasarili()
        else:
            self.girisBasarisiz()

    def girisKontrol(self,Kullaniciadi,Sifre):
        self.veriler=self.verial()
        try:
            for kullanici in self.veriler["Kullanıcılar"]:
                if kullanici["Kullanıcıadı"]==Kullaniciadi and kullanici["Şifre"]==Sifre:
                    return True
        except KeyError:
            return False
        return False


    def girisBasarili(self):
        print("Kontrol Ediliyor...")
        time.sleep(2)
        print("Giriş Başarılı. Siteye Hoşgeldiniz...")
        self.sonuc=False
        self.dongu=False

    def girisBasarisiz(self):
        print("Kullanıcı Adı veya Şifreniz Hatalı...")
        time.sleep(2)
        self.menuDon()
        
    def kayıtOl(self):
        def kontrolka(Kullaniciadi):
            if len(Kullaniciadi)<8:
                raise Exception("Kullanıcı Adı en az 8 karaterden oluşmalıdır...")
        while True:
            try:
                Kullaniciadi=input("Kullanıcı Adınız : ")
                kontrolka(Kullaniciadi)
            except Exception as hataad:
                print(hataad)
                time.sleep(2)
            else:
                break

        def kontrolsifre(Sifre):
            if len(Sifre)!=8:
                raise Exception("Şifreniz en az 8 karaterden oluşmalıdır...")
            elif not re.search("[0-9]",Sifre):
                raise Exception("Şifrenizde en az bir rakam olmalıdır...")
            elif not re.search("[A-Z]",Sifre):
                raise Exception("Şifrenizde en az bir büyük harf olmalıdır...")
            elif not re.search("[a-z]",Sifre):
                raise Exception("Şifrenizde en az bir küçük harf olmalıdır...")
        while True:
            try:
                Sifre=input("Şifreniz : ")
                kontrolsifre(Sifre)
            except Exception as hataad:
                print(hataad)
                time.sleep(2)
            else:
                break

        def kontrolmail(Mail):
            if not re.search("@" and ".com",Mail):
                raise Exception("Geçerli bir mail adresi giriniz...")
        while True:
            try:
                Mail=input("Mail Adresiniz : ")
                kontrolmail(Mail)
            except Exception as hataad:
                print(hataad)
                time.sleep(2)
            else:
                break
                     
        sonuc=self.kayıtVarmı(Kullaniciadi,Mail)

        if sonuc == True:
            print("Bu kullanıcı adı ve mail sistemde kayıtlı!!")
        else:
            aktivasyonkodu = self.aktivasyonGonder()
            durum=self.aktivasyonKontrol(aktivasyonkodu)
        while True:
            if durum==True:
                self.veriKaydet(Kullaniciadi,Mail,Sifre)
                break
            else: 
                print("Aktivasyon kodunuz hatalı !!!!")
                time.sleep(2)
        self.menuDon()
                

    def kayıtVarmı(self,Kullaniciadi,Mail):
        self.veriler=self.verial()
        try:
            for kullanıcı in self.veriler["Kullanıcılar"]:
                if kullanıcı["Kullanıcıadı"]==Kullaniciadi and kullanıcı["Mail"]==Mail:
                    return True
        except KeyError:
            return False
        return False
            
    def aktivasyonGonder(self):
        with open("C:/Users/Ali/Desktop/aktivasyon.txt","w") as Dosya:
            aktivasyon=str(random.randint(10000,99999))
            Dosya.write("Aktivasyon Kodunuz: "+aktivasyon)
        return aktivasyon

    def aktivasyonKontrol(self,aktivasyon):
        aktivasyonkodual=input("Lütfen Mailinize gelen aktivasyon kodunuzu giriniz :")
        if aktivasyon == aktivasyonkodual:
            return True
        else:
            return False
        
    def verial(self):
        try:
            with open("C:/Users/Ali/Desktop/Kullanıcılar.json","r") as Dosya:
                veriler = json.load(Dosya)
        except FileNotFoundError:
            with open("C:/Users/Ali/Desktop/Kullanıcılar.json","w") as Dosya:
                Dosya.write("{}")
            with open("C:/Users/Ali/Desktop/Kullanıcılar.json","r") as Dosya:
                veriler = json.load(Dosya)
        return veriler



    def veriKaydet(self,Kullaniciadi,Mail,Sifre):
        self.veriler=self.verial()

        try:
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı":Kullaniciadi,"Şifre":Sifre,"Mail":Mail})
        except KeyError:
            self.veriler["Kullanıcılar"]=list()
            self.veriler["Kullanıcılar"].append({"Kullanıcıadı":Kullaniciadi,"Şifre":Sifre,"Mail":Mail})
        with open("C:/Users/Ali/Desktop/Kullanıcılar.json","w") as Dosya:
            json.dump(self.veriler,Dosya,ensure_ascii=False,indent=4)
            print("Kayıt Başarılı...")
            time.sleep(2)
        self.menuDon()



    def cıkıs(self):
        print("Çıkış Yapılıyor...")
        time.sleep(2)
        self.dongu=False
        exit()

    def menuDon(self):
        while True:
            x = input("Ana menüye dönmek için 5 e çıkmak için lütfen 4 e basınız...:")
            if x == "5":
                print("Ana menüye dönülüyor...")
                time.sleep(2)
                self.program()
                break
            elif x == "4":
                print("Çıkış yapılıyor...")
                time.sleep(2)
                self.cıkıs()
                break
            else:
                print("Lütfen Geçerli Bir Değer giriniz")

Sistem = Site()
while Sistem.dongu:
    Sistem.program()