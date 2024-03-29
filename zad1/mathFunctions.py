import math
import matplotlib.pyplot as plt

bazaFunkcji = [
    ['tryg',"sin", 1, 1, 0,0,], # sin(x)
    ['wyk',1,2,1,1,11], # 2^(x+1) + 11
    ['wielo',1,0,-2,-2] # x^3 - 2x - 2
]


def rozwiazWielomioan (wspolczynniki, x):
    #wspolczynniki = [wspolczynnikPrzyX^3, wspolczynnikPrzyX^2, wspolczynnikPrzyX^1, wyrazWolny]
    wynik = 0
    for i in range(len(wspolczynniki)):
        wynik = wynik * x + wspolczynniki[i]
    return wynik
def rozwiazWykladnicze(wspolczynniki, x):
    #wspolczynniki = [podstawa, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY]
    nowyX = x
    if wspolczynniki[2] == "x":
        wspolczynniki[2] = x
        nowyX = 1
    return wspolczynniki[0]*(pow(wspolczynniki[1],(wspolczynniki[2] * nowyX) + wspolczynniki[3])+ wspolczynniki[4])
def rozwiazTrygonometryczne(wspolczynniki, x ):
    #wspolczynniki = [funTryg, wspolczynnikPrzyY, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY,]

    if wspolczynniki[0] == "sin":
        return wspolczynniki[1]  * math.sin(wspolczynniki[2] * x + wspolczynniki[3]) + wspolczynniki[4]
    elif wspolczynniki[0] == "cos":
        return wspolczynniki[1] * math.cos(wspolczynniki[2] * x + wspolczynniki[3]) + wspolczynniki[4]
    elif wspolczynniki[0] == "tan":
        return wspolczynniki[1] * math.tan(wspolczynniki[2] * x + wspolczynniki[3]) + wspolczynniki[4]
    elif wspolczynniki[0] == "sin/cos":
        sincos = math.sin(wspolczynniki[2] * x + wspolczynniki[3]) / math.cos(wspolczynniki[2] * x + wspolczynniki[3])
        return wspolczynniki[1] * sincos * + + wspolczynniki[4]
    else:
        raise Exception("Nieznana funkcja trygonometryczna")
def rozwiazRowanianie(kolejnoscFunkcji,x):
    if len(kolejnoscFunkcji) != 1:
        kolejnoscFunkcji = list(reversed(kolejnoscFunkcji))
    wynik = 0
    for i in range(len(kolejnoscFunkcji)):
        funkcja = kolejnoscFunkcji[i][1:]
        keyFunkcja = kolejnoscFunkcji[i][0]

        if i != 0:
            match (keyFunkcja):
                case "tryg":  # trygonometrycnza -
                    wynik = rozwiazTrygonometryczne(funkcja, wynik)
                case "wyk":  # wykladniczza -
                    wynik = rozwiazWykladnicze(funkcja, wynik)
                case "wielo":  # wielomian -
                    wynik = rozwiazWielomioan(funkcja, wynik)
                case _:
                    raise Exception("Nieznana funkcja")
        else:
            match (keyFunkcja):
                case "tryg":  # trygonometrycnza -
                    wynik = rozwiazTrygonometryczne(funkcja, x)
                case "wyk":  # wykladniczza -
                    wynik = rozwiazWykladnicze(funkcja, x)
                case "wielo":  # wielomian -
                    wynik = rozwiazWielomioan(funkcja, x)
                case _:
                    raise Exception("Nieznana funkcja")
    return wynik
def metodaBisekcjiDokladnosc (kolejnoscFunkcji, a, b, dokladnosc):
    wartoscNaA = rozwiazRowanianie(kolejnoscFunkcji, a)
    wartoscNaB = rozwiazRowanianie(kolejnoscFunkcji, b)
    if (wartoscNaA > 0 and wartoscNaB > 0) or (wartoscNaA < 0 and wartoscNaB < 0):
        raise Exception("Bledna dziedzina")
    srodek = (a + b) / 2
    wartoscSrodka = 0
    licznik = 0
    while abs(rozwiazRowanianie(kolejnoscFunkcji, (a + b) / 2)) > dokladnosc:
        licznik += 1

        wartoscA = rozwiazRowanianie(kolejnoscFunkcji, a)
        wartoscB = rozwiazRowanianie(kolejnoscFunkcji, b)
        wartoscSrodka = rozwiazRowanianie(kolejnoscFunkcji, srodek)

        if wartoscSrodka == 0:
            return [srodek,wartoscSrodka]
        elif (wartoscA > 0 and wartoscSrodka < 0) or (wartoscA < 0 and wartoscSrodka > 0):
            b = srodek
        elif (wartoscB > 0 and wartoscSrodka < 0) or (wartoscB < 0 and wartoscSrodka > 0):
            a = srodek
        srodek = (a + b) / 2
    return [srodek,wartoscSrodka, licznik]

