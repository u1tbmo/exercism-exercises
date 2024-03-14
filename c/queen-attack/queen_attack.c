#include "queen_attack.h"

attack_status_t can_attack(position_t queen_1, position_t queen_2)
{
    // Check if a queen is in an invalid position
    if (!is_valid_position(queen_1) || !is_valid_position(queen_2) || (queen_1.row == queen_2.row && queen_1.column == queen_2.column))
    {
        return INVALID_POSITION;
    }

    int slope = 0;
    int row_diff = queen_2.row - queen_1.row;
    int col_diff = queen_2.column - queen_1.column;
    if (col_diff != 0)
    {
        slope = row_diff / col_diff;
    }
    else
    {
        // Since col_diff is 0, the queens can attack.
        return CAN_ATTACK;
    }

    // If the queens are on the same row, column, or diagonal, then they can attack.
    if (row_diff == 0 || col_diff == 0 || slope == 1 || slope == -1)
    {
        return CAN_ATTACK;
    }
    else
    {
        return CAN_NOT_ATTACK;
    }
}

bool is_valid_position(position_t queen)
{
    // A queen's position is invalid if it is not in the range 0 to 7.
    // The data type uint8_t is unsigned and thus always starts at 0, we no longer have to check for that condition.
    return queen.row <= 7 && queen.column <= 7;
}