def tab(signs: int, s):
    s = str(s)
    return s + " "*(signs-len(s))

def printf(s: str):
    print(s, end="")

def printTable(f:int, o:str):
    signs = len(str(f*f))
    printf(tab(signs, o))
    for i in range(f):
        printf(tab(signs, i))
    print()
    for i in range(f):
        printf(tab(signs, i))
        for j in range(f):
            printf(tab(signs, int(eval(f"{i}{o}{j}")) % f))
        print()

def fEval(f: int, s: str):
    print(int(eval(s)) % f)
    
printTable(7, '+')
print()
printTable(7, '*')

while True:
    fEval(7, input())