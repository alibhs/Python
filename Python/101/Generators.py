# # #iteratorle aynı işe yarar ama sürekli çalışmaz

# # def ciftSayi(sayi):
# #     liste=[]

# #     for i in range(1,sayi):
# #         liste.append(i*2)
# #     return liste

# # print(ciftSayi(100))

# def cift(sayi):
#     for i in range(1,sayi):
#         yield i*2

# for i in cift(100):
#     print(i) 