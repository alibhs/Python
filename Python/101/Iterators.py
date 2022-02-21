# #objenin her bir elemanını döndürür

# liste = [1,2,3,4,5]

# # for i in liste:
# #     print(i)

# iterator=iter(liste)
# # print(iterator)
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator)) # liste bitti stopiterator hatası veriyor

# # for i in liste'nin manueli
# while True:
#     try:
#         tara = next(iterator)
#         print(tara)
#     except StopIteration:
#         break

class Sayılar:
    def __init__(self,basla,bitir):
        self.basla = basla
        self.bitir = bitir
    def __iter__(self):
        return self
    def __next__(self):
        if self.basla <= self.bitir:
            x = self.basla
            self.basla+=1
            return x
        else:
            raise StopIteration

print(Sayılar)

liste=Sayılar(0,100)
 
for i in liste:
    print(i)
