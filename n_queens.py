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
    n = len(B) # Get the size of the board directly from the list
    
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
            # Place the queen
            B[i][col] = 1
            
            # Recur to place the rest of the queens
            if solve_nq(B, col + 1):
                return True
                
            # If placing queen here doesn't lead to a solution, backtrack (remove it)
            B[i][col] = 0
            
    return False

def print_board(B):
    """Prints the board in a readable grid format."""
    for row in B:
        # Replaces 0s with dots and 1s with 'Q' for a better visual
        formatted_row = ["Q" if x == 1 else "." for x in row]
        print(" ".join(formatted_row))

# --- Main Execution ---
n = 4
board = create_board(n)

if solve_nq(board, 0):
    print(f"Solution for {n}x{n} board:")
    print_board(board)
else:
    print("No solution exists")
