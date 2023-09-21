def position_valid(row, column):
    # if the row parameter is negative
    if row < 0:
        raise ValueError("row not positive")
    # if the row parameter is not on the defined board
    if row > 7:
        raise ValueError("row not on board")
    # if the column parameter is negative
    if column < 0:
       raise ValueError("column not positive")
    # if the column parameter is not on the defined board
    if column > 7:
        raise ValueError("column not on board")
    
    return True

class Queen:
    # a Queen object has an attribute position, which is a tuple of two integers
    position = (0, 0)

    # initialize the queen's position using the row and column parameters
    def __init__(self, row, column):
        if position_valid(row, column):
            self.position = (row, column)

    def can_attack(self, another_queen):
        # if the queens are in the same square
        if self.position == another_queen.position:
            raise ValueError("Invalid queen position: both queens in the same square")
        
        # if the queens are on the same row
        if self.position[0] == another_queen.position[0]:
            return True

        # if the queens are on the same column
        if self.position[1] == another_queen.position[1]:
            return True

        # if the queens are on the same diagonal
        slope = (self.position[0] - another_queen.position[0]) / (self.position[1] - another_queen.position[1])
        return True if slope == 1 or slope == -1 else False
