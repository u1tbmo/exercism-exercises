#include "robot_simulator.h"

robot_status_t robot_create(robot_direction_t direction, int x, int y)
{
    robot_status_t new_robot;
    new_robot.direction = direction;
    new_robot.position.x = x;
    new_robot.position.y = y;

    return new_robot;
}
void robot_move(robot_status_t *robot, const char *commands)
{
    for (int i = 0, l = strlen(commands); i < l; i++)
    {
        switch (commands[i])
        {
        case 'L':
            robot->direction = (robot->direction == 0) ? DIRECTION_WEST : robot->direction - 1;

            break;
        case 'R':
            robot->direction = (robot->direction + 1) % DIRECTION_MAX;

            break;
        case 'A':
            switch (robot->direction)
            {
            case DIRECTION_NORTH:
                robot->position.y++;
                break;
            case DIRECTION_EAST:
                robot->position.x++;
                break;
            case DIRECTION_SOUTH:
                robot->position.y--;
                break;
            case DIRECTION_WEST:
                robot->position.x--;
                break;
            default:
                break;
            }
            break;

        default:
            break;
        }
    }
}
