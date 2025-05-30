# Given an n x n matrix and a number x, find the position of x in the matrix if it is present in it. Otherwise, print “Not Found”. In the given matrix, every row and column is sorted in increasing order. The designed algorithm should have linear time complexity. 

# Example: 

# Input: mat[4][4] = { {10, 20, 30, 40},
#                       {15, 25, 35, 45},
#                       {27, 29, 37, 48},
#                       {32, 33, 39, 50}};
#               x = 29
# Output: Found at (2, 1)
# Explanation: Element at (2,1) is 29

# Input : mat[4][4] = { {10, 20, 30, 40},
#                       {15, 25, 35, 45},
#                       {27, 29, 37, 48},
#                       {32, 33, 39, 50}};
#               x = 100
# Output : Element not found
# Explanation: Element 100 is not found


def searchMatrix(mat, m, n, key):
    i,j = 0,n-1

    while 0<=i<m and 0<=j<n:
        if mat[i][j] == key:
            return (i, j)
        
        elif mat[i][j] > key:
            j -= 1
        else:
            i += 1
    
    return -1

if __name__ == '__main__':
    mat = [[10, 20, 30, 40], [15, 25, 35, 45],[27, 29, 37, 48],[32, 33, 39, 50]]
    print(searchMatrix(mat, 4, 4, 29))