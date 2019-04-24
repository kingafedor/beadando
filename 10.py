try:
    szamok = input("Adj meg harom szamot:")
    while szamok != '0':
        ls = szamok.split(" ")

        for i in range(len(ls)):
            ls[i] = int(ls[i])

        print(ls)
        for i in range(len(ls)-1):
            for j in range(i+1, len(ls)):
                if ls[i] > ls[j]:
                    ls[i], ls[j] = ls[j], ls[i]

        print(ls[1])

        szamok = input("Adj meg harom szamot:")

except ValueError:
    print("Hibas bemenet.")
