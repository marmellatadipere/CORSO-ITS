
def interoInput(s:str) -> int:
     s = float((input(" ")))
     if s.is_integer() and s > 0:
        return int(s)

def numeratore(seq:list[int] = [], freq:dict[int, int] = {}): # x:int, seq:dict[int,list[int]]

        numx = interoInput("Inserisci un numero intero")
        if numx.is_integer() and numx > 0:
            numseq = float(input("Inserire un nero intero positivo nella sequenza"))
            if numseq.is_integer() and numseq > 0:
                if numseq not in freq:
                    freq[numseq] = 1
                else:
                    freq[numseq] += 1
                seq.append(numseq)
            else:
                    numx = float(input("inserire un numero intero e maggioe di ZERO"))        
        else:
            numx = float(input("inserire un numero intero e maggioe di ZERO"))

        print(freq) 
        print(f"il numero x : {numx} appare {freq[numx]} volte")
#       print(f"la posizione del numero x nella sequenza è {}")
        for numeri in seq:
            sum = 0
            if numeri != numx:
                sum += numeri
        print(f"La somma di tutti i numeri inseriti diveri dal numero x è {sum}")



if __name__ == "__main__":
    prova = numeratore(self="start")

        
        