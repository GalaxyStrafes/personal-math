#transform a vector with a linear transformation described by the matrix
#use square matrices only and please use same number of dimensions for vectors and matrices
#ik i suck but i need a way to learn and to probably help people to see that they don't suck xD

def transform(vector, matrix): #linearly transforms a ND vector with a given matrix of N dimensions (square matrix)
    """1D array of 3 nums for vector, and an array of 3 arrays with 3 elements for matrix"""
    """ARRAY OF ARRAYS IN THIS CASE MEANS ARRAY OF COLLUMNS OF A MATRIX"""
    #vector = np.array(vector)
    #matrix = np.array(matrix)
    try:
        out = []
        for i in range(len(vector)):
            outpush = 0
            for j in range(len(vector)):
                outpush += vector[j] * matrix[j][i]
            out.append(outpush)
        print('used vector: ' + str(vector))
        print('used matrix: ' + str(matrix) + '  and got:')
        return(out)
    except TypeError:
        return(['wrong entry type, entry must be array of collumns of a matrix (as arrays), returns None', None])
    except:
        return(['something else went wrong, returning 0', 0])



#composition of ND matrices
#use square matrices only

def findComposition(m2, m1): #returns composition matrix
    """Given an input of 2 2d array square matrices, returns a 2d array composition"""
    try:
        out = []
        print('multiplying matrix m1 by matrix m2 with matrices', m2 ,'and', m1)
        for i in range(len(m1)):
            print('transform output logs:')
            out.append(transform(m1[i], m2))
        print("if this function didn't output properly, keep in mind that matrix m2 goes first and matrix m1 goes second since that is how you find a composition of 2 linear transformations described by those (you read from right to left)")
        return(out)
    except ImportError:
        return(['Incorrectly imported module, fix that or contact developer, returns None', None])
    except TypeError:
        return(['Matrices are imported as arrays of arrays, where one array contains arrays of columns of matrices, incorrect input, returns none', None])
    except:
        return(['Something went wrong, returning 0', 0])