NUM_CHAR_ARRAY = [
    [" _ ", "| |", "|_|", "   "],  # 0
    ["   ", "  |", "  |", "   "],  # 1
    [" _ ", " _|", "|_ ", "   "],  # 2
    [" _ ", " _|", " _|", "   "],  # 3
    ["   ", "|_|", "  |", "   "],  # 4
    [" _ ", "|_ ", " _|", "   "],  # 5
    [" _ ", "|_ ", "|_|", "   "],  # 6
    [" _ ", "  |", "  |", "   "],  # 7
    [" _ ", "|_|", "|_|", "   "],  # 8
    [" _ ", "|_|", " _|", "   "],  # 9
]


def convert_grid(grid_to_convert: list[str]) -> str:
    for i in range(len(NUM_CHAR_ARRAY)):
        if grid_to_convert == NUM_CHAR_ARRAY[i]:
            return str(i)
    return "?"


def convert_to_4_rows(input_grid: list[str], qty: int) -> tuple:
    row1 = input_grid[0]
    row2 = input_grid[1]
    row3 = input_grid[2]
    row4 = input_grid[3]

    i = 0
    for row in input_grid[4:]:
        # loop again to 0 when i > 3
        if i > 3:
            i = 0

        # check the current index of the row to know what row to add the string to
        match i:
            case 0:
                row1 += row
            case 1:
                row2 += row
            case 2:
                row3 += row
            case 3:
                row4 += row
        i += 1

    qty = len(row1) // 3

    return ([row1, row2, row3, row4], qty)


def convert(input_grid: list[str]) -> str:
    # when the rows aren't multiples of 4
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    # when the columns aren't multiples of 3
    for row in input_grid:
        if len(row) % 3 != 0:
            raise ValueError(
                "Number of input columns is not a multiple of three")

    # calculate the number of numbers in the input
    qty = len(input_grid[0]) // 3
    og_qty = qty  # used to check if the qty has changed

    # if rows > 4, convert to 4 rows
    if len(input_grid) > 4:
        input_grid, qty = convert_to_4_rows(input_grid, qty)

    # convert every string in the list to a list of strings with 3 characters
    str_list = []
    for row in input_grid:
        n = 0
        for _ in range(qty):
            str_list.append(row[n:n+3])
            n += 3

    output = ""

    # from str_list, create a list of 3x4 grids
    grid = []
    for i in range(qty):
        grid.append(str_list[i])
        grid.append(str_list[i+qty])
        grid.append(str_list[i+qty*2])
        grid.append(str_list[i+qty*3])

        # convert each 3x4 grid into a number
        output += convert_grid(grid)

        # remove everything from grid
        grid.clear()

    # initialize output list
    output_list = []

    # if the length of the output is greater than the qty of numbers that means there were multiple lines of numbers
    # if so, for every qty, add a comma to the output, except if the comma is at the end
    if qty > og_qty:
        # split the output into qty parts
        for i in range(og_qty):
            output_list.append(
                # e.g. output[0:3], output[3:6], output[6:9]
                output[i*og_qty:i*og_qty+og_qty]
            )

        # create a list of commas
        result = [","] * (og_qty * 2 - 1)

        # interleaving the output_list and the result list
        result[0::2] = output_list

        # join the output list
        output = "".join(result)

    return output
