"""
N-Queens Backtracking Solver
Finds a valid placement for N queens on an NxN chessboard 
and prints the final solution using a beautiful Unicode grid.
"""

def create_board(n):
    """Generates an empty n x n chessboard filled with 0s."""
    B = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        B.append(row)
    return B

def is_safe(B, row, col):
    """Checks if a queen can be safely placed at B[row][col]."""
    n = len(B)
    
    # Check this row on left side
    for i in range(col):
        if B[row][i] == 1:
            return False
            
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if B[i][j] == 1:
            return False
            
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if B[i][j] == 1:
            return False
            
    return True

def solve_nq(B, col):
    """Uses backtracking to place queens one column at a time."""
    n = len(B)
    
    # Base case: If all queens are placed, return True
    if col >= n:
        return True
        
    for i in range(n):
        if is_safe(B, i, col):
            B[i][col] = 1 # Place the queen
            
            if solve_nq(B, col + 1):
                return True
                
            B[i][col] = 0 # Backtrack: Remove the queen
            
    return False

def print_board(B):
    """Prints the final board using a beautiful Unicode checkerboard pattern."""
    print("\n   N-Queens Board")
    print("  " + "-" * (len(B) * 3))
    
    for row in range(len(B)):
        formatted_row = []
        for col in range(len(B)):
            if B[row][col] == 1:
                formatted_row.append(" ♛ ") # The Queen
            else:
                # Creates a black and white checkerboard pattern
                if (row + col) % 2 == 0:
                    formatted_row.append(" ■ ")
                else:
                    formatted_row.append(" □ ")
        print("  |" + "".join(formatted_row) + "|")
        
    print("  " + "-" * (len(B) * 3) + "\n")

# --- Main Execution ---
n = 8  # Changed to 8 for a full-sized chessboard!
board = create_board(n)

if solve_nq(board, 0):
    print(f"Solution found for an {n}x{n} board:")
    print_board(board)
else:
    print("No solution exists for this board size.")
