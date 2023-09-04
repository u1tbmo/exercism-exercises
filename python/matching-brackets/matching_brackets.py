def is_paired(input_string):
    # create a storage list
    storage = []
    # loop through the string
    for char in input_string:
        # if the current character is an opening bracket
        if char == '(' or char == '[' or char == '{':
            # add it to the storage list
            storage.append(char)
        # otherwise if the current character is a closing bracket
        elif char == ')' or char == ']' or char == '}':
            # check if there are no opening brackets in the storage list
            if len(storage) == 0:
                # if there are no opening brackets in the storage list, then it is not a valid pairing
                return False
            # check if the current character is a closing bracket and the last opening bracket in the storage list is not its matching opening bracket
            elif char == ')' and storage[-1] != '(':
                # if the current character is a closing bracket and the last opening bracket in the storage list is not its matching opening bracket, then it is not a valid pairing
                return False
            # check if the current character is a closing bracket and the last opening bracket in the storage list is not its matching opening bracket
            elif char == ']' and storage[-1] != '[':
                # if the current character is a closing bracket and the last opening bracket in the storage list is not its matching opening bracket, then it is not a valid pairing
                return False
            # check if the current character is a closing bracket and the last opening bracket in the storage list is not its matching opening bracket
            elif char == '}' and storage[-1] != '{':
                # if the current character is a closing bracket and the last opening bracket in the storage list is not its matching opening bracket, then it is not a valid pairing
                return False
            # if all of the above checks failed, then the current character is a closing bracket and the last opening bracket in the storage list is its matching opening bracket
            else:
                # remove the last opening bracket from the storage list
                storage.pop()
    # check if there are any opening brackets left in the storage list
    return len(storage) == 0
