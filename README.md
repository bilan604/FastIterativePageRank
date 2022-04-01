# FastIterativePageRank
theSolver.py : contains the two classes that solve the pagerank problem iteratively

allCode.py : contains all the code, datapreprocessing, and functions to display results, view the page links, rank the page links, and compare time splits

The solver approximates more accurately with higher iterations. For the data, 50 iterations suffices to rank the pages, and SVD with numpy functions is about 50% slower.

Iterations can be paused and stacked.
