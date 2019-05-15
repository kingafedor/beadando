def leghosszabbpalindromresz(st):
    n = len(st)
    table = [[0 for x in range(n)] for y
             in range(n)]
    maxhossz = 1
    i = 0
    while (i < n):
        table[i][i] = True
        i = i + 1

    start = 0
    i = 0
    while i < n - 1:
        if (st[i] == st[i + 1]):
            table[i][i + 1] = True
            start = i
            maxhossz = 2
        i = i + 1

    k = 3
    while k <= n:
        i = 0
        while i < (n - k + 1):
            j = i + k - 1

            if (table[i + 1][j - 1]==True and st[i] == st[j]):
                table[i][j] = True

                if (k > maxhossz):
                    start = i
                    maxhossz = k
            i = i + 1
        k = k + 1
    print("A leghosszabb rész-palindrom: ", st[start:start + maxhossz])


try:
    st=input("A feladat kiírja a kapott string leghosszabb rész-palindromját: ")
    print()
    #st = "forgeeksskeegfor"
    leghosszabbpalindromresz(st)
except TypeError:
    print("Adjon meg érvényes stringet!")
