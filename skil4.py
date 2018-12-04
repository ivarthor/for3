# Ívar Þór Þórðarson
# 23.10.2018

#############################
####Parent_class (Nemi)######
#############################

class Nemi():
    def __init__(self,kennitala,nafn,kyn,heimilisfang,simanumer,netfang):
        self.kennitala = kennitala
        self.nafn = nafn,
        self.kyn = kyn
        self.heimilisfang = heimilisfang
        self.simanumer = simanumer
        self.netfang = netfang

    #Set föll

    def breyta_kennit(self,ny_kennit):
        self.kennitala = ny_kennit

    def breyta_nafn(self,ny_nafn):
        self.nafn = ny_nafn

    def breyta_kyn(self,ny_kyn):
        self.kyn = ny_kyn

    def breyta_heimilisf(self,ny_heimilisf):
        self.heimilisfang = ny_heimilisf

    def breyta_simanum(self,ny_simaum):
        self.simanumer = ny_simaum

    def breyta_net(self,ny_net):
        self.netfang = ny_net

    # Get Föll

    def get_kennit(self):
        return self.kennitala

    def get_nafn(self):
        return self.nafn

    def get_kyn(self):
        return self.kyn

    def get_heimilisf(self):
        return self.heimilisfang

    def get_simanum(self):
        return self.simanumer

    def get_net(self):
        return self.netfang

    # str fall

    def __str__(self):
        return "Nemi : " + " : " + str(self.kennitala) + " : " + str(self.nafn) + " : " + str(self.kyn) + " : " + str(self.heimilisfang) + " : " + str(self.simanumer) + " : " + str(self.netfang)

#######################################
####child_class_1 (Grunnskólanemi)#####
#######################################

class Grunnskola_nemi(Nemi):
    def __init__(self,kennitala,nafn,kyn,heimilisfang,simanumer,netfang,forradamadur,nafn_skola):
        Nemi.__init__(self,kennitala,nafn,kyn,heimilisfang,simanumer,netfang)
        self.forr_m = forradamadur
        self.n_skola = nafn_skola

    # Set föll

    def breyta_forr_m(self,ny_forr):
        self.forr_m = ny_forr

    def breyta_skola(self,ny_skoli):
        self.n_skola = ny_skoli

    # get föll

    def get_forradamann(self):
        return self.forr_m

    def get_nafn_skola(self):
        return self.n_skola

    # str fall

    def __str__(self):
        return "Grunnskolanemi : " + " : " + str(self.kennitala) + " : " + str(self.nafn) + " : " + str(self.kyn) + " : " + str(self.heimilisfang) + " : " + str(self.simanumer) + " : " + str(self.netfang) + " : " + str(self.forr_m) + " : " + str(self.n_skola)

##########################################
####Child_class_2 (Framhaldskólanemi)#####
##########################################

class Framhaldskolanemi(Nemi):
    def __init__(self,kennitala,nafn,kyn,heimilisfang,simanumer,netfang,braut,styrkur = False):
        Nemi.__init__(self,kennitala,nafn,kyn,heimilisfang,simanumer,netfang)
        self.braut = braut
        self.styrkur = styrkur

    # set föll

    def breyta_braut(self,ny_braut):
        self.braut = ny_braut

    def breyta_kennit(self,ny_styrkur):
        self.styrkur = ny_styrkur

    # get föll

    def get_braut(self):
        return self.braut

    def get_styrk(self):
        return self.styrkur

    # str fall

    def __str__(self):
        return "Nemi : " + " : " + str(self.kennitala) + " : " + str(self.nafn) + " : " + str(self.kyn) + " : " + str(self.heimilisfang) + " : " + str(self.simanumer) + " : " + str(self.netfang) + " : " + str(self.braut) + " : " + str(self.styrkur)

####################################
####Child_class_3 (Háskólanemi)#####
####################################

class Haskolanemi(Nemi):
    def __init__(self,kennitala,nafn,kyn,heimilisfang,simanumer,netfang,stig):
        Nemi.__init__(self,kennitala,nafn,kyn,heimilisfang,simanumer,netfang)
        self.stig = stig

    # Set föll

    def breyta_stig(self,ny_stig):
        self.stig = ny_stig

    # get föll

    def get_stig(self):
        return self.stig

    # str fall

    def __str__(self):
        return "Nemi : " + " : " + str(self.kennitala) + " : " + str(self.nafn) + " : " + str(self.kyn) + " : " + str(self.heimilisfang) + " : " + str(self.simanumer) + " : " + str(self.netfang) + " : " + str(self.stig)


# Gera alla nemenduna
g_nemi1 = Grunnskola_nemi("0912354324","Sammi","KK","Móatjörn 3","123-4567","netfang@gmail.com","Sölvi","Akurskóli")
f_nemi1 = Framhaldskolanemi("123456789","Nína","KVK","Skólabraut 8","234-5678","netfang2@gmail.com","FORR2HF05CU",True)
h_nemi1 = Haskolanemi("5678924556","Kjartan","KK","Hringbraut 23","890-2345","netfang3@gmail.com","Med")

# Prent skipanir
print(g_nemi1)
print()
print(f_nemi1)
print()
print(h_nemi1)
print()

# Breyti nafni á Grunnskóla nema með set falli
g_nemi1.breyta_nafn("Kristófer")
# Finn út hvort að set fallið virakði með get falli
print(g_nemi1.get_nafn())
# prenta neman með nýja nafninu
print(g_nemi1)

inp = input("í hvað viltu breyta nafninu hjá grunnskólanemanum? --> ")
g_nemi1.breyta_nafn(inp)
print(g_nemi1.get_nafn())
print(g_nemi1)


