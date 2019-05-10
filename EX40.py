import numpy.random as np

def determ():
    tomb=[]
    szamlalo=0
    while szamlalo!=5:
        a=np.randint(0,10)
        b=np.randint(0,10)
        c=np.randint(0,10)
        d=np.randint(0,10)
        if 10<= (a*d-b*c) <=20:
            szamlalo += 1
            print("a:", a, "b:", b, "c:", c, "d:", d)
            tomb = [[a, b], [c, d]]
            for i in tomb:
                print(i)