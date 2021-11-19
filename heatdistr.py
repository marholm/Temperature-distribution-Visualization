import numpy as np

# Physics problem: Tempretature distribution 

def main():
    # Initialize all lattice sites
    # Set boundary conditions

    N = 10                      # variable for N
    n = int(round(N/2))         # variable for N/2
    r = int(round(N*(0.35)))    # variable for N*0.35
    a = int(round(N*(0.7)))     # variable for N*0.7
    delta = 100
    tolerance = 1
    IMAX = N-1      # burde kanskje være N-2 siden siste er konstant
    JMAX = N-1
    np.set_printoptions(precision=0)
    
    # Create NXN-matrix
    heat_matrix = np.zeros((N, N))
    print('Heat matrix initialized with zeros:')
    print(heat_matrix)
    print('')
    
    
    # Set constant temperature at rows 0 and N-1 (for all columns)
    heat_matrix[0] = 100
    heat_matrix[N-1] = 32

    # Set constant temperature at bottom half of columns 0 and N-1 (for all rows)
    for row in range(n, N):
        heat_matrix[row][0] = 32
        heat_matrix[row][N-1] = 32

    # Set temperature at top half of columns 0 and N-1 to linear increase between 32 and 100 for all rows
    for row in range(1, n):
        X = (100-32)/(n-1)  # trekker fra en fordi den øverste er satt så det er halve matrisen minus en
        heat_matrix[row][0] = int(100-((row-1)*X))
        heat_matrix[row][N-1] = int(100-((row-1)*X))


    # Set temperature at matrix center to 212
    # Center is defined fom. row N(0.35) tom. N(0.7) 
    for row in range(r, a):
        for col in range(r, a):
            heat_matrix[row][col] = 212
    
    print('')
    print('Heat matrix initialized with correct initial values:')
    print('')
    print(heat_matrix)
    print('')

    
    print(heat_matrix)
    
    # TODO: Create main loop for setting values for rest of the matrix
    # so delta is how much the value at a cell has changed from one iteration
    # to the next. Want to stop iteration when values stop changing.
    #while (delta > tolerance):
    Maxiter = 500
    for iteration in range(0, Maxiter):
        #delta = 0               # merk! usikker
        for i in range(1, IMAX):
            for j in range(1, JMAX):
                # Make variable for heat_matrix[i][j] value from last iteration before we update it
                c_old = heat_matrix[i][j]
                print('c_old[',i,'][',j,']=',c_old)
                
                west_neighbour = heat_matrix[IMAX][j] if (i==1) else heat_matrix[i-1][j]
                #print('west_neighbor: ', west_neighbour)
                east_neighbour = heat_matrix[1][j] if (i==IMAX) else heat_matrix[i+1][j]
                #print('east_neighbor: ', east_neighbour)
                north_neighbour = heat_matrix[i][1] if (j==JMAX) else heat_matrix[i][j+1]
                #print('north neighbor:', north_neighbour)
                south_neighbour = heat_matrix[i][JMAX] if (j==1) else heat_matrix[i][j-1]
                #print('south_neighbor: ', south_neighbour)


                # Set NEW value of heat_matrix[i][j]
                heat_matrix[i][j] = (0.25)*(west_neighbour + east_neighbour + 
                            north_neighbour + south_neighbour)

                print('heat_matrix[',i,'][',j,']:',heat_matrix[i][j])
                
    
            #if (abs(c_old - heat_matrix[i][j]) > tolerance):
             #   print('in delta loop')
              #  delta = (c_old - heat_matrix[i][j])
               # print('delta:', delta)
                
    
    print('')
    print('Heat matrix post iterations: ')
    print('')
    print(heat_matrix)
    
    
    
    
    # TODO: Write result to csv-file to be read by paraview






RUN_MAIN = main()
