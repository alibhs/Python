import json
# Bilgiler={"Ad":"Ali","Soyad":"Bahşi","Yaş":21}
# print(Bilgiler["Ad"])

Bilgiler="""{"Ad":"Ali","Soyad":"Bahşi","Yaş":21}"""
bilgiOku = json.loads(Bilgiler)
print(bilgiOku["Ad"])
