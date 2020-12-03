from sympy import factorint
#Critère de divisibilité dans une base optimale d'un premier p

def p_bestbase(p):
    """Renvoie la période minimale du critère de divisibilité par le
    premier p, étudie pour cela l'entier m tel que p=2*m+1"""
    m = (p-1)//2
    Lf = factorint(m) #produit un dictionnaire où chaque clé est un premier
    if len(Lf)*list(Lf.values())[0]==1: #cas où m est premier {p:1}
        if m == 2:
            n = 4 #cas particulier p=5
        else:
            n = m
    else: #cas où m est composé
        n0 = n1 = m
        for k in Lf.keys(): # détermination des deux plus petits facteurs de m
            if k < n0:
                n1 = n0
                n0 = k
            else:
                n1 = min(n1,k)
        if n0 == 2: # cas m est un nombre pair
            n = min(4,n1) # discrimine le cas n1 =3
        else:
            n = n0
    return n

def resolmod1(n,p):
    """cherche une base b non triviale solution de l'équation b^n=1[p]"""
    for k in range(2,p-1):
        if test1(k,n,p): #teste si k^n = 1 [p]
            return k #renvoie la première base optimale
    return False

def test1(b,n,p):
    """Teste si b^n=1[p]"""
    B = b
    for k in range(n-1):
        B = (b*B)%p
    return B == 1

def affich_best_bases(p):
    """Détermine la liste des bases optimales pour
     le critère de divisibilité par p"""
    n = p_bestbase(p)
    b0 = resolmod1(n,p)
    if (p-1)//2==n:
      txt="c'est un premier sûr: "+str(b0)+": \n(1, "
	  CL=""
	for k in range(2,n):
		CL+=
    else:
        txt="{"
		
	return txt


