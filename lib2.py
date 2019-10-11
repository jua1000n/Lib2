from sys import stdin

def conj(i):
    r = [i[0], i[1]]
    res1 = -1 * r[1]
    r[1] = res1
    p=(r[0],r[1])
    return p

def producto(r, i):
    res1 = (r[0] * i[0]) - (r[1] * i[1])
    res2 = (r[0] * i[1]) + (r[1] * i[0])
    return (round(res1,4), round(res2,4))

def suma(r, i):
    res1 = r[0] + i[0]
    res2 = r[1] + i[1]
    return (round(res1,4), round(res2,4))

def multimat(r,i):
    mat = [[(0,0)]*len(i[0]) for h in range(len(r))]
    for y in range(len(r)):
        for j in range(len(i[0])):
            if len(mat)==1:
                long=2
            else:
                long=len(mat)
            for z in range(long):
                mat[y][j]=suma(mat[y][j],producto(r[y][z],i[z][j]))
    return mat

def matAdjun(r):
    mat=matTrans(matConj(r))
    return mat

def matTrans(r):
    mat=[]
    for y in range(len(r[0])):
        mat.append([])
        for x in range(len(r)):
            mat[y].append(r[x][y])
    return mat

def matConj(r):
    mat=[]
    for y in range(len(r)):
        mat.append([])
        for x in range(len(r[0])):
            mat[y].append(conj(r[y][x]))
    return mat

def proba(lis,pos):
    res=(abs((lis[pos-1][0][0])**2+(lis[pos-1][0][1]**2))/((mag(lis))**2))
    return round(res,4)

def mag(lis):
    res=0
    for i in range(len(lis)):
        res+=abs((lis[i][0][0])**2+(lis[i][0][1])**2)
    return res**(1/2)

def transi(lis1,lis2):
    p=(multimat(matAdjun(lis2[1]),lis1[1])[0][0][1])
    r=(mag(lis1[1])*mag(lis2[1]))
    return round(p/r,2)
    

