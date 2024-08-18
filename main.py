color = {
    'black'  : 30,
    'white'  : 37,
    'gray'   : 90,
    'red'    : 91,
    'green'  : 92,
    'yellow' : 93,
    'blue'   : 94,
    'purple' : 95,
    'cyan'   : 96
}

def print_color(text, color_code, bold = False, new_line = False):
    bold_code = ''
    if bold:
        bold_code = '1;'

    if new_line:
        print("\033[{}{}m{}\033[0m".format(bold_code, color_code, text))

    else:
        print("\033[{}{}m{}\033[0m".format(bold_code, color_code, text), end='')

print_color('gray', color['gray'], True)
print_color('white', color['white'], True)
print_color('black', color['black'], True)
print_color('red', color['red'], True)
print_color('green', color['green'], True)
print_color('yellow', color['yellow'], True)
print_color('blue', color['blue'], True)
print_color('purple', color['purple'], True)
print_color('cyan', color['cyan'], True, True)

print_color('gray', color['gray'])
print_color('white', color['white'])
print_color('black', color['black'])
print_color('red', color['red'])
print_color('green', color['green'])
print_color('yellow', color['yellow'])
print_color('blue', color['blue'])
print_color('purple', color['purple'])
print_color('cyan', color['cyan'])