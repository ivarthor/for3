class Animal():
    def __init__(self,aldur,kyn):
        self.aldur = aldur
        self.kyn = kyn

    def __str__(self):
       return "Animal : " + str(self.aldur) + " : " + str(self.kyn)

class person(Animal):
    def __init__(self,aldur,kyn):
        Animal.__init__(self,aldur,kyn)

class Student(person):
    def __init__(self,aldur,kyn,nafn,skoli):
        person.__init__(self,aldur,kyn)
        self.nafn = nafn
        self.skoli = skoli

    def __str__(self):
       return "Stúdent : " + str(self.aldur) + " : " + str(self.kyn) + " : " + str(self.nafn) + " : " + str(self.skoli)
student1 = Student(14,"m","Sammi","Skolinn")
print(student1)
