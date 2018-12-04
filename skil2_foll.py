# Ívar Þór Þórðarson 20.9.2018
import math
import time

# Finnur langhliðina af hringi með hliðum a og b
def langhlid(a,b):
    svar = pow(a,2) + pow(b,2)
    hlidc = math.sqrt(svar)
    return round(hlidc,2)

# Finnur út hvort að tala 2 er margföldun af tölu 1
def margfoldun_af(t1,t2):
    if t2 % t1 == 0:
        return True
    else:
        return False

# Býr til ferning úr stjörunum
def ferningur_ur_stjornum(t):
    for i in range(t):
        for x in range(t - 1):
            print("*", end=" ")
        print("*")

# kíkjir hvort að tala sé slétt eða oddatala
def er_slett_tala(t):
    if t % 2 == 0:
        return True
    else:
        return False

# finnur flatarmál hrings út frá radíusi
def flatarmal_hrings(r):
    f = 3.14 * pow(r,2)
    return f

# skrifar út 'bank' á 0.2 sek fresti í einhverjar sekúndur
def bank_bank(sek):
    end = time.time() + sek
    while time.time() < end:
        print("bank")
        time.sleep(0.20)

