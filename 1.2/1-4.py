# Opdracht 1
def opdracht1():
    def p():
        print("H   H  I")
        print("H   H")
        print("H   H  I")
        print("HHHHH  I")
        print("H   H  I")
        print("H   H  I")
        print("H   H  I")

    p()
    #   print(1 + 1)
    p()


# Opdracht 2
def opdracht2(nummer1, nummer2, nummer3):
    if nummer1 > nummer2 and nummer1 > nummer3:
        print(nummer1)
    if nummer2 > nummer1 and nummer2 > nummer3:
        print(nummer2)
    if nummer3 > nummer2 and nummer3 > nummer1:
        print(nummer3)

# opdracht2(1, 5, 3)


# Opdracht 3
def opdracht3(nummer1, nummer2, nummer3):
    if nummer1 > nummer2 and nummer1 > nummer3:
        return nummer1
    if nummer2 > nummer1 and nummer2 > nummer3:
        return nummer2
    if nummer3 > nummer2 and nummer3 > nummer1:
        return nummer3

# print(opdracht3(1, 2, 3))
# print(opdracht3(10, 11, 14))


# Opdracht 4


def opdracht4(x, y, z):
    def macht3(macht):
        return macht * macht * macht

    def faculteit(fac):
        getal = fac
        while (getal > 2):
            getal = getal - 1
            fac = fac * getal
        return fac

    return (macht3(x) * macht3(y) * macht3(z) + faculteit(x)) / faculteit(y)

# print(opdracht4(3, 3, 3))


# Opdrach 4b
def opdracht4b(naam, age):
    length = 20
    inaam = length - len(naam)
    iage = length - len(str(age))

    print('**********************')
    print('*                    *')

    print('* Welkom ' + naam + '! ', end="")
    while inaam > 10:
        print(' ', end="")
        inaam -= 1
    print('*')

    print('* Je leeftijd is: ' + str(age), end="")
    while iage > 17:
        print(' ', end="")
        iage -= 1
    print('*')

    print('*                    *')
    print('**********************')
# opdracht4b('Admin', 50)