#bir ve birden fazla fonksiyona dışardan özellik eklemek için kullanılır...
# return aslında bir fonksiyon yapısını tekrar fonksiyona göndermek için kullanılır

# def topla(x,y):
#     sonuc = x+y
#     print(sonuc)

# topla(4,7)

# a=topla

# a(4,12)

# def fonksiyon1():
#     print("Merhabalar")

#     def fonksiyon2():
#         print("Nasılsınız")

# fonksiyon1() #fonksiyon2 çalışmadı sebebi return kullanmayıp onu tekrar fonksiyona göndermedik

# def fonksiyon1():
#     print("Merhabalar")

#     def fonksiyon2():
#         return "Nasılsınız" #tek başına yetmez bir de yazdırma komutunu eklemeyeliz
#     print(fonksiyon2())

# fonksiyon1() 

# def fonksiyon1(fonksiyon):
#     def wrapper():
#         print("Eklemek İstediğimiz Alan1")
#         fonksiyon()
#         print("Eklemek istediğiniz Alan2")
#     return wrapper

# @fonksiyon1
# def Selam():
#     print("merhaba")

# Selam()

# def deco(func):
#     def wrapper(x,y):
#         print("İşleminizin sonucu...:")
#         func(x,y)
#     return wrapper
# @deco
# def topla(x,y):
#     sonuc = x+y
#     print(sonuc)
# @deco
# def carpma(x,y):
#     sonuc = x*y
#     print(sonuc)

# topla(5,8)
# carpma(4,3)

import time

# def toplam(x,y):
#     basla=time.time()
#     time.sleep(2)
#     sonuc=x+y
#     bitir=time.time()
#     fark=bitir-basla
#     print("Sonuc {}. Fonksiyon {} sürede çalışmanız bitirildi...".format(sonuc,fark))

# toplam(2,5)

# def carpma(x,y):
#     basla=time.time()
#     time.sleep(2)
#     sonuc=x*y
#     bitir=time.time()
#     fark=bitir-basla
#     print("Sonuc {}. Fonksiyon {} sürede çalışmanız bitirildi...".format(sonuc,fark))

# carpma(2,5)

# -------------- ÜSTTE GİBİ HER FONKSİYONA TEK TEK YAZARIZ YA DA DECO İLE HIZLICA EKLERİZ----------------------------------------------------------------

def zamanolc(fonks):
    def wrapper(*args, **kwargs):
        basla= time.time()
        time.sleep(2)
        fonks(*args, **kwargs)
        bitir= time.time()
        time.sleep(2)
        fark = bitir-basla
        print("Fonksiyon {} sürede çalışmanız bitirildi...".format(fark))
    return wrapper

@zamanolc
def topla(x,y):
    sonuc = x+y
    print(sonuc)

@zamanolc
def carp(x,y):
    sonuc = x*y
    print(sonuc)

topla(50000,12222)