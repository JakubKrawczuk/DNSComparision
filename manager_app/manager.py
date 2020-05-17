import wzorzec as wzor
import importStruct
import threading
import socket
import os.path


class SendThread(threading.Thread):
    def __init__(self, psi, url):
        threading.Thread.__init__(self)
        self.url = url
        self.psi = psi

    def run(self):
        for q in self.psi:
            q.wyslijTest(self.url)


class ReceiveThread(threading.Thread):
    def __init__(self, count, q):
        super().__init__()
        self.q = q
        self.count = count
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("0.0.0.0", 5000))
        self.sock.settimeout(2000)

    def run(self):
        while self.count > 0:
            data, addr = self.sock.recvfrom(1024)
            self.count = self.count - 1
            print(data, self.count)
            self.q.append(data)
        self.sock.close()

def patternChange():
    global psi, wzorce
    plik_wzorcowy = "0"
    while len(plik_wzorcowy) > 0 and not os.path.isfile(plik_wzorcowy):
        print("Plik wzorca [struct.cfg]:")
        plik_wzorcowy = input()
    if len(plik_wzorcowy) > 0:
        [psi, wzorce] = importStruct.run(plik_wzorcowy)
    else:
        [psi, wzorce] = importStruct.run()

print("Nacisnij enter, aby rozpoczac")
input()

# lista prób porównawczych
patternChange()

zapytanie = ""
while zapytanie != "q":
    wynik = []

    print("Podaj zapytanie (q-quit, w-wzorzec)")
    zapytanie = input()
    if zapytanie == 'q':
        break
    elif zapytanie == 'w':
        patternChange()
        continue
    # zapytanie = "e3.dsk"

    receiveThread = ReceiveThread(len(psi), wynik)
    receiveThread.start()
    sendThread = SendThread(psi, zapytanie)
    sendThread.start()

    receiveThread.join()
    wynik = wzor.Psi.sortWynik(psi, wynik, zapytanie)
    opinia = wzor.Wzorzec.sprawdz(wzorce, wynik)
    print("Opinia:", opinia)
