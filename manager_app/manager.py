import wzorzec as wzor
import importStruct
import threading
import socket


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


# lista prób porównawczych
[psi, wzorce] = importStruct.run()

print("Nacisnij enter, aby rozpoczac")
input()
zapytanie = ""
while zapytanie != "q":
    wynik = []

    print("Podaj zapytanie (q-quit)")
    zapytanie = input()
    if zapytanie == 'q':
        break
    # zapytanie = "e3.dsk"

    receiveThread = ReceiveThread(len(psi), wynik)
    receiveThread.start()
    sendThread = SendThread(psi, zapytanie)
    sendThread.start()

    receiveThread.join()
    wynik = wzor.Psi.sortWynik(psi, wynik, zapytanie)
    opinia = wzor.Wzorzec.sprawdz(wzorce, wynik)
    print("Opinia:", opinia)
