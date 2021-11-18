import numpy as np

# Physics problem: Tempretature distribution 

def main():
    # Initialize all lattice sites
    # Set boundary conditions

    N = 20                      # variable for N
    n = int(round(N/2))         # variable for N/2
    r = int(round(N*(0.35)))    # variable for N*0.35
    a = int(round(N*(0.7)))     # variable for N*0.7
    
    # Create NXN-matrix
    heat_matrix = np.zeros((N, N))
    # print(heat_matrix)

    # Set constant temperature at rows 0 and N-1 (for all columns)
    heat_matrix[0] = 100
    heat_matrix[N-1] = 32

    # Set constant temperature at bottom half of columns 0 and N-1 (for all rows)
    for row in range(n, N):
        heat_matrix[row][0] = 32
        heat_matrix[row][N-1] = 32

    # Set temperature at top half of columns 0 and N-1 to linear increase between 32 and 100 for all rows
    for row in range(1, n):
        X = (100-32)/(n-1)  # trekker fra en fordi den øverste er sat så det er halve matrisen minus en
        heat_matrix[row][0] = int(100-((row-1)*X))
        heat_matrix[row][N-1] = int(100-((row-1)*X))


    # Set temperature at matrix center to 212
    # Center is defined fom. row N(0.35) tom. N(0.7) 
    for row in range(r, a):
        for col in range(r, a):
            heat_matrix[row][col] = 212
    
    print('The initialized matrix:')
    print('')
    print(heat_matrix)

    # TODO: Create main loop for setting values for rest of the matrix

    delta = 50
    tolerance = 5
    IMAX = N-2
    JMAX = N-2

    while delta > tolerance:
        for i in range(1, IMAX):
            for j in range(1, JMAX):
                
                west_neighbour = heat_matrix[IMAX][j] if (i==1) else heat_matrix[i-1][j]
                east_neighbour = heat_matrix[1][j] if (i==IMAX) else heat_matrix[i+1][j]
                north_neighbour = heat_matrix[i][1] if (j==JMAX) else heat_matrix[i][j+1]
                south_neighbour = heat_matrix[i][JMAX] if (j==1) else heat_matrix[i][j-1]
                
                c_old = heat_matrix[i][j]
                c_new = (1/4)*(west_neighbour + east_neighbour + 
                            north_neighbour + south_neighbour)

                if (abs(c_old - c_new) > tolerance):
                    delta = (c_old - c_new)






RUN_MAIN = main()
