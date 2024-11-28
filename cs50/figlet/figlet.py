import sys
from pyfiglet import Figlet
import random


figlet = Figlet()
fonts = Figlet().getFonts()
def main():
    if len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            if sys.argv[2] in fonts:
                user_input = input('Input: ')
                figlet.setFont(font=sys.argv[2])
                print(sys.argv[2])
                print(figlet.renderText(user_input))
                sys.exit(0)
            else:
                print('Invalid Usage')
                sys.exit(1)
        else:
            print('Invalid Usage')
            sys.exit(1)
    elif len(sys.argv) == 1:
        user_input = input('Input: ')
        n = random.randrange(0, 549, 1)
        figlet.setFont(font=fonts[n])
        print(figlet.renderText(user_input))
        sys.exit(0)
    else:
        print('Invalid Usage')
        sys.exit(1)

main()
