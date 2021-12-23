class Musteri:
    def __init__(self,ad,soyadi,kartsifre,bakiye,kkborc,sonodeme):
        self.ad = ad
        self.soyadi = soyadi
        self.kartsifre = kartsifre
        self.bakiye = bakiye
        self.kkborc = kkborc
        self.sonodeme = sonodeme

Ahmethesap = Musteri("Ahmet","Akdağ",1511,100000,0,None)
MehmetHesap = Musteri("Mehmet","Ercan",9123,23000,50000,"13/08/2022")
TakılanKart = Ahmethesap

class ATM:
    def __init__(self,atmAd):
        self.atmAd = atmAd
        self.girisKontrol()
        self.dongu = True
    
    def girisKontrol(self):
        Hak = 3
        for i in range(0,3):
            Sifre = int(input("Lutfen 4 haneli şifrenizi giriniz :  "))
            if Sifre == TakılanKart.kartsifre:
                self.program()
            elif Sifre != TakılanKart.kartsifre and Hak !=0:
                print("Hatalı Şifre Girdiniz Kalan Hakkınız {} 'dir".format(Hak))
                Hak -=1
            elif Sifre != TakılanKart.kartsifre and Hak==0:
                print("""Şifrenizi 3 kere hatalı girdiğiniz için kartınız bloke olmuştur lütfen en yakın şubeye uğrayınız!!!""")
                exit()

    def program(self):
        secim = self.menu()

        if secim == 1:
            self.bakiye()
        if secim == 2:
            self.kkborc()
        if secim == 3:
            self.paracek()
        if secim == 4:
            self.parayatir()
        if secim == 5:
            self.cıkıs()

    def menu(self):
        secim = int(input("\nMerhabalar. {} Banka Hoşgeldiniz Sayın {} {}.\n\n Lütfen Yapmak İstediğiniz İşlemi Seçiniz...\n\n[1] Bakiye Sorgulama\n[2] Kredi Kartı Borç Sorgulama\n[3] Para Çekme\n[4] Para Yatırma\n[5] Kart İade \nSeçim: ".format(self.atmAd,TakılanKart.ad,TakılanKart.soyadi)))

        while secim<1 or secim>5:
            print("Lütfen 1 ve 5 arasında geçerli bir sayı giriniz...\nAna menüye dönülüyor...")
            self.program()
        return secim

    def bakiye(self):
        print("Hesap Bakiyeniz: {} TL'dir".format(TakılanKart.bakiye))
        self.dongu = False
        self.menuyedon()

    def kkborc(self):
        print("Güncel Borcunuz: {} TL'dir ve Son Ödeme Tarihiniz {} ' dir".format(TakılanKart.kkborc,TakılanKart.sonodeme))
        self.dongu = False
        self.menuyedon()

    def paracek(self):
        miktar = int(input("Lütfen çekeceğiniz tutarı giriniz : "))
        YeniBakiye = TakılanKart.bakiye - miktar
        if miktar > TakılanKart.bakiye:
            print("Yetersiz bakiye")
            self.menuyedon()
        else:
            print("İşlem Başarılı \nYeni Bakiyeniz: {} TL'dir".format(YeniBakiye))
            self.menuyedon()

    def parayatir(self):
        miktar2 = int(input("Lütfen yatıracağınız tutarı giriniz : "))
        YeniBakiye2 = TakılanKart.bakiye + miktar2
        print("İşlem Başarılı \nYeni Bakiyeniz: {} TL'dir".format(YeniBakiye2))
        self.menuyedon()

    def cıkıs(self):
        print("Bizi tercih ettiğiniz için teşekkürler, İyi günler...")
        self.dongu = False
        exit()

    def menuyedon(self):
        x = int(input("Ana menüye dönmek için lütfen 7 tuşuna basınız kart iade için 5 e basınız..."))
        if x == 7:
            self.program()
        elif x == 5 :
            self.cıkıs()

Banka = ATM("BankerBilo")
while Banka.dongu:
    Banka.program()
