import socket


class Psi:
    def __init__(self, komparator, paraPorownawcza):
        self.k = komparator
        self.p = paraPorownawcza

    def wyslijTest(self, url):
        port = 5000
        msg = str(self.k) + ";;" + ';'.join(map(str, self.p)) + ";;" + url
        print("Wysylam do", "jkdsk_dns_" + self.k,
              "(" + socket.gethostbyname("jkdsk_dns_" + self.k) + ":" + str(port) + ")", "zapytanie o porownanie",
              self.p, " url:", url, " (" + msg + ")")
        byte_message = bytes(msg, "utf-8")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(byte_message, (socket.gethostbyname("jkdsk_dns_" + self.k), port))
        sock.close()

    @classmethod
    def sortWynik(cls, psi, wynik, url):
        sorted = []
        for p in psi:
            sstr = str(p.k) + ";;" + ';'.join(map(str, p.p)) + ";;" + url + ";;"
            for w in wynik:
                w = w.decode('utf-8')
                if w.startswith(sstr):
                    sorted.append(w[-1])
        return sorted


class Wzorzec:
    def __init__(self, wzorzec, opinia):
        self.w = list(map(str.strip, wzorzec.split(";")))
        self.o = opinia.strip()

    @classmethod
    def sprawdz(cls, wzorce, wynik):
        for lp in wzorce:
            fit = True
            w = lp.w
            for i in range(0, len(w)):
                if w[i] != 'x' and w[i] != wynik[i]:
                    fit = False
                    break
            if fit:
                print(wynik)
                print(w)
                return lp.o

        return False
