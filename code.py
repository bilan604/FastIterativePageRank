import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer
from numpy import sqrt, dot, array, diagonal, mean, transpose, eye, diag, ones
from numpy import transpose, diag, dot
from numpy.linalg import svd, inv, qr
from sklearn.linear_model import LinearRegression

def getTop20(toSort, U):
    if type(toSort) != Matrix:
        if type(toSort) != list:
            toSort = list(toSort)
        if type(toSort[0]) != float:
            toSort = [xi[0] for xi in x]
        dd = {i:toSort[i] for i in range(len(toSort))}
        dd = dict(sorted(dd.items(), key=lambda item: item[1]))
        sortedInds = list(reversed(list(dd.keys())))[:20]
        return [(toSort[i], U[i]) for i in sortedInds]
    else:
        used, top20 = [], []
        while len(top20) < 20:
            _ind = 0
            best = -1
            for link in matrix.links:
                if link.page_rank > best and link.ind not in used:
                    _ind, best = link.ind, link.page_rank
            top20.append((best, U[_ind]))
            used.append(_ind)
    return top20

def viewTop20(top20):
    for row in top20:
        if len(row[1]) > 65:
            print("PAGERANK: ", row[0], "      LINK: ",  row[1][:65], "...", sep="")

        else:
            print("PAGERANK: ", row[0], "     LINK:",  row[1])

def makeP(A):
    n = len(A)
    p = 0.85
    p1 = 0.15/n
    p2 = 1.0/n
    P = []
    for i in range(n):
        r = []
        ri = sum(A[i])
        if sum(A[i]) > 0:
            for j in range(n):
                r.append(p*(A[i,j]/ri) + p1)
        else:
            for j in range(n):
                r.append(p2)
        P.append(r)
    return array(P)

with open("U.txt") as f:
    U = f.readlines()
    Uraw = array(U)

with open("A.txt") as f2:
    A = f2.readlines()

U = [link[1:-2] for link in U]
A = [row[:-1] for row in A if row[-1] == "\n"]
A = [row.split(",") for row in A]
A = array([[int(entry) for entry in row] for row in A]).T

remove = [U[i] for i in (1, 45, 68, 149, 322, 381, 470)]
space = ", "
print(f"Removing links: {space.join(remove)}")

for link in remove:
    rem_ind = list(U).index(link)
    U = np.delete(U, rem_ind, 0)
    A = np.delete(A, rem_ind, 0)
    A = np.delete(A, rem_ind, 1)
print(f"Matrix A is of Dimensions {len(A)}x{len(A[0])}")

P = makeP(A)
n = len(A)
p = 0.85
ri_not0 = (1-p)/float(n)
IP = np.eye(n) - P.T
np.sum(IP[:,0])
IP[0] = ones(n)
b = np.zeros(n).reshape(n,1)
b[0] = 1.0


def run_iterations(mtx, n):
    for i in range(n):
        for link in mtx.links:
            link.iterate() 


# the iterative solver
class Link(object):
    def __init__(self, ind):
        self.ind = ind
        self.ri = []
        self.ci = []
        self.page_rank = 0.1

    def iterate(self):
        self.page_rank = p * sum([link.page_rank/len(link.ri) for link in self.ci]) + ri_not0
# the iterative solver
class Matrix(object):
    def __init__(self, inds):
        self.links = []
        self.index_ref = {}
        for ind in inds:
            self.links.append(Link(ind))
        for link in self.links:
            self.index_ref[link.ind] = link

    def initialize(self):
        for link in self.links:
            row, col = A[link.ind], A[:,link.ind]
            for i in range(n):
                if row[i] == 1:
                    link.ri.append(self.index_ref[i])
                if col[i] == 1:
                    link.ci.append(self.index_ref[i])



matrix = Matrix([ind for ind in range(n)])
matrix.initialize()

start = default_timer()
run_iterations(matrix, 50)
stop = default_timer()
print(f'Iterative solution took: {stop - start}s')

m2 = LinearRegression()
start = default_timer()
m2.fit(IP,b)
stop = default_timer()
print(f'SKLearn Linear Regression took: {stop - start}s')

start = default_timer()
u,d,v = svd(IP)
x = dot(v.T, inv(diag(d))).dot(u.T).dot(b)
stop = default_timer()
print(f'Numpy SVD solution took: {stop - start}s')

c = sum([matrix.links[i].page_rank for i in range(n)])
factor = 1/c
pageRanksIter50 = [link.page_rank*factor for link in matrix.links].copy()

#for iterative solution
viewTop20(getTop20(pageRanksIter50, U))
# For Dense eigen-solver SVD
viewTop20(getTop20(x, U))
