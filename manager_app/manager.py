import wzorzec as wzor
import importStruct

def sendAll(psi, url):
    for q in psi:
        q.wyslijTest(url)

#lista prób porównawczych    
[psi, wzorce] = importStruct.run()
input()
print("Podaj zapytanie")
zapytanie = input()

sendAll(psi, zapytanie)