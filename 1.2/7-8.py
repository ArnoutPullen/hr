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