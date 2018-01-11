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
