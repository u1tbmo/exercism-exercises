def transform(legacy_data):
    transformed_data = {}

    key_list = list(legacy_data.keys())
    value_list = legacy_data.values()

    for index, sublist in enumerate(value_list):
        for letter in sublist:
            letter = letter.lower()
            transformed_data.update({letter: key_list[index]})

    return transformed_data
    