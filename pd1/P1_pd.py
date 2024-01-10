
def main():
    #ierakstu vajadzīgos lielumus
    vārds = (input("ievadiet vārdu:"))
    uzvārds = (input("ievadiet uzvārdu:"))
    stundas = float(input("cik stundas jūs nostrādājat mēnesī:"))
    likme = float(input("cik ir jūsu stundas likme:"))
    #parastas algas apreiķināšanas formula
    alga = (float(stundas)) * (float(likme))
    #kā apreiķināt 10% no visas algas
    procenti = 10/100 * alga
    #alga ar procentiem kopā
    alga2 = procenti + alga
    #funkcija, kas parāda algu, ja stundas ir virs 40 vai zem
    if stundas < 40:
        print(vārds, uzvārds, alga, " eiro alga")
    elif stundas > 40:
       print(vārds, uzvārds, alga2, "eiro alga")
main()

