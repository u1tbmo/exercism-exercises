math_operations = ['plus','minus','multiplied','divided']

def answer(question):
    question = question.replace('What is', '').replace('?', '').replace('by ','').strip()
    question_as_list = question.split()
    if not question:
        raise ValueError('syntax error')
    for word in question_as_list:
        if word == "Who" or word == "squared" or word == "cubed":
            raise ValueError('unknown operation')
    
    for index, word in enumerate(question_as_list):
        if word in math_operations:
            question_as_list[index] = {
               'plus': '+',
               'minus': '-',
               'multiplied': '*',
               'divided': '/'
            }[word]

    # makes sure to evaluate the first operation first
    question_as_list.insert(0, '(')
    question_as_list.insert(4, ')')

    try:
        return eval(' '.join(question_as_list))
    except:
        raise ValueError('syntax error')