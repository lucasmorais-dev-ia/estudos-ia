import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    chosen = random.choice(fonts)
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
    chosen = sys.argv[2]
else:
    sys.exit("Invalid usage")
text = input("Input: ")
figlet.setFont(font=chosen)
print("Output:")
print(figlet.renderText(text))