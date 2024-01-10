
def tips():
#paprasa ievadīt doto lielumu
    a = input("ievadi dotā faila nosaukumu")
#meklē kurš ievadītais der
    if ".jpg" in a:
        print("šis ir attēls")
    elif ".gif" in a:
        print("šis ir attēls")
    elif ".bmp" in a:
        print("šis ir attēls")
    elif ".txt" in a:
        print("šis ir dokuments")
    elif ".doc" in a:
        print("šis ir dokuments")
    elif "pdf" in a:
        print("šis ir dokuments")
    else:
        print("fails nav definēts")
tips()
