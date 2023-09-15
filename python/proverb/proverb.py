def proverb(*args, **kwargs):
    args_len = len(args)
    args_list = list(args)
    qualifier = kwargs.get("qualifier", None) # get the qualifier from the kwargs dict, if it exists
    line = ""
    
    proverb = []

    for item in args_list:
        try:
            next_item = args_list[args_list.index(item) + 1] # gets the item next to the current item
        except IndexError:
            next_item = None

        if next_item:
            line = f"For want of a {item} the {next_item} was lost."
        elif qualifier and next_item is None:
            line = f"And all for the want of a {qualifier} {args_list[0]}."
        elif qualifier is None and next_item is None:
            line = f"And all for the want of a {args_list[0]}."
        
        proverb.append(line)

    return proverb