def metodaBisekcjiIloscIteracji (kolejnoscFunkcji, a, b, iloscIteracji):
    wartoscNaA = rozwiazRowanianie(kolejnoscFunkcji, a)
    wartoscNaB = rozwiazRowanianie(kolejnoscFunkcji, b)
    if (wartoscNaA > 0 and wartoscNaB > 0) or (wartoscNaA < 0 and wartoscNaB < 0):
        raise Exception("Bledna dziedzina")
    licznik = 0
    srodek = (a + b) / 2
    wartoscSrodka = 0

    while (licznik < iloscIteracji):
        licznik += 1

        wartoscA = rozwiazRowanianie(kolejnoscFunkcji, a)
        wartoscB = rozwiazRowanianie(kolejnoscFunkcji, b)
        wartoscSrodka = rozwiazRowanianie(kolejnoscFunkcji, srodek)

        if wartoscSrodka == 0:
            return [srodek,wartoscSrodka, licznik]
        elif (wartoscA > 0 and wartoscSrodka < 0) or (wartoscA < 0 and wartoscSrodka > 0):
            b = srodek
        elif (wartoscB > 0 and wartoscSrodka < 0) or (wartoscB < 0 and wartoscSrodka > 0):
            a = srodek
        srodek = (a + b) / 2
    return [srodek, wartoscSrodka, licznik]
def pochodnaWielomian(wspolczynniki):
    stopien = len(wspolczynniki) - 1
    noweWspolczynniki = []
    for i in range(stopien):
        noweWspolczynniki.append(wspolczynniki[i]*stopien)
        stopien -= 1
    return noweWspolczynniki
def pochodnaTrygonometrycznej(wspolczynniki):
    #wspolczynniki = [funTryg, wspolczynnikPrzyY, wspolczynnikPrzyX, wspolczynnikDoX, wspolczynnikDoY,]
    noweWspolczynniki = wspolczynniki
    if wspolczynniki[0] == "sin":
        noweWspolczynniki[0] = "cos"
        return noweWspolczynniki
    elif wspolczynniki[0] == "cos":
        noweWspolczynniki[0] = "sin"
        noweWspolczynniki[1] = wspolczynniki[1] * (-1)
        return noweWspolczynniki
    elif wspolczynniki[0] == "tan":
        noweWspolczynniki[0] = "sin/cos"
        return noweWspolczynniki
    else:
         raise Exception("Nieznana funkcja trygonometryczna")
def pochodnaWykladniczej(wspolczynniki):
    noweWspolczynniki = []
    noweWspolczynniki.append(math.log(wspolczynniki[1]))
    noweWspolczynniki.append(wspolczynniki[1])
    noweWspolczynniki.append("x")
    noweWspolczynniki.append(wspolczynniki[3])
    noweWspolczynniki.append(0)
    return noweWspolczynniki
def pochodnaZlozen(kolejnoscFunkcji):
    kolejnoscPochodnych = []
    for i in range(len(kolejnoscFunkcji)):

        funkcja = kolejnoscFunkcji[i][1:]
        keyFunkcja = kolejnoscFunkcji[i][0]
        match (keyFunkcja):
            case "tryg":  # trygonometrycnza -
                pochodna = pochodnaTrygonometrycznej(funkcja)
                pochodna.insert(0,"tryg")
                kolejnoscPochodnych.append(pochodna)
            case "wyk":  # wykladniczza -
                pochodna = pochodnaWykladniczej(funkcja)
                pochodna.insert(0,"wyk")
                kolejnoscPochodnych.append(pochodna)
            case "wielo":  # wielomian -
                pochodna = pochodnaWielomian(funkcja)
                pochodna.insert(0,"wielo")
                kolejnoscPochodnych.append(pochodna)
            case _:
                raise Exception("Nieznana funkcja")
    return kolejnoscPochodnych
