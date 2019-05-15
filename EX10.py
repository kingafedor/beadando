tombregi=input("Adjon meg bináris számokat (max 5 jegyű) ;-vel elválasztva: ")
karakterek=["0","1",";"]

for betu in tombregi:
    if betu not in karakterek:
        print("Adjon meg helyes értéket!")
        tombregi = input("Adjon meg bináris számokat (max 5 jegyű) ;-vel elválasztva: ")
    else:
        continue

ujtomb=tombregi.split(";")

print(tombregi)
print(ujtomb)

ujtombbin=[]
ujtombdec=[]

for szam in ujtomb:
    decszam = 0
    seged = 1
    for j in range(len(szam) - 1, -1, -1):
        if int(szam[j]) == 1:
            decszam += seged
        seged = seged * 2

    if decszam%3==0 and decszam!=0:
        ujtombbin.append(szam)
        ujtombdec.append(decszam)

print()
print(ujtombbin)
print(ujtombdec)
