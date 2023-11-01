class ConnectGame:
    def __init__(self, board: str):
        self.lines: list = [line.strip() for line in board.split('\n')]
        self.board: list = [line.split(' ') for line in self.lines]
        self.dimensions: int = len(self.board[0])

    def get_winner(self):
        # No winner if no board
        if self.dimensions == 0:
            return ''
        # In a 1x1 board, the winner is the only piece
        elif self.dimensions == 1:
            return self.board[0][0]
        # Normal case
        else:
            # Check if X won
            if self.check_x_wins(self.board):
                return 'X'
            # Check if O won
            if self.check_o_wins(self.board):
                return 'O'
            # No winner
            return ''

        
    # Check if X has connected from left to right
    def check_x_wins(self, board: list):
        for i in range(self.dimensions):
            # Check for an X in the first column
            if board[i][0] == 'X':
                # Create a visited set and a stack containing cells that are Xs
                visited = set()
                stack = [(i, 0)]
                # Explore the board
                while stack:
                    cell = stack.pop()
                    # Return True if the cell is in the last column
                    if cell[1] == self.dimensions - 1:
                        return True
                    # Visit the cell and add all of its neighbors to the stack
                    if cell not in visited:
                        visited.add(cell)
                        row, col = cell
                        neighbors = [
                            (row - 1, col), # Up left
                            (row - 1, col + 1), # Up right
                            (row + 1, col - 1), # Down left
                            (row + 1, col), # Down right
                            (row, col - 1), # Left
                            (row, col + 1), # Right
                        ]
                        # Extend the stack with the possible neighbors
                        stack.extend([(row, col) for row, col in neighbors if 0 <= row < self.dimensions and 0 <= col < self.dimensions and board[row][col] == 'X'])
        # Return False if no X has connected from left to right (the stack is empty)
        return False
                

    # Check if O has connected from top to bottom
    def check_o_wins(self, board: list):
        for i in range(self.dimensions):
            # Check for an O in the first row
            if board[0][i] == 'O':
                # Create a visited set and a stack containing cells that are Os
                visited = set()
                stack = [(0, i)]
                # Explore the board
                while stack:
                    cell = stack.pop()
                    # Return True if the cell is in the last row
                    if cell[0] == self.dimensions - 1:
                        return True
                    # Visit the cell and add all of its neighbors to the stack
                    if cell not in visited:
                        visited.add(cell)
                        row, col = cell
                        neighbors = [
                            (row - 1, col), # Up left
                            (row - 1, col + 1), # Up right
                            (row + 1, col - 1), # Down left
                            (row + 1, col), # Down right
                            (row, col - 1), # Left
                            (row, col + 1), # Right
                        ]
                        # Extend the stack with the possible neighbors
                        stack.extend([(row, col) for row, col in neighbors if 0 <= row < self.dimensions and 0 <= col < self.dimensions and board[row][col] == 'O'])
        # Return False if no O has connected from left to right (the stack is empty)
        return False