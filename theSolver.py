"""
Make the non-symetric nxn matrix A corresponding to an adjacency matrix
"""
n = len(A)
p = 0.85  # the damping parameter / beta
not0 = (1-p)/float(n)

class Link(object):
    def __init__(self, ind):
        self.ind = ind
        self.ri = []
        self.ci = []
        self.page_rank = 0.1

    def iterate(self):
        self.page_rank = p * sum([link.page_rank/len(link.ri) for link in self.ci]) + not0

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

# run n iterations
def run_iterations(mtx, n):
    for i in range(n):
        for link in mtx.links:
            link.iterate()

matrix = Matrix([ind for ind in range(n)])
matrix.initialize()
run_iterations(matrix, 100)
