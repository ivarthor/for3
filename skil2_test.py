# Ívar Þór Þórðarson 20.9.2018
from skil2_foll import *
import sys
import time

# valmynd
val = 1
timi = time.localtime()
if val == 1:
    while val > 0:
        try:
            val = 0
            nafn = str(input("Hvað heitir þú? --> "))
            print()
            print("1 = Langhlið")
            print("2 = Tala er margföldun af")
            print("3 = Ferningur úr stjörnum")
            print("4 = slétt tala")
            print("5 = flatarmál hrings")
            print("6 = bank, bank")
            print("Veldu mínus tölu til að hætta")

            val = (int(input("Hvaða lið viltu keyra? --> "))) + 1


        except:
            print("þessi villa kom upp --> ", sys.exc_info())
            print()
            val = 1

        # skrifar út nafnið á notanda og segir líka hvað klukkan er
        if val < 0:
            print("Þakkað þér fyrir að nota mig", nafn)
            print("klukkan er", timi[3] ,":", timi[4])


        # Val 1 : Langhlið
        elif val == 2:

            # Valmynd inní valmynd
            ha = 1
            while ha > 0:
                # tekur inn báðar tölurnar fyrir fallið langhlid() og heldur áfram þangað til að notandi segir því að hætta
                try:
                    ha = float(input("Sláðu inn hlið a (mínus tala til að hætta) --> "))
                    if ha > 0:
                        hb = float(input("Sláðu inn hlið b --> "))
                        print("hlið c er --> ", langhlid(ha,hb))

                # ef það er skrifað streng í staðinn fyrir heiltölu
                except ValueError:
                    print("þessi villa kom upp --> ", sys.exc_info())
                    print("Sláðu inn tölu næst")
                    print()
                    val = 1

        # Val 2 : Tala er margföldun af
        elif val == 3:

            # Valmynd inní valmynd
            t1 = 1
            while t1 != 0:
                # tekur inn báðar tölurnar fyrir fallið er_margfoldun_af() og heldur áfram þangað til að notandi segir því að hætta
                try:
                    t1 = int(input("Sláðu inn fyrstu töluna (núll til að hætta) --> "))
                    if t1 == 0:
                        break
                    else:
                        t2 = int(input("Sláðu inn aðra töluna --> "))
                        sv = margfoldun_af(t1,t2)
                        if sv:
                            print(t1,"margfaldast með", t2)
                        else:
                            print(t1,"er ekki margföldun á", t2)

                # ef það er skrifað streng í staðinn fyrir heiltölu
                except ValueError:
                    print("þessi villa kom upp --> ", sys.exc_info())
                    print("Sláðu inn tölu næst")
                    print()

        # Val 3 : ferningur úr stjörnum
        elif val == 4:

            # tekur inn töluna fyrir fallið ferningur_ur_stjornum()
            try:
                ft = int(input("Sláðu inn hversu stóran ferning þú vilt --> "))
                print()
                ferningur_ur_stjornum(ft)
                print()

            # ef það er skrifað streng í staðinn fyrir heiltölu
            except ValueError:
                print("þessi villa kom upp --> ", sys.exc_info())
                print("Sláðu inn tölu næst")
                print()

        # Val 4 : slétt tala
        elif val == 5:

            # Valmynd inní valmynd
            t = 1
            while t != 0:
                # tekur inn tölurna fyrir fallið er_slett_tala og heldur áfram þangað til að notandi segir því að hætta
                try:
                    t = int(input("Sláðu inn tölu (núll til að hætta) --> "))
                    if t != 0:
                        sv = er_slett_tala(t)
                        if sv:
                            print(t, "er slétt tala")
                        else:
                            print(t,"er oddatala")

                # ef það er skrifað streng í staðinn fyrir heiltölu
                except ValueError:
                    print("þessi villa kom upp --> ", sys.exc_info())
                    print("Sláðu inn tölu næst")
                    print()

        # Val 5 : Flatarmál hrings
        elif val == 6:

            # Valmynd inní valmynd
            r = 1
            while r > 0:
                # tekur inn radíus fyrir fallið flatarmal_hrings() og heldur áfram þangað til að notandi segir því að hætta
                try:
                    r = float(input("Sláðu inn radíus (mínus tala til að hætta) --> "))
                    if r > 0:
                        print("flatarmálið hringsins með radíusinn",r,"er",flatarmal_hrings(r))

                # ef það er skrifað streng í staðinn fyrir heiltölu
                except ValueError:
                    print("þessi villa kom upp --> ", sys.exc_info())
                    print("Sláðu inn tölu næst")
                    print()

        # Val 6 : bank, bank
        elif val == 7:
            # tekur inn sekúndur fyrir fallið bank_bank()
            try:
                sek = int(input("Sláðu inn sekúndurnar sem þú vilt sjá strengin 'bank' í --> "))
                bank_bank(sek)
                print("Hver er þar?")

            # ef það er skrifað streng í staðinn fyrir heiltölu
            except ValueError:
                print("þessi villa kom upp --> ", sys.exc_info())
                print("Sláðu inn tölu næst")
                print()