def obliczWartoscPochodnychZlozen(kolejnoscFunkcji,kolejnoscPochodnych,x):
    wartosc = 1
    for i in range(len(kolejnoscPochodnych)):
        pochodna = [kolejnoscPochodnych[i]]
        funkcje = kolejnoscFunkcji[i+1:]
        if funkcje == []:
            wartoscFunkcjiZlozonych = x
        else:
            wartoscFunkcjiZlozonych = rozwiazRowanianie(funkcje,x)
        wartoscPochodnej = rozwiazRowanianie(pochodna,wartoscFunkcjiZlozonych)
        wartosc *= wartoscPochodnej
    return wartosc
def metodasStycznejIteracje (kolejnoscFunkcji, a, b, iloscIteracji):
    wartoscNaA = rozwiazRowanianie(kolejnoscFunkcji, a)
    wartoscNaB = rozwiazRowanianie(kolejnoscFunkcji, b)
    if (wartoscNaA > 0 and wartoscNaB > 0) or (wartoscNaA < 0 and wartoscNaB < 0):
        raise Exception("Bledna dziedzina")
    kolejnoscPochodnych = pochodnaZlozen(kolejnoscFunkcji)
    xk = (a-b)/2
    licznik = 0
    while licznik < iloscIteracji:
        licznik += 1
        wartoscFunkcji = rozwiazRowanianie(kolejnoscFunkcji,xk)
        if wartoscFunkcji == 0:
            return [xk, wartoscFunkcji,licznik]
        wartoscPochodnej = obliczWartoscPochodnychZlozen(kolejnoscFunkcji,kolejnoscPochodnych, xk)
        temp = xk - (wartoscFunkcji / wartoscPochodnej)
        xk = temp
    return [xk,rozwiazRowanianie(kolejnoscFunkcji,xk),licznik]
def metodasStycznejDokladnosc (kolejnoscFunkcji, a, b, dokladnosc):
    wartoscNaA = rozwiazRowanianie(kolejnoscFunkcji, a)
    wartoscNaB = rozwiazRowanianie(kolejnoscFunkcji, b)
    if (wartoscNaA > 0 and wartoscNaB > 0) or (wartoscNaA < 0 and wartoscNaB < 0):
        raise Exception("Bledna dziedzina")
    kolejnoscPochodnych = pochodnaZlozen(kolejnoscFunkcji)
    xk = (a-b)/2
    licznik = 0
    while abs(rozwiazRowanianie(kolejnoscFunkcji,xk)) > dokladnosc:
        licznik += 1
        wartoscFunkcji = rozwiazRowanianie(kolejnoscFunkcji, xk)
        wartoscPochodnej = obliczWartoscPochodnychZlozen(kolejnoscFunkcji,kolejnoscPochodnych, xk)
        temp = xk - (wartoscFunkcji / wartoscPochodnej)
        xk = temp
    return [xk, rozwiazRowanianie(kolejnoscFunkcji, xk),licznik]
