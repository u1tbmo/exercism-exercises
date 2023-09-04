actions = ['jump', 'close your eyes', 'double blink', 'wink']

def commands(binary_str):
    commands = []
    for index, bit in enumerate(binary_str[1:]):
        if bit == '1':
            commands.append(actions[index])
    return commands[::-1] if binary_str[0] == '0' else commands
