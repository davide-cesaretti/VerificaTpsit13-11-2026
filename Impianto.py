from pannello.py import PannelloFotovoltaico

class ImpiantoSolare:
    def __init__(self, codice:str, modello:str, localita:str, potenza_massima_kw: float, stato:str, pannelli: list[PannelloFotovoltaico]):
        self.codice = codice
        self.modello = modello
        self.localita = localita
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli = pannelli
        
    

