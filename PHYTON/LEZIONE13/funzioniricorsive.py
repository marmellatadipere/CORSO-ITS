#Lezione 27 marzo


#esercizio 1
'''
def recursive_countdown(n:int) -> None: #caso in cui la ricorsione non deve partire
    if n < 0:
        print("ERROR")
    elif n == 0:
        print(0)
    else:
        print(n)
        recursive_countdown(n-1)
'''

#esercizio 2
'''
def recursiveSum(n:int) -> int:
    if n < 0:
        print("ERROR")
        return 0
    elif n == 0:
        return 0
    else:
        return int(n + recursiveSum(n-1))
'''


#esercizio 3 
def recursiveSumInRange(a:int, b:int) -> int:
    if a > b:
        temp:int = a
        a = b
        b = temp
    elif b == a:
        return int(a)
    else:
        return int(b + recursiveSumInRange(a, b-1))