import random
listi = []

for i in range(30):
    listi.append(random.randint(-20,20))
print(listi)


ny = list(map(lambda x:abs(x),listi))
print(ny)

listi2 = []
tel = 20
for i in range(50 +1):
    listi2.append(tel)
    tel += 1

print(listi2)

cels = list(map(lambda c: (c - 32) * (5/9),listi2))

#T(°C) = (T(°F) - 32) × 5/9
print(cels)

listi4 = ["epli","rúsína","appesína","ananas","banani","mangó","kiwi","sveskja","plóma","granet"]

avoxt = list(filter(lambda x: x if len(x) <= 5 else None,listi4))
print(avoxt)
