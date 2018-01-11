import math

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

# Opdracht 5 a
def opdracht5a(val):
    index = 0
    while index < len(val):
        print(str(index + 1) + ':' + val[index])
        index += 1
# opdracht5a('awdawfiawhif')


# Opdracht 5 b
def addDot(val):
    last = val[len(val) - 1]
    if last == '.':
        return val
    else:
        return val + '.'
# addDot('adw')

def opdracht5b(text):
    text = text.split('.')
    result = ''
    for sentence in text:
        if sentence == '':
            break
        sentence = sentence.lstrip(' ')
        result += sentence[0].capitalize() + sentence[1:] + '. '
    return result
# print(opdracht5b('python is een general-purpose programmeertaal. sql is een declarative programming language.'))


def opdracht5c(text):
    return ' '.join(text.split())
# opdracht5c('a  b')


def opdracht5d(text):
    text = text.replace('0', 'nul')
    text = text.replace('1', 'een')
    text = text.replace('2', 'twee')
    text = text.replace('3', 'drie')
    text = text.replace('4', 'vier')
    text = text.replace('5', 'vijf')
    text = text.replace('6', 'zes')
    text = text.replace('7', 'zeven')
    text = text.replace('8', 'acht')
    text = text.replace('9', 'negen')
    return text
# opdracht5d('We zitten nu in 2017, volgend jaar is het 2018.')


def opdracht5e(text):
    text = opdracht5b(opdracht5d(addDot(opdracht5c(text))))
    print(text)
# opdracht5e('we       zitten     nu in 2017.      volgend jaar is het      2018')

# Opdracht 6

# pc 1 =
def m1():
    global s
    s = 'no spam...'
    print(s)
    t = 'Java...'
    print(t)
    x = 1
    z = 2
    m2(x, z)
    x = 3

def m2(x, y):
    x = x + 1
    z = y + 2
    m3(x, z)

def m3(x, b):
    x = 4
    x = m4(x)

def m4(z):
    return z + z

s = 'I hate spam'
t = 'Programming is great'
# m1()
# print(s)
# print(t)

"""
pc=166
pc=167,s='I hate spam'
pc=168,s='I hate spam',t='Programming is great'
pc=168,s='I hate spam',t='Programming is great'|pc=144, s='I hate spam'
pc=168,s='I hate spam',t='Programming is great'|pc=145, s='no spam...'
pc=168,s='I hate spam',t='Programming is great'|pc=146, s='no spam...'
pc=168,s='I hate spam',t='Programming is great'|pc=147, s='no spam...'
pc=168,s='I hate spam',t='Programming is great'|pc=148, s='no spam...',t='Java...'
pc=168,s='I hate spam',t='Programming is great'|pc=150, s='no spam...',t='Java...',x=1
pc=168,s='I hate spam',t='Programming is great'|pc=151, s='no spam...',t='Java...',x=1,y=2
pc=168,s='I hate spam',t='Programming is great'|pc=151, s='no spam...',t='Java...',x=1,y=2|pc=155,x=1,y=2
pc=168,s='I hate spam',t='Programming is great'|pc=151, s='no spam...',t='Java...',x=1,y=2|pc=156,x=2,y=2
pc=168,s='I hate spam',t='Programming is great'|pc=151, s='no spam...',t='Java...',x=1,y=2|pc=157,x=2,y=4
pc=168,s='I hate spam',t='Programming is great'|pc=151, s='no spam...',t='Java...',x=1,y=2|pc=158,x=2,y=4|pc=160,x=2,b=4
pc=168,s='I hate spam',t='Programming is great'|pc=151, s='no spam...',t='Java...',x=1,y=2|pc=158,x=2,y=4|pc=161,x=4,b=4
pc=168,s='I hate spam',t='Programming is great'|pc=151, s='no spam...',t='Java...',x=1,y=2|pc=158,x=2,y=4|pc=161,x=4,b=4|pc=164,z=4,return=8
pc=168,s='I hate spam',t='Programming is great'|pc=151, s='no spam...',t='Java...',x=1,y=2|pc=158,x=2,y=4|pc=161,x=8,b=4
pc=168,s='I hate spam',t='Programming is great'|pc=151, s='no spam...',t='Java...',x=1,y=2|pc=157,x=8,y=4
pc=168,s='I hate spam',t='Programming is great'|pc=152, s='no spam...',t='Java...',x=1,y=2
pc=168,s='I hate spam',t='Programming is great'|pc=152, s='no spam...',t='Java...',x=3,y=2
pc=169,s='I hate spam',t='Programming is great'
pc=170,s='I hate spam',t='Programming is great'
"""

# Opdracht 7
def opdracht7():
    # A
    def opdracht7a(n):
        if n > 1:
            opdracht7a(n-1)
        print('-', end="")
    # opdracht7a(5)

    # B
    def opdracht7b(n):
        txt = "-"
        if n == 1:
            return txt
        return txt + opdracht7b(n - 1)
    # result = opdracht7b(5)

    # C
    def opdracht7c(n):
        if n <= 1:
            return 1
        return n * opdracht7c(n-1)
    # result = opdracht7c(5)

    # D
    def opdracht7d(n):
        sum = 0
        if n <= 0:
            return sum
        sum += opdracht7d(n)
        return sum + opdracht7d(n-1)
    # result = opdracht7d(5)

    # E
    def opdracht7e(n):
        if n == 0:
            return ""
        else:
            opdracht7e(n-1)
            print(n * "*")
    # opdracht7e(4)

    # F
    def opdracht7f(n):
        if n > 0:
            if n % 2 == 0:
                print(n)
            opdracht7f(n-1)
    # opdracht7f(100)

    if 'result' in locals():
        print(result)
