import wzorzec as wzor

##########################################
######  IMPORT STRUKTURY Z PLIKU  ########
##########################################

def run(filename = "./struct.cfg"):
    psi = []
    wzorce = []

    #3 pierwsze linie dla prób porównawczych
    linieProb = 3
    zbiorProb = []
    linieWzorca = 0
    wzorOdp = []
    opinia = []
    with open(filename) as f: 
        for line in f:
            line = line.split("//",1)[0].strip() #ignoring comment lines //
            if line != "":
                if linieProb > 0:
                    zbiorProb.append(line.split(";"))
                    linieProb = linieProb - 1
                else:
                    [wz, op] = line.split(";;")
                    wzorOdp.append(wz)
                    opinia.append(op)
                    linieWzorca = linieWzorca + 1

    liczbaProb = len(zbiorProb[0])
    for i in range(0,liczbaProb):
        k = zbiorProb[0][i].strip()
        p = [zbiorProb[1][i].strip(), zbiorProb[2][i].strip()]
        psi.append(wzor.Psi(k,p))

    liczbaWzorcow = len(wzorOdp)
    for i in range(0, liczbaWzorcow):
        wzorce.append(wzor.Wzorzec(wzorOdp[i], opinia[i]))
		
    return [psi, wzorce]