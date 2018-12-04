import random

###############################
########### Trapísa klasi #####
###############################

class trapisaTest:

    def __init__(self,a = 0,b = 0,c = 0, d = 0,h = 0):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.d = d

    def ummal(self):
        print(self.a+self.b+self.c+self.d)

    def flatarmal_1(self):
        print((self.a+self.b+self.c+self.d)/2)

    def flatarmal_2(self):
        print(((self.a+self.c)/2)*self.h)

    def jafnarma(self):
        skil = False
        if self.a == self.b or self.c == self.d:
            skil = True
        else:
            skil = False
        return skil

    def lestu_mig(self):
        print("Trapisa eða hálfsamsíðungur er ferhyrningur þar sem tvær mótlægar hliðar eru samsíða.")



###############################
########### Bílar klasi #######
###############################

class bilar:
    def __init__(self,teg,ar,hradi,bensin,eydsla):
        self.teg = teg
        self.ar = ar
        self.hradi = hradi
        self.bensin = bensin
        self.eydsla = eydsla

    def kappakstur(self,b2,b3):

        if (self.eydsla) * 10 > self.bensin:
            bil1 = False
        else:
            b1 = True

        if (b2.eydsla) * 10 > b2.bensin:
            bil2 = False
        else:
            bil2 = True

        if (self.eydsla) * 10 > self.bensin:
            bil3 = False
        else:
            bil3 = True

        if bil1 != False:
            if self.hradi > b2.hradi and self.hradi > b3.hradi:
                print("bíll eitt vinnur")
        else:
            print("bíll eitt er búinn með bensínið")

        if bil2 != False:
            if b2.hradi > self.hradi and b2.hradi > b3.hradi:
                print("Bíll tvö vinnur")
        else:
            print("Bíll tvö er búinn með bensínið")

        if bil3 != False:
            if b3.hradi > b2.hradi and b3.hradi > self.hradi:
                print("Bíll þrjú vinnur")
        else:
            print("Bíll þrjú er búinn með bensínið")


val = 1
while val != 0:
    val = int(input("val -->"))
    ###############################
    ########### Trapísa ###########
    ###############################
    if val == 1:

        a = int(input("Sláðu inn hlið a"))
        b = int(input("Sláðu inn hlið b"))
        c = int(input("Sláðu inn hlið c"))
        d = int(input("Sláðu inn hlið d"))
        h = int(input("Sláðu inn hæðina á trapísunni"))
        trapisa1 = trapisaTest(a,b,c,d,h)

        if trapisa1.jafnarma() == True:
            trapisa1.ummal()
            trapisa1.flatarmal_1()
            print(trapisa1.jafnarma())
            trapisa1.lestu_mig()
        else:
            trapisa1.ummal()
            trapisa1.flatarmal_2()
            print(trapisa1.jafnarma())
            trapisa1.lestu_mig()

    ###############################
    ########### Bílar ############
    ###############################
    elif val == 2:

        bill1 = bilar("Ford","2005",random.randint(1,200),random.randint(1,100),random.randint(1,10))
        bill2 = bilar("Lexus","2015",random.randint(1,200),random.randint(1,100),random.randint(1,10))
        bill3 = bilar("Honda","2010",random.randint(1,200),random.randint(1,100),random.randint(1,10))
        f = bill1.kappakstur(bill2,bill3)

