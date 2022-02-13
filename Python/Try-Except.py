while True:
    try:
        x = int(input("Lütfen ilk sayi giriniz: "))
        y = int(input("Lütfen ikinci sayi giriniz: "))
        print(x/y)
# except (ZeroDivisionError):
#     print("Sıfıya bölmeye çalışıyorsunuz")
# except ValueError:
#     print("Sayı dışında bir değer girdiniz")
    # except (ZeroDivisionError,ValueError):
    #     print("Hatalı bir değer girdiniz")
    except Exception as hata:
        print("Yolunda gitmeyen bir şey var",hata)
    else:
       # print("Sorun yok")
        break

print(x/y)
