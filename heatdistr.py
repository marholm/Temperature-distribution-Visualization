import numpy as np
from numpy.lib.shape_base import column_stack
import pandas as pd
import sys
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(precision=0)

# Physics problem: Temperature distribution

def main():
    # Define necessary variables for setting initial conditions
    N = 20                      # variable for N
    n = int(round(N/2))         # variable for N/2
    r = int(round(N*(0.35)))    # variable for N*0.35
    a = int(round(N*(0.7)))     # variable for N*0.7
    
    # ------------- Set boundary conditions ------------------
    
    # Create NXN-matrix
    heat_matrix = np.zeros((N, N))
    
    # Set the unknown values to a reasonable value between 32 and 212
    for i in range(N):
        for j in range(N):
            heat_matrix[i][j] = 90 
    
    # Set constant temperature at rows 0 and N-1 (for all columns)
    heat_matrix[0] = 100
    heat_matrix[N-1] = 32

    # Set constant temperature at bottom half of columns 0 and N-1 (for all rows)
    for i in range(n, N):
        heat_matrix[i][0] = heat_matrix[i][N-1] = 32 

    # Set temperature at top half of columns 0 and N-1 to linear increase between 32 and 100 for all rows
    for i in range(1, n):
        X = (100-32)/(n-1)  # trekker fra en fordi den øverste er satt så det er halve matrisen minus en
        heat_matrix[i][0] = int(100-((i-1)*X))
        heat_matrix[i][N-1] = int(100-((i-1)*X))

    # Set temperature at matrix center to 212 (center is defined fom. row N(0.35) tom. N(0.7))
    for i in range(r, a):
        for j in range(r, a):
            heat_matrix[i][j] = 212
    
   
    # ----------- Create main loop for laplace iterations ---------------


    # Define necessary variables for iterations
    delta = 1          # delta is how much the value at a cell has changed in one iteration
                       # when values stop changing - the solution has stabilised and we can stop 
    tolerance = 0.5    # the lower tolerance, the more accuracy
    IMAX = N-1         
    JMAX = N-1
    max_iterations = 50000      
    iterations = 1
    
    
    # Main loop
    while (delta > tolerance and iterations < max_iterations):
        delta = 0             
        for i in range(1, IMAX):
            for j in range(1, JMAX):
                # cell value of iteration n
                c_current = heat_matrix[i][j]
                
                west_neighbour = heat_matrix[IMAX][j] if (i==1) else heat_matrix[i-1][j]
                east_neighbour = heat_matrix[1][j] if (i==IMAX) else heat_matrix[i+1][j]
                north_neighbour = heat_matrix[i][1] if (j==JMAX) else heat_matrix[i][j+1]
                south_neighbour = heat_matrix[i][JMAX] if (j==1) else heat_matrix[i][j-1]

                # cell value of iteration n+1
                c_new = (0.25)*(west_neighbour + east_neighbour + 
                            north_neighbour + south_neighbour)
                
                # Want to check that the solution has not stabilised yet by checking the change/difference
                if (abs(c_current - c_new) > tolerance):
                    # the delta variable stores the difference 
                    delta += abs(c_current - c_new)

                # Update cell value
                heat_matrix[i][j] = c_new

        iterations += 1
    
    # ----------- Convert the resulting data to (x, y, value)-format si it can be read by paraview ----------------
    C = np.zeros((N*N, 3))
    R = list(np.arange(0,(N*N)))
    for i in range(N):       
        for j in range(N):   
            r = R.pop(0)
            C[r, 0] = i         
            C[r, 1] = j
            C[r, 2] = heat_matrix[i][j]

    # ----------------- Write the result to a csv-file --------------------
    # 1. convert numpy array to pandas dataframe
    data_frame = pd.DataFrame(C)

    # 2. save dataframe as csv file
    data_frame.to_csv('heat_data.csv', index=False) 
    

RUN_MAIN = main()
