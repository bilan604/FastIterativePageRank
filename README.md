# FastIterativePageRank  

"theSolver.py" solves the pagerank problem for a given adjacency matrix A. It is a script that does not require any libraries.  

The pagerank values become more accurate with more iterations. For the example data, 50 iterations gives a good approximation of pages, and for comparison, the solution calculaed by SVD (numpy's functions) is about 50% slower. The solver solves the pageranks at around the same speed as SKLearn's LinearRegression (uses blas/lapack). Iterations can be paused and stacked.

## theSolver.py
It contains the two classes that solve the pagerank problem iteratively and the parameters.

## allCode.py
Contains all the code, datapreprocessing, and functions to display results, view the page links, rank the page links, and compare time splits.  

## Why
The solver is intuitive, and stores data how the data tends to be gathered in the first place, with less steps for error in the matrix/notation interpretation O(n^3) linear algebra solution.
