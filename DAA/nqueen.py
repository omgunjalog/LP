# Function to check if it is safe to place the queen at board[row][col]
def isSafe(mat, row, col):
    n = len(mat)
    for i in range(row):
        if mat[i][col]:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if mat[i][j]:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
        if mat[i][j]:
            return False
    return True

# Recursive function to place queens
def placeQueens(row, mat):
    n = len(mat)
    if row == n:
        return True
    for i in range(n):
        if isSafe(mat, row, i):
            mat[row][i] = 1
            if placeQueens(row + 1, mat):
                return True
            mat[row][i] = 0
    return False

# Function to solve N-Queens and print board
def nQueen(n):
    mat = [[0 for _ in range(n)] for _ in range(n)]
    if placeQueens(0, mat):
        print("\nSolved N-Queens board:")
        for row in mat:
            print(" ".join('Q' if cell else '.' for cell in row))
    else:
        print("No solution exists.")

# Main execution
if __name__ == "__main__":
    n = int(input("Enter the size of the board (n): "))
    nQueen(n)

