import json
import requests

while True:
    sehir=input("Lütfen Hava Durumunu Görmek İstediğiniz Şehrin Adını Giriniz: ")
    apikey="42bf090d43fb897c6c0bbf453867c213"

    adres="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=tr&units=metric".format(sehir,apikey)

    baglan=requests.get(adres)
    sorgu=baglan.json()
    # print(sorgu)
    havadurumu = sorgu["weather"][0]["description"]
    havasıcaklık= sorgu["main"]["temp"]
    hissedilensıcaklık=sorgu["main"]["feels_like"]
    minsıcaklık=sorgu["main"]["temp_min"]
    maxsıcaklık=sorgu["main"]["temp_max"]
    basınc=sorgu["main"]["pressure"]
    nemoranı=sorgu["main"]["humidity"]

    print("{} için hava durumu bilgileri aşağıdaki gibidir...\nSıcaklık:{} Derecedir.\nDurum:{}\nHissedilen Sıcaklık:{} Derecedir.\nEn Düşük Sıcaklık:{} Derecedir.\nEn Yüksek Sıcaklık:{} Derecedir.\nBasınç:{} hpa\nNem:%{}".format(sehir.capitalize(),havasıcaklık,havadurumu.title(),hissedilensıcaklık,minsıcaklık,maxsıcaklık,basınc,nemoranı))