def wygenerujWykres (kolejnoscFunkcji, a,b, miejsceZerowe1, miejsceZerowe2):
    rozpietoscDziedziny = abs(a) + abs(b)
    iloscPunktow = rozpietoscDziedziny * 100

    #zaznaczanie miejsc zerowych z funkcji
    wartoscPZerowego1 = rozwiazRowanianie(kolejnoscFunkcji,miejsceZerowe1)
    wartoscPZerowego2 = rozwiazRowanianie(kolejnoscFunkcji,miejsceZerowe2)
    plt.plot(miejsceZerowe1,wartoscPZerowego1,marker='x', markersize=10, color="red", mec='r', mew=3)
    plt.plot(miejsceZerowe2,wartoscPZerowego2,marker='x', markersize=10, color="green", mec='g', mew=3)

    krok = rozpietoscDziedziny / iloscPunktow
    zbiorX = []
    zbiorY = []
    x = a
    zbiorX.append(x)
    zbiorY.append(rozwiazRowanianie(kolejnoscFunkcji, x))
    for i in range(int(iloscPunktow)):
        x += krok
        if  x > b:
            break
        zbiorX.append(x)
        wartoscWPunkcie = rozwiazRowanianie(kolejnoscFunkcji, x)
        zbiorY.append(wartoscWPunkcie)

    # domyslne wartosci
    figX = 6.4
    figY = 4.8
    dpi = 100
    titleSize = 10
    tickSize = 0.8 * titleSize

    if iloscPunktow > 300:


        #obliczam skale oraz skaluje
        skala = iloscPunktow / 300
        newfigX = figX * skala
        newfigY = figY * skala
        newdpi = dpi * skala
        newtitleSize = titleSize * skala
        newtickSize = newtitleSize * 0.8


        #stosuje przesklaowane wartosci
        fig = plt.gcf()
        fig.set_size_inches(newfigX, newfigY)
        fig.set_dpi(newdpi)
        plt.rc('font',size=newtitleSize)
        plt.xticks(fontsize=newtickSize)
        plt.yticks(fontsize=newtickSize)

        #generuje wykres
        plt.plot(zbiorX, zbiorY)
        plt.grid()
        plt.title("Wykres funkcji")
        plt.show()

        #przywracam wartosci domyslne
        fig.set_size_inches(figX, figY)
        fig.set_dpi(dpi)
        plt.rc('font',size=titleSize)
        plt.xticks(fontsize=tickSize)
        plt.yticks(fontsize=tickSize)
    else:
        #generuje wykres
        plt.plot(zbiorX, zbiorY)
        plt.grid()
        plt.title("Wykres funkcji")
        plt.show()


def pobierzFunkcje():
    textWyboruFunkcji = "Jaki typ funkcji chcesz podać?\n1 - trygonometryczne\n2 - wykladnicza\n3 - wielomianowa\n\tTwoj wybor: "
    wyborFunkcji = int(input(textWyboruFunkcji))
    wspolczynniki = []
    match wyborFunkcji:
        case 1:
            wspolczynniki.append("tryg")
            funkcjaTrygonometryczna = str(input("Podaj funkcje trygonometryczną [sin/cos/tan]: "))
            wspolczynniki.append(funkcjaTrygonometryczna)
            wspolczynniki.append(1.0) #nie pozwalamy uzytkownikowi wstawiac wartosci przy funkcji trygonometrycznej
            wspolczynnikiPrzyX = float(input("Podaj wspolczynnik przy x: "))
            wspolczynniki.append(wspolczynnikiPrzyX)
            wsplczynnikiDodawanyDoX = float(input("Podaj wspolczynnik dodawany do x: "))
            wspolczynniki.append(wsplczynnikiDodawanyDoX)
            wspolczynnikiDodawanyDoY = float(input("Podaj wspolczynnik dodawany do y: "))
            wspolczynniki.append(wspolczynnikiDodawanyDoY)
        case 2:
            wspolczynniki.append("wyk")
            wspolczynniki.append(1.0) #nie pozwalamy uzytkownikowi wprowadzac wartosci mnozacej wartosc podnoszona do potegi
            wspolczynnikiPodstawa = float(input("Podaj podstawe potegi: "))
            wspolczynniki.append(wspolczynnikiPodstawa)
            wspolczynniki.append(1.0)  # nie pozwalamy uzytkownikowi wprowadzac wartosci mnozacej x
            wspolczynnikDodawanyDoX = float(input("Podaj wspolczynnik dodawany do x: "))
            wspolczynniki.append(wspolczynnikDodawanyDoX)
            wspolczynnikiDodawanyDoY = float(input("Podaj wspolczynnik dodawany do y: "))
            wspolczynniki.append(wspolczynnikiDodawanyDoY)
        case 3:
            wspolczynniki.append("wielo")
            stopienWielomianu = int(input("Podaj stopien wielomianu: "))
            temp = stopienWielomianu
            for i in range(stopienWielomianu+1):
                wspolczynnik = float(input("Podaj wspolczynnik przy x w potedze {}.: ".format(temp)))
                wspolczynniki.append(wspolczynnik)
                temp -= 1
        case _:
            raise Exception("Nieznany wybor")
    return wspolczynniki


