from math import sqrt,log

def coeff_CL(b,p):
    bp=b%p # on calcule le reste de la division Euclidienne de b par p
    L=[1] # le premier coefficient de la liste L est b^0=1
    while True:
        if  bp in L: #on se retouve au début de la nouvelle période
            L.append(bp) # le coefficient est ajouté en fin de liste L
            break
        L.append(bp)
        bp=bp*b%p
# On cherche à améliorer la lecture des coeff en détectant certains cas
    Lm=[k  if k==0 or abs(log(k)/log(b)-int(log(k)/log(b)))<10**-12 or k<=p//2 and k!=p-b else k-p for k in L]
    del(L)
    return Lm

def bestbase(p,rk):
    Lbase=[]
    Lscore=[]
    for k in range(2,p-1):
        Lck=coeff_CL(k,p)
        sc=len(Lck)-1
        Lscore.append(sc)
        Lbase.append(str(sc)+"\tBase "+str(k)+": \t("+"".join(str(j)+" ," for j in Lck)+"...)\n")
    Ls,Lb=zip(*sorted(zip(Lscore,Lbase)))
    if len(Ls)>rk:
        Lb,Ls=Lb[:rk],Ls[:rk]
    return "Score\tDivisibilité par "+str(p)+"\n"+"".join(j for j in Lb)+"\n"

def primeN(n0,n1):
    L=[]
    for k in range(n0,n1,2):
        if all(k%i!=0 for i in range(3,int(sqrt(k))+1, 2)):
            L.append(k)
    return L

def divisi(n,b):
    txt="Critères de divisibilité en base "+str(b)+"\n"
    for k in range(2,n+1):
        Lck=coeff_CL(b,k)
        txt+=str(k)+" : ("+"".join(str(j)+" ," for j in Lck)+"...)\n"
        del(Lck)
    return txt

#print(divisi(100,10))
#print(divisi(100,2))

def ListeDiv5P(n):
    Lp=primeN(5,n)
    for k in Lp:
        print(bestbase(k,12))
    return Lp

def baseScore(p):
    """Renvoie la liste de toutes les périodes du critère de divisibilité par p
    dans toutes les bases non triviales"""
    Lscore=[]
    L=[]
    for k in range(2,p-1):
        Lscore.append(len(coeff_CL(k,p))-1)
    L=sorted(Lscore)
    del(Lscore)
    return L

def Sign_base(n):
    Lp=primeN(5,n)
    bs=[]
    for k in Lp:
        bS=baseScore(k)
        if bS[0] not in bs:
            bs.append(bS[0])
        print(str(k)+" :\t",bS[:24])
    return sorted(bs)

