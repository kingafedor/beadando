tombregi=input("Adjon meg bináris számokat (max 5 jegyű) ;-vel elválasztva: ")
ujtomb=tombregi.split(";")

print(tombregi)
print(ujtomb)

ujtombbin=[]
ujtombdec=[]

for szam in ujtomb:
    decszam = 0
    seged = 1