# Ívar Þór Þórðarson 3.9.2018

# Föll úr Lið 1

def numer_nafni(dicto,nafn):
    svar = dicto.get(nafn)
    if svar == None:
        svar = "Þetta nafn er ekki til"
    return svar

def baeta(dic,nafn,numer):
    dic[nafn] = numer

def eyda(dic,nafn):
    dic.pop(nafn)

def breyta_nr(dic,nafn,nr):
    dic[nafn] = nr

# Föll úr Lið 2

def sort(l):
    l.sort()
    for i in l:
        print(i)

def sam(l1,l2):
    listi = []
    for x in  l1:
        for i in l2:
            if x == i:
                listi.append(x)
    return listi

# Föll úr lið 3

def listi_n_p(n,p):
    rett = "VELKOMIN"
    vitlaust_p_n = "RANGT"
    vitlaust = "EKKI TIL"
    nafn = []
    pas = []
    f = open("lykilord.txt","r",encoding="utf-8")
    g = f.readlines()


    for i in g:
        na = i.split(";")[0]
        pa = i.split(";")[1]
        nafn.append(na)
        pas.append(pa)


    for x in range(len(nafn)):
        if n == nafn[x]:
            if p == pas[x].strip():
                return rett
            else:
                return vitlaust_p_n
        else:
            return vitlaust

# valmynd
val = 1
while val != 0:
    val = 0
    print()
    print("1 = ")
    print("2 = ")
    print("3 = ")
    print("4 = ")
    print("5 = ")
    print("Veldu 0 til að hætta")

    val = int(input("Hvaða lið viltu keyra? --> "))


    if val == 1:
        val2 = 1
        while val2 != 0:
            val2 = 0
            print()
            print("1. Finna númer frá nafni")
            print("2. Bæta nafni og númeri")
            print("3. Eyða staki")
            print("4. Breyta númeri")
            print("Veldu 0 til að hætta")

            val2 = int(input("Hvað viltu gera í lið 1?"))

            dic = {"Kalli":"615-2345","Palli":"422-3456","Halli":"123-4567","Ívar":"312-7777","Bjarki":"894-3456","Andri":"198-645","Kristófer":"480-5535","Kristján":"445-7735","Alexander":"555-6666","Samúel":"341-7742"}

            if val2 == 1:
                print(dic)
                naf = str(input("skrifaðu nafnið á aðila hér --->"))
                print(numer_nafni(dic,naf))

            elif val2 == 2:
                print(dic)
                nafn = str(input("Sláðu inn nafninu sem þú vilt bæta inn ---> "))
                nr = str(input("Sláðu inn númer sem þú vilt bæta inn ---> "))
                baeta(dic,nafn,nr)
                print(dic)

            elif val2 == 3:
                print(dic)
                nafn = str(input("Sláðu inn nafninu á stakinu sem þú vilt eyða ---> "))
                eyda(dic,nafn)
                print("Staki hefur verið eytt")
                print(dic)

            elif val2 == 4:
                print(dic)
                nafn = str(input("Sláðu inn nafnið hjá aðilanum sem þú vilt breyta ---> "))
                nr = str(input("Sláðu inn nýtt númer ---> "))
                breyta_nr(dic,nafn,nr)
                print(dic)


    elif val == 2:
        forr = []
        gog = []
        #Búa til lista fyrir FOR
        f_nr = int(input("Hvað eru margir nemndur í hópnum FOR1TÖ05CU ---> "))

        for i in range(f_nr):
            f_nafn = str(input("Sláðu inn nafn á nemanda --> "))
            print()
            forr.append(f_nafn)


        # búa til lista fyrir GSÖ
        g_nr = int(input("Sláðu núna inn hvað það eru margir í hópnum GSÖ1TÖ05AU ---> "))

        for a in range(g_nr):
            g_nafn = str(input("Sláðu inn nafn á nemanda --> "))
            print()
            gog.append(g_nafn)
        print("nemendur úr FOR1TÖ05CU í stafrófsröð")
        sort(forr)
        print("nemendur úr GSÖ1TÖ05AU í stafrófsröð")
        sort(gog)

        # Kalla í fallið sem finnur öll sambærileg stök
        print("Nemendur sem eru í báðum hópum")
        samb = sam(forr,gog)
        for o in samb:
            print(o)

        if f_nr > g_nr:
            print("það eru fleirri í FOR1TÖ05CU")

        elif g_nr > f_nr:
            print("það eru fleirri í GSÖ1TÖ05AU")

        else:
            print("Það eru jafnmargir í hópunum")

        for k in range(2):
            gog.append(forr[-1])
            del(forr[-1])
        print("síðustu tveir teknir úr listanum",forr)
        print("síðustu tveir úr FOR1TÖ05CU bættir í listann",gog)


    elif val == 3:

        n_nafn = str(input("Sláðu inn notenda-nafn --> "))
        pas = str(input("Sláðu inn password --> "))

        print(listi_n_p(n_nafn,pas))

    elif val == 4:

        nyr = ""
        #input
        strengur = ""
        for x in range(0,len(strengur),2):
            if x+1 < len(strengur):
                nyr = nyr + strengur[x+1] + strengur[x]
            else:
                nyr = nyr + strengur[x]
