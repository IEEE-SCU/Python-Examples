#Author:D4Vinci
#print with colors in any platform with colorama and if it not working because u on windows then use method 2 to print with powershell ;) 

#Console Colors
G = '\033[92m' #green
Y = '\033[93m' #yellow
B = '\033[94m' #blue
R = '\033[91m' #red
W = '\033[0m'  #white

def colored_print(text,color):

    #Check if we are running this on windows platform
    is_windows = sys.platform.startswith('win')

    if is_windows:
        try:
            import colorama
            method = 1
        except:
            method = 2

        if method == 1:
            from colorama import init, AnsiToWin32
            init(wrap=False)
            stream = AnsiToWin32(sys.stderr).stream
            print >>stream, color + text

        elif method == 2:
            if color == '\033[92m':
                color = "G"

            if color == '\033[93m':
                color = "Y"

            if color == '\033[94m':
                color = "B"

            if color == '\033[91m':
                color = "R"

            if color == '\033[0m':
                color = "W"

            def powershell_print(text,color):
                color = color.upper()
                powershell_colors = {"B":"Blue","G":"Green","R":"Red","W":"White","Y":"Yellow"}
                import subprocess,sys
                subprocess.Popen('powershell -command "write-host {{"{0}"}} -foreground "{1}" " '.format(text,powershell_colors[color]) , stdout=sys.stdout)

            powershell_print(text,color)
    else:
        print color+text+'\033[0m'
