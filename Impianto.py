from Pannello import PannelloFotovoltaico

class ImpiantoSolare:
    def __init__(self, codice:str, modello:str, localita:str, potenza_massima_kw: float, stato:str, pannelli: list[PannelloFotovoltaico]):
        self.codice = codice
        self.modello = modello
        self.localita = localita
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli = pannelli
        
    
    def aggiungi_pannello(self, pannello: PannelloFotovoltaico) -> None :
        valid = True
        for p in self.pannelli:
            if p.codice == pannello.codice:
                valid = False
         
        somma = self.potenza_pannelli()
        if(somma + pannello.potenza_kw > self.potenza_massima_kw):
            valid = False
            
        if(valid == False ):
            return ValueError("pannello non valido")
        else:
            self.pannelli.append((pannello))
            

    def potenza_pannelli(self) -> float:
        somma = 0
        for p in self.pannelli:
            somma += p.potenza_kw
        return somma
    
    def cerca_pannello(self, codice:str):
        return[pannello in self.pannelli if pannello.codice == codice else None]
    
    def rimuovi_pannello(self, codice:str):
        for p in self.pannelli:
            if(p.codice == codice):
                self.pannelli.remove(p)
                return p
            
        return None
    
    def pannelli_sotto_potenza(self, potenza_massima:float) ->list[PannelloFotovoltaico]:
        pannelli =[]
        pannelli.append(pannello for pannello in self.pannelli if pannello.potenza_kw < potenza_massima)
        return pannelli
