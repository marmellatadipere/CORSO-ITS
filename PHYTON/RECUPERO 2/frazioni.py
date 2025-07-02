class Frazione:
    def __init__(self, __numeratore:int, __denominatore:int):
        self.numeratore = __numeratore
        self.denominatore = __denominatore

    @property
    def numeratore(self):
        return self.__numeratore
    
    @property
    def denominatore(self):
        return self.__denominatore
    
    
    @numeratore.setter
    def numeratore(self, valore:int):
        if float(valore).is_integer():
            self.__numeratore = valore
        else:
            self.__numeratore = 15

    @denominatore.setter
    def denominatore(self, valore):
        if valore != 0 and float(valore).is_integer():
            self.__denominatore = valore
        else:
            self.__denominatore = 13

    def __str__(self):
        return f"{self.__numeratore} / {self.__denominatore}"
    
    def value(self):
        valore:float = (self.__numeratore / self.__denominatore)
        return round(valore,3)
    
def mcd(x:int , y: int) -> int:
    divisoriX = []
    divisoriY = []
    divisoriComuni = []
    risultato: int = 0

    if x != y :
        for numero in range(1,(x + 1)):
            if x % numero == 0:
                divisoriX.append(numero)
        for numero in range(1,(y + 1)):
            if y % numero == 0 and numero in divisoriX:
                divisoriY.append(numero)
                divisoriComuni.append(numero)
        if len(divisoriComuni) > 0:
            risultato = max(divisoriComuni)
        else:
            risultato = 1
            
    else:
        risultato = x 

    return risultato


def semplifica(l:list[Frazione]) -> list[Frazione]:
    frazioniIrriducibili = []
    for elemento in l:
        num = elemento.numeratore
        den = elemento.denominatore
        maxcomdiv = mcd(num , den)
        if maxcomdiv == 1:
            frazioniIrriducibili.append(elemento)
        else:
            elementosemplificato = Frazione((num / maxcomdiv) , (den / maxcomdiv))
            frazioniIrriducibili.append(elementosemplificato)

    return frazioniIrriducibili

        

def fractionCompare(l:list[Frazione], ls: list[Frazione]):
    i = 0

    for element in l:
        b = ls[i].value()
        if element.value()!= b:
            print("Errore")
        else:
            print(f"il rapporto {element.value()} è uguale al rapporto {b}")
            i += 1

        
    
if __name__ == "__main__":
    frazione1 = Frazione(6,3) #oggetto della classe frazione con attributi numeratore = 6 e denominatore = 3
    frazione1.value() #richiamo la funzione value sull' oggetto frazione1
    print(frazione1.value())
    maxcommdiv = mcd(frazione1.numeratore, frazione1.denominatore)
    print(f"Il massimo comun divisore tra il numeratore e il denominatore è:\n{maxcommdiv}")


    l = [
        Frazione(2.5, 0),     # valori invalidi → default 13/5
        Frazione(1, 2),
        Frazione(2, 4),
        Frazione(3, 5),
        Frazione(6, 9),
        Frazione(4, 7),
        Frazione(24, 36),
        Frazione(12, 36),
        Frazione(40, 60),
        Frazione(5, 11),
        Frazione(10, 45),
        Frazione(42, 78),
        Frazione(9, 15)
    ]

    l_s = semplifica(l)
    for f in l_s:
        print(f)
    fractionCompare(l, l_s)