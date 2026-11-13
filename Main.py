from Impianto import ImpiantoSolare

if __name__ == "__main__":
    
    def registra_impianto(impianti: list[ImpiantoSolare], impianto: ImpiantoSolare):
        for i in impianti:
            if(impianto.codice == i.codice):
                return ValueError("impianto gia presente")
        impianti.append(impianto)    
    
    def cerca_impianto(impianti: list[ImpiantoSolare], codice: str):
        return [impianto for impianto in impianti if impianto.codice == codice]
        
    def repilogo_impianti(impianti: list[ImpiantoSolare]):
        for i in impianti:
            print(f"{impianto.codice}")
            
 