# ilk_sayı    = input("ilk sayı: ")
# ikinci_sayı = input("ikinci sayı: ")

# try:
#     sayı1 = int(ilk_sayı)
#     sayı2 = int(ikinci_sayı)
#     print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
# except (ValueError, ZeroDivisionError) as hata:
#     print("Bir hata oluştu!")
#     print("orijinal hata mesajı: ", hata)

# while True:
#     ilk_sayı = input("ilk sayı (Programdan çıkmak için q tuşuna basın): ")

#     if ilk_sayı == "q":
#         break

#     ikinci_sayı = input("ikinci sayı: ")

#     try:
#         sayı1 = int(ilk_sayı)
#         sayı2 = int(ikinci_sayı)
#         print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
#     except (ValueError, ZeroDivisionError):
#         print("Bir hata oluştu!")
#         print("Lütfen tekrar deneyin!")