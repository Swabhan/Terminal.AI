import math

def dot(u,v):
    '''Calculate the dot product between vectors u and v'''
    if len(u) != len(v):
        print("ERROR -  dimensions not equal")
    else:
        temp = 0
        for i in range(len(u)):
            temp += u[i]*v[i]
        return temp
    



def multiply(m1,m2):
    '''Calculate the matrix multiplication between m1 and m2 represented as list-of-list.'''
    n = len(m1)
    d = len(m2)
    m = len(m2[0])
    
    if len(m1[0]) != d:
        print("ERROR - inner dimentions not equal")
    else:
        result = [[0 for i in range(n)] for j in range(m)]
        for i in range(0,n):
            for j in range(0,m):
                for k in range(0,d):
                    result[i][j] = result[i][j] + m1[i][k] * m2[k][j]
        return result
    


def add_vectors(v1,v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]+v2[i])
    return v3



def sub_vectors(v1,v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]-v2[i])
    return v3



def norm(u):
    '''Calculate the norm of vector u'''
    nm = 0
    for i in range(len(u)):
        nm += u[i]*u[i]
    return math.sqrt(nm)



def transpose(A):
    '''Calculate the transpose of matrix A represented as list of lists'''
    # number of rows
    n = len(A[0]) 
    # number of columns
    m = len(A) 

    AT = list()
    for j in range(0,m):    
        temp = list()
        for i in range(0,n):
            temp.append(A[i][j])
        AT.append(temp)
    return AT



def proj(v,u):
    
    pv = [ dot(v, u) / dot(u, u)*i for i in u]
    
    return pv


def subtract(a, b):
    return [(a_ - b_) for (a_, b_) in list(zip(a, b))]
