# FastIterativePageRank  

"theSolver.py" contains a script that does not depend on any libraries and solves the pagerank problem for a given adjacency matrix A.

The pagerank values become more accurate with more iterations. In the example, solving to 4 significant digits takes around 1/3rd of the time it takes when directly using numpy's linear algebra for a given link graph matrix P, and 1/2 the time sklearn's as Linear Regression which, uses the same BLAS/LAPACK solvers.  

I believe the time complexity for an iteration is O(n), but perhaps with greater links, more iterations would be required to converge. I have not seen evidence for such yet.

## theSolver.py
Takes an link adjacency matrix A, and is currently coded to take a numpy matrix, but this trivial as it only uses the matrix for initialization.

## allCode.py
Contains all the code, datapreprocessing, and functions to display results, view the page links, rank the page links, and compare time splits.  

## Why
The solver is intuitive, and formats the data how the data much closer to how the data would have been gathered in the first place. Its faster and uses less memory.  
