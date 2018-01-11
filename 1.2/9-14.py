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
