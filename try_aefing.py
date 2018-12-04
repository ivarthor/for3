import sys
val = 1
while val != 0:
    val = 0
    print("--------------------------")
    print("1 = ")
    print("2 = ")
    print("3 = ")
    print("0 = Hætta í forriti")
    print("--------------------------")

    val = int(input("Hvaða lið viltu keyra? --> "))

    if val == 1:
        listi = []
        t = 0
        for x in range(10 + 1):
            try:
                a = input("Sláðu inn tölu --> ")
                listi.append(int(a))
                t += 1

            except:
                    print("þetta er ekki heiltala", sys.exc_info())

        print(listi)

    elif val == 2:
        c = "T"
        t = 0
        try:
            ############
            a = 6/0
            ############
            #f = open("asd.txt")
            ############
            #k = int(c)
            ############
            #"g" + 5
            ############
            #9 * spam*3
            ############
            #listi = ["a",2,4,"g","1"]
            #for i in range(10):
             #   print(listi[t])
              #  t += 1
            ############

        except ValueError:
            print("vitlaust gagnatag")
            pass

        except (ZeroDivisionError):
            print("Ekki deila með núll")
            pass

        except (TypeError):
            print("get ekki lagt sama str og int")
            pass

        except (NameError):
            print("óskilgreind breyta")
            pass

        except (IndexError):
            print("index out of range")
            pass

        except:
            print("óvænt villa")
            pass


    elif val == 3:
        try:
            a = int(input("tala hér ---> "))
            if a < -10:
                raise ValueError("má ekki vera minni en -10")
            if a > 200:
                raise ValueError("Má ekki vera stærri en 200")
            if a == 12:
                raise ValueError("Má ekki vera 12")
        except ValueError as x:
            print(x)

    elif val == 4:
        try:
            f = open("try.txt","r", encoding="utf-8")
            for i in f:
                print(i + 3)

        except:
            print("eitthvað fór úrskeiðis",sys.exc_info())

        finally:
            f.close()
            print("skránni hefur verið lokað")
