class Print:  #custom printing class
    def __init__(self):
        pass

    def color(text, color):  # the function that allows for the print class to take an input color
        color_code = "white"
        if color == "gray":
            color_code = 90
        elif color == "red":
            color_code = 91
        elif color == "green":
            color_code = 92
        elif color == "yellow":
            color_code = 93
        elif color == "blue":
            color_code = 94
        elif color == "purple":
            color_code = 95
        elif color == "cyan":
            color_code = 96

        print("\033[{}m {}\033[00m".format(color_code, text))


array = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*',
         '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']

Print.color(" ".join(str(x) for x in array), "green")
