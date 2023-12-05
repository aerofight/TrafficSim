class pr: #custom printing class
    def color(text, color): # the function that allows for the print class to take an input color
        if color == "gray":
            colorCode = 90
        elif color == "red":
            colorCode = 91
        elif color == "green":
            colorCode = 92
        elif color == "yellow":
            colorCode = 93
        elif color == "blue":
            colorCode = 94
        elif color == "purple":
            colorCode = 95
        elif color == "cyan":
            colorCode = 96

        print("\033[{}m {}\033[00m" .format(colorCode, text))


array = ['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',
         '*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']

pr.color(" ".join(str(x) for x in array),"green")