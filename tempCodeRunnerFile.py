sonlar = [1, 2, 3, 4, 5,6,7,8,9,23,1]

max_son = max(sonlar)
sonlar.remove(max_son)

juft_sonlar = sorted([son for son in sonlar if son % 2 == 0], reverse=True)
toq_sonlar = sorted([son for son in sonlar if son % 2 != 0])

natija = toq_sonlar + [max_son] + juft_sonlar

print("Yangi tartibdagi ro'yxat:", natija)



