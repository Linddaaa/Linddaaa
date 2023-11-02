# name = input("whats your name?")
# print(f"hello, {name}")

# name = input("whats your name?")
# file = open("names.txt","w")
# file.write(name)
# file.close()


# name = input("whats your name?")
# file = open("names.txt","a")
# file.write(f"{name}\n")
# file.close()

#noteikt tekstā cik rindiņas sākās ar burtu T
# def line_count():
#     file = open("story.txt", "r")
#     count = 0
#     for line in file:
#         if line[0] not in 'T':
#             count+=1
#     file.close()
#     print("No of lines not starting with 'T'=", count)

# line_count()

def burti_a(fails):
    with open(fails, 'r') as f:
        saturs = f.read()
        skaits = saturs.count('a')
    return skaits 
fails = "teksts.txt"
skaits = burti_a(fails)
print(f"Failā '{fails}' ir {skaits} burti 'a'.")