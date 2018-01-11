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