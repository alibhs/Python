import re

dogumTarihi = "2000"
zorunluKarakterler=["\?","\*","\!","\%"] # başlarına \ koyma sebebimiz karakter olarak görsün fonksiyon olarak değil

def SifreKontrol(sifre):
    if len(sifre)<8:
        raise Exception("Şifreniz en az 8 karakterden oluşmalıdır.")
    elif not re.search("[a-z]",sifre):
        raise Exception("Şifreniz en az bir tane küçük harf içermelidir.")
    elif not re.search("[A-Z]",sifre):
        raise Exception ("Şifreniz en az bir tane büyük harf içermelidir.")
    elif not re.search("[0-9]",sifre):
        raise Exception("Şifreniz en az bir tane rakam içermelidir.")
    elif not re.search(str(zorunluKarakterler),sifre):
        raise Exception("Şifreniz en az bir karakter ('?,'*','!','%') içermelidir.")
    elif sifre.startswith(dogumTarihi)==True or sifre.endswith(dogumTarihi) == True:
        raise Exception("Şifreniz Doğum Tarihiniz ile Başlayamaz veya Bitemez.")
    else:
        print("Şifreniz başarılı şekilde oluşturulmuştur...")

while True:
    try:
        sifre=input("Lütfen Şifrenizi Oluşturunuz:")
        SifreKontrol(sifre)
    except Exception as hata:
        print(hata)
    else:
        break