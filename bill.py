class bill:
    def __init__(self,teg,nr):
        self.teg = teg
        self.nr = nr

    def uppl(self):
        print(self.teg,self.nr)

class klasi():
    def fall(self):
        print("Hæ")

bill1 = bill("Ford","zk-t24")
bill2 = bill("Toyota", "AG-324")
bill1.uppl()
bill2.uppl()

h = klasi()
h.fall()



