# Ívar Þór Þórðarson
import random
import math

######### klasar ##########

######### klasar dæmi 3 ###
class Tolur:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def gera_lista(self):
        l = []
        for i in range(3):
            if self.a <= self.b:
                l.append(self.a)
                self.a = self.a + self.c

        return l

    def gera_dict(self):
        dict = {'a':self.a,'b':self.b,'c':self.c}
        return dict

    def summa(self,listi):
        summan = sum(listi)
        return summan

    def lamban(self,listi):
        nyji = list(filter(lambda x: x % 2 == 0 and x >= 50 or x <= 90,listi))
        return nyji

###########################
#########klasar dæmi 4#####

class geimvera():

    def frumnafn(self):
        return "Geimvera"

    def hver_er_eg(self):
        return "Ég er Geimvera"

class venus(geimvera):

    def __init__(self,litur,tala):
        self.litur = litur
        self.tala = tala

    def nafn(self):
        return "Venus"

    def hver_er_eg(self):
        return geimvera.hver_er_eg(self) + " frá Venus Talan er "+ self.tala + " og liturinn er " + self.litur

class mars(geimvera):

    def __init__(self,litur,tala):
        self.litur = litur
        self.tala = tala

    def nafn(self):
        return "Mars"

    def hver_er_eg(self):
        return geimvera.hver_er_eg(self) + " frá Mars Talan er " + self.tala + " og liturinn er "+ self.litur

###########################
######### Dæmi 1 ##########

def tolur(listi):
    nyr = list(filter(lambda x: (x%5 == 0),listi))
    return nyr

listi = []
for i in range(23):
    listi.append(random.randint(40,130))

print("-----------------------------")
print(listi)
print(tolur(listi))

    ###########################

    ######### Dæmi 2 ##########


listi1 = ["konni","sigga","snorri"]
listi2 = ["fótbolta","handbolta","blaki"]
ny_listi = [x + " er í " + listi2[random.randint(0,3)] for x in listi1]
print("-----------------------------")
print(ny_listi)


    ###########################
    ######### Dæmi 3 ##########

z = [2,8,3]
m = Tolur(2,8,3)
print("-----------------------------")
print(m.gera_dict())
print(m.gera_lista())
print(m.summa(z))
print(m.lamban(listi))

###########################
######### Dæmi 4 ##########

hlutur1 = geimvera()
hlutur2 = venus("gulur","22")
hlutur3 = mars("rauður","136")
print("-----------------------------")
print(hlutur1.frumnafn())
print(hlutur1.hver_er_eg())
print(hlutur2.nafn())
print(hlutur2.hver_er_eg())
print(hlutur3.nafn())
print(hlutur3.hver_er_eg())





