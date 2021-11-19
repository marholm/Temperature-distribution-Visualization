import numpy as np
import csv
import pandas as pd

# Physics problem: Tempretature distribution 

def main():
    # Initialize all lattice sites
    # Set boundary conditions

    N = 10                      # variable for N
    n = int(round(N/2))         # variable for N/2
    r = int(round(N*(0.35)))    # variable for N*0.35
    a = int(round(N*(0.7)))     # variable for N*0.7
    
    np.set_printoptions(precision=0)
    
    # Create NXN-matrix
    heat_matrix = np.zeros((N, N))
    # print('Heat matrix initialized with zeros:')
    # print(heat_matrix)
    # print('')

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

    # Set temperature at matrix center to 212, center is defined fom. row N(0.35) tom. N(0.7) 
    for i in range(r, a):
        for j in range(r, a):
            heat_matrix[i][j] = 212
    
    print('')
    print('Heat matrix initialized with correct initial values:')
    print('')
    print(heat_matrix)
    print('')
    
    
    # TODO: Create main loop for setting values for rest of the matrix
    # so delta is how much the value at a cell has changed from one iteration
    # to the next. Want to stop iteration when values stop changing.

    delta = 1
    tolerance = 0.5    # the lower tolerance, the more accuracy
    IMAX = N-1         
    JMAX = N-1
    max_iterations = 500
    iterations = 1

    # main loop
    while (delta > tolerance and iterations < max_iterations):
        # reset delta before next iteration of the matrix
        delta = 0             
        for i in range(1, IMAX):
            for j in range(1, JMAX):
                # cell value of iteration n
                c_current = heat_matrix[i][j]
                # print('c_current[',i,'][',j,']=',c_current)
                
                west_neighbour = heat_matrix[IMAX][j] if (i==1) else heat_matrix[i-1][j]
                #print('west_neighbor: ', west_neighbour)
                east_neighbour = heat_matrix[1][j] if (i==IMAX) else heat_matrix[i+1][j]
                #print('east_neighbor: ', east_neighbour)
                north_neighbour = heat_matrix[i][1] if (j==JMAX) else heat_matrix[i][j+1]
                #print('north neighbor:', north_neighbour)
                south_neighbour = heat_matrix[i][JMAX] if (j==1) else heat_matrix[i][j-1]
                #print('south_neighbor: ', south_neighbour)

                # cell value of iteration n+1
                c_new = (0.25)*(west_neighbour + east_neighbour + 
                            north_neighbour + south_neighbour)

                # print('c_new[',i,'][',j,']:',c_new)
                
                # Only want to record the change if its bigger than 1/2 degree
                if (abs(c_current - c_new) > tolerance):
                    # the delta variable stores the difference 
                    delta += (c_current - c_new)
                    heat_matrix[i][j] = c_new

        iterations += 1
                
    
    print('')
    print('Heat matrix post iterations: ')
    print('')
    print(heat_matrix)
    
    
    # TODO: Write result to csv-file to be read by paraview
    # convert numpy array to pandas dataframe
    data_frame = pd.DataFrame(heat_matrix)

    # save dataframe as csv file
    data_frame.to_csv('heat_data.csv')
    


RUN_MAIN = main()