# opdracht7()

# Opdracht 8
"""
pc=220
pc=220|pc=217,n=5
pc=220|pc=219,n=5
pc=220|pc=219,n=5|pc=217,n=4
pc=220|pc=219,n=5|pc=219,n=4
pc=220|pc=219,n=5|pc=219,n=4|pc=217,n=3
pc=220|pc=219,n=5|pc=219,n=4|pc=219,n=3
pc=220|pc=219,n=5|pc=219,n=4|pc=219,n=3|pc=217,n=2
pc=220|pc=219,n=5|pc=219,n=4|pc=219,n=3|pc=219,n=2
pc=220|pc=219,n=5|pc=219,n=4|pc=219,n=3|pc=219,n=2|pc=217,n=1
pc=220|pc=219,n=5|pc=219,n=4|pc=219,n=3|pc=219,n=2|pc=218,n=1,return=1
pc=220|pc=219,n=5|pc=219,n=4|pc=219,n=3|pc=219,n=2,return=2
pc=220|pc=219,n=5|pc=219,n=4|pc=219,n=3,return=3
pc=220|pc=219,n=5|pc=219,n=4,return=4
pc=220|pc=219,n=5,return=5
pc=220,return 220
"""

# Opdracht 9
def opdracht9():
    l = []

    def ask(l):
        inp = input('Enter ')
        if inp == 'stop':
            for i in reversed(l):
                print(i)
        else:
            l.append(inp)
            ask(l)
        return l
    l = ask(l)
# opdracht9()

# Opdracht 10
def opdracht10():
    l = [1, 2, 3, 4, 5, 10]
    def returnGreatest(l):
        greatest = 0
        for i in l:
            if i > greatest:
                greatest = i
        print(greatest)
    returnGreatest(l)
# opdracht10()

def opdracht11():
    l = [1, 2, 3, 4, 5, 10]

    def som(x, y):
        return x + y

    def calc(l):
        if len(l) > 2:
            l[-2] = som(l[-1], l[-2])
            calc(l[:-1])
        else:
            print(som(l[-1], l[-2]))

    calc(l)
# opdracht11()

# Opdracht 12
def opdracht12():
    l = [1, 2, 3, 4, 5, 10]
    def calc(l):
        if len(l) > 1:
            # Check if second last is greatest
            if l[-1] > l[-2]:
                # Replace second last with last
                l[-2] = l[-1]
                # Recursive without last list item
                calc(l[:-1])
        else:
            print(l[0])
    calc(l)
# opdracht12()

# Opdracht 13
def opdracht13():
    l = ["n", "e", "g", "e", "n"]
    # l = ["n", "e", "g", "e", "e"]
    def palindroom(l):
        # If can slice
        if len(l) > 2:
            # Check if first and last item from list match
            if l[0] == l[-1]:
                # Recursive parm = list without first and last item
                palindroom(l[1:-1])
            else:
                return False
        elif len(l) == 1:
            return True
        elif len(l) == 2:
            return False
    x = palindroom(l)
    print(x)
# opdracht13()


# Opdracht 14
def opdracht14():
    def filter(l, x):
        for i in l:
            x(i)
    filter([0, 1, 2], lambda a: a + 1)
    filter([], True if 0 else 1)
    filter([], lambda a: a > 0 if True else False)


# Opdracht 15
def opdracht15():
    number_array = [1, 2, 3, 4, 5, 6, 7]
    random_string = "we       zitten     nu in 2017.      volgend jaar is het      2018"

    def operation(a, b, operation):
        return operation(a, b)

    def map(array, map):
        new_list = []
        for value in array:
            new_list.append(map(value))
        return new_list

    def filter(array, filter):
        new_list = []
        for value in array:
            check = filter(value)
            if check:
                new_list.append(value)
        return new_list

    def then(first, last):
        return lambda value: last(first(value))

    def a():
        q = operation(1, 2, lambda a, b,: a + b)
        print(q)
        w = operation(3, 4, lambda a, b: a * b)
        print(w)
        e = operation("hello", "world", lambda a, b: a + " " + b)
        print(e)
        r = operation(3, 4, lambda a, b: math.pow(a, b))
        print(r)
    # a()

    def b():
        t = filter(number_array, lambda a: a > 3)
        print(t)
        y = map(t, lambda a: a * 3)
        print(y)
        u = filter(y, lambda a: a > 10)
        print(u)
        i = map(u, lambda a: a + 2)
        print(i)
    # b()

    def c():
        def replace_spacing(str):
            return opdracht5c(str)
        def replace_numbers(str):
            return opdracht5d(str)
        def dot(str):
            return addDot(str)
        def capitalize(str):
            return opdracht5b(str)
        x = then(then(then(replace_spacing, replace_numbers), dot), capitalize)(random_string)
        print(x)
    c()

opdracht15()
