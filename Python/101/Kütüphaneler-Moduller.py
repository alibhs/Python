# import  kütüüphane indirme
# from kütüphaneadı import modülismi  as benim modulum (as ile kendine göre isim atarsın)= herhangi bir modül indirme

# ------------------ MATH KÜTÜPHANESİ ------------------
#import math  = math kütüphanesi tanıtma
#from math import* # = kütüphaneyi kullanınca math yazmak zorunda bıraktırmaz

#------------- İMPORT MATH İLE İLGİLİ ÖRNEKLER---------
# x = math.sqrt(25)
# print(x)
# y= math.factorial(10)
# print(y)

#------------FROM MATH İMPORT* İLE YAPILAN ÖRNEKLER-----

# x = sqrt(25)
# print(x)

#-----------------DATETİME KÜTÜPHANESİ--------------

# from datetime import*
# import time

# x = datetime.today()
# print(x.strftime("%d-%B-%Y"))

# while True:
#     zaman = time.strftime("%H:%M:%S")
#     print(zaman)
#     time.sleep(3)
#     exit()

# ----------RANDOM KÜTÜPHANESİ------------

# import random

# x = random.random() # 0-1 arası randım
# print(x)

# y = random.uniform(1,100) # aralık arası random
# print(y)

# z=random.randint(0,100) # tam sayı random
# print(z)

# a = ["Ali","Memo","Berk"]
# s = random.choice(a)
# print(s)

# liste = range(0,100)
# x = random.sample(liste,20)
# print(x)