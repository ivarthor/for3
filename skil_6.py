from skraning import Skraning
from mysql.connector import Error

try:
    med = str(input("Hvað heitir nýji meðlimurinn sem þú vilt bæta við? >>>> "))
    af = str(input("Hvað heitir áfanginn sem nýji meðlimurinn á að ver í? >>>> "))
    vinna=Skraning()
    vinna.nyr_medlimur(med)
    vinna.nyr_afangi(af)
    vinna.prenta("notendur")
    vinna.prenta("namskeid")
    vinna.skraning(med,af)
    vinna.prenta("skradir")
    vinna.skradurIafanga(med)


except Error as e:
    print("villa",e)
