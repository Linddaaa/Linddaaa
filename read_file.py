f = open("mansteksts.txt", "r")
f.write("Now the file has more con")
for x in f: 
    print(x)
print(f.readline())