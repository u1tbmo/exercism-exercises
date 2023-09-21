def transpose(lines):
    line_list = lines.split('\n')
    num_rows = len(line_list)
    num_cols = max([len(line) for line in line_list])
    # create a placeholder transposed matrix
    matrix = [[' ' for row in range(num_rows)] for col in range(num_cols)]

    for i in range(len(line_list)): # for each line
        for j in range(len(line_list[i])): # for each character in the line
            matrix[j][i] = line_list[i][j] # add the character to the transposed matrix

    # convert the transposed matrix into a string
    output_list = []
    for row in matrix:
        output_list.append(''.join(row))
    
    for index, row in enumerate(output_list):
        output_list[index] = row.rstrip()        

    # super hacky code
    i = 0
    while i < len(output_list):
        if i - 1 < 0:
            line_before = ""
        else:
            line_before = output_list[i-1]
        line_current = output_list[i]
        try:
            line_after = output_list[i+1]
        except IndexError:
            line_after = ""
        # # get the length of the current line, and fix it to be the length of either the line before or after depending on conditions
        # it is the first line, the line will always have the correct length
        if line_before == "" and line_after != "": 
            i += 1
        # the current line is shorter than both the line before and after
        elif len(line_current) < len(line_before) and len(line_current) < len(line_after):
            # if the line before is longer than the line after, add spaces to the end of the current line to match the line after
            if len(line_before) > len(line_after):
                while len(line_current) < len(line_after):
                    line_current += ' '
                i += 1
                output_list[i] = line_current
            # if the line before and line after are the same length, add spaces to the end of the current line to match the lines before and after
            elif len(line_before) == len(line_after):
                while len(line_current) < len(line_before):
                    line_current += ' '
                output_list[i] = line_current
                i += 1
        else:
            i += 1

    output = '\n'.join(output_list)
    return output
