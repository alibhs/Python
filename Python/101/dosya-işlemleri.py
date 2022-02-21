# w =  olmayan bir dosya yaratmak için kullanılır | Aynı isimli dosya oluşturursan onu tamamen siler yerine bunu atar
# a =  içinde olan bilgileri silmeden ekleme yapar
# x =  aynı isimli dosya varsa oluşturmaz hata verir
# r =  herhangi bir dosyayı okumak için kullanılır
# --------------------------------------------------------------------------------------

#------------- WRİTE AND READ -----------------------------------
# Dosya = open("Merhaba.txt","w")
# Dosya = open("Merhaba.txt","a")
# Dosya = open("Merhaba2.txt","x")

# Dosya.write("\nMerhaba benim adım Kemal")
# Dosya.close()

# Dosya = open("Merhaba.txt","r")
#print(Dosya.read())
# for i in Dosya:
#     print(i,end=" ")
# print(Dosya.readline()) # ilk satırı yazar | her satırı tek tek yazar
# print(Dosya.readline()) # ikinci satırı yazar
# liste = Dosya.readlines() # Elemanları liste şeklinde döndürür
# print(liste[2])
# print(Dosya.read(5)) # parantez içindeki indexe kadar yazdırır 

# Dosya.close()

#--------------------- WİTH - SEEK - TELL -----------------------------
# with open("Merhaba.txt","r") as Dosya:  # alt satırda yapılan işlemlerden sonra with otomatik dosyayı kapar
#     Dosya.seek(8) # içindeki karakterden itibaren okumaya başlar
#     Dosya.read(5)
#     print(Dosya.tell()) # kaçıncı karakterde olduğumuz gösterir

#----------------------------DOSYA İŞLEMLERİ VE METODLAR ------------------------------------------

# with open("Merhaba.txt","r+") as Dosya: # r nin yanına bir de + koyarsak hem okuma hem yazma yaptırabiliriz
#     # print(Dosya.read())
#     Dosya.seek(40)
#     Dosya.write("\nNasılsın?")

with open("Merhaba.txt","a+") as Dosya: # r nin yanına bir de + koyarsak hem okuma hem yazma yaptırabiliriz
    # Dosya.write("\nNasılsın?")
    Dosya.seek(0)
    print(Dosya.read())


 
