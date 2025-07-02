def numeratore(self): # x:int, seq:dict[int,list[int]]
    seq = []
    freq = {}        
    while True:       
        numx = float(input("Inserire il numero X:\n"))
        if numx.is_integer() and numx > 0:      
            numseq = float(input("Inserire un nero intero positivo nella sequenza:\n"))
            while True:
                if numseq.is_integer() and numseq > 0:
                    if numseq not in freq:
                        freq[numseq] = 1
                    else:
                        freq[numseq] += 1
                seq.append(numseq)
            else:
                print("inserire un numero intero e maggioe di ZERO")   
    else:
        numx = float(input("inserire un numero intero e maggioe di ZERO"))

    print(freq)
    



if __name__ == "__main__":
    prova = numeratore(self="start")

        
        