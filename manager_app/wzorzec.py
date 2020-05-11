class Psi:
    def __init__(self, komparator, paraPorownawcza):
        self.k = komparator
        self.p = paraPorownawcza
    
    def wyslijTest(self, url):
        print("wyslij do ", self.k, " zapytanie o porownanie", self.p, " url: ", url);

class Wzorzec:
    def __init__(self, wzorzec, opinia):
        self.w = map(str.strip, wzorzec.split(";"))
        self.o = opinia.strip()
        
    def sprawdz(self, wynik):
        print("jeśli zgodny ", list(self.w), " to opinia", self.o);
        return False #lub opinia
        