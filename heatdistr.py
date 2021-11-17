import numpy as np

# Physics problem: Tempretature distribution 

def main():
    # Create nXn matrix
    # Set all initial and constant values: Middle and sides

    # Initialize all lattice sites

    N = 20                      # variable for N
    n = int(round(N/2))         # variable for N/2
    r = int(round(N*(1/4)))     # variable for N*0.25
    a = int(round(N*(3/4)))     # variable for N*0.75
    
    # Create NXN-matrix
    heat_matrix = np.zeros((N, N))
    # print(heat_matrix)

    # Set constant temperature at rows 0 and N-1 (for all columns)
    heat_matrix[0] = 100
    heat_matrix[N-1] = 32

    # Set constant temperature at bottom half of columns 0 and N-1
    # (for all rows)
    for row in range(n, N):
        heat_matrix[row][0] = 32
        heat_matrix[row][N-1] = 32
    
    # Set temperature at top half of columns 0 and N-1 to linear increase
    # between 32 and 100

    # Set temperature at matrix center to 212
    # Center is defined fom. row N(1/4) tom. N(3/4) and 
    # column N(1/4) to column N(3/4)
    print('r: ', r, '  a: ', a)
    for row in range(r, a):
        for col in range(r, a):
            heat_matrix[row][col] = 212

    
    print(heat_matrix)





    
    
    


run_main = main()
