# FastIterativePageRank  

The pagerank values become more accurate with more iterations. For the data used, 50 iterations suffices to rank the pages, and for comparison the solution calculaed by SVD (numpy's functions) is about 50% slower. The solver solves the pageranks at around the same speed as SKLearn's LinearRegression (uses blas/lapack). Iterations can be paused and stacked.

## theSolver.py
Without using outside libraries, this script solves the pagerank problem for an adjacency matrix A which is not given. It contains the two classes that solve the pagerank problem iteratively and the parameters.

## allCode.py
Contains all the code, datapreprocessing, and functions to display results, view the page links, rank the page links, and compare time splits.  
