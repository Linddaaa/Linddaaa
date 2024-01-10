
def main():
    #iegūstu dotos lielumus
    šķira = input("izvēlies šķiru (1. vai 2.):")
    platums = float(input("kāds ir dēļu platums:"))
    garums = float(input("kāds ir dēļu garums:"))
    biezums = float(input("kāds ir dēļu biezums:"))
    #uztaisu formulas (V = a*b*c)
    pirmā_šķira = ((platums * 145) + (garums * 145) + (biezums * 145))
    otrā_šķira = ((platums * 125) + (garums * 125) + (biezums * 125))
    #izreiķina 1. vai 2. šķiru, pieliek formulu, lai noapaļo divus ciparus aiz komata
    if "1." in šķira:
       print(format(pirmā_šķira, ".2f"))
    elif "2." in šķira:
       print(format(otrā_šķira, ".2f"))
main()