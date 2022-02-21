# x = int(input("Lütfen 0 dan farklı bir sayi giriniz : "))

# if x==0:
#     raise Exception("Girdiğiniz değer 0 dan farklı olmalıdır")
# else:
#     print(x)

def kontrol(x):
    if len(x)<5:
        raise Exception("Şifreniz en az 5 karakterden oluşmalıdır")
    else:
        print("şifreniz başarılı şekilde oluşturulmuştur")

x = input("lütfen bir şifre belirleyiniz:")

try:
    kontrol(x)
except Exception as hata:
    print(hata)
