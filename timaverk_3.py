import random

def random_tolur(byrja,enda,tala): # Fall sem býr til random lista
    listi = []
    for i in range(tala):
        listi.append(random.randint(byrja,enda))
    return listi

def snua(x,y):# Fall fyrir lið 1
    x = x[::-1]
    y = y[::-1]
    sv = int(x) + int(y)
    return sv

def lista_breytir(l): # Fall fyrir lið 2
    listi2 = list(filter(lambda x: x % 5 == 0 and x > 350,l))
    return listi2

def list_comp(l): # Fall fyrir lið 3
    listi2 = [x**3 for x in l]
    return listi2

# Valmynd
val = 1
while val != 0:
    print("1 = Liður eitt")
    print("2 = Liður tvö")
    print("3 = Liður þrjú")
    val = int(input("Hvaða lið viltu fara í ?(0 til að hættta) --->"))


    # Dæmi 1
    if val == 1:

        a = str(input("slaðu inn fyrir a"))
        b = str(input("Slaðu in fyrir b"))
        s = snua(a,b)
        print(s)

    # Dæmi 2
    elif val == 2:

        listi = random_tolur(50,1000,200)
        l = lista_breytir(listi)
        print(l)

    # Dæmi 3
    elif val == 3:
        listi = random_tolur(1,50,100)
        print(listi)
        l = list_comp(listi)
        print(l)

