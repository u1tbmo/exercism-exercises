def slices(series, length):
    if not series or series == "":
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    
    
    sliced_series = []
    for i in range(len(series) - length + 1): # subtract length to avoid index out of range, add 1 to include last element
        sliced_series.append(series[i:i+length]) # append slice to sliced_series
    return sliced_series