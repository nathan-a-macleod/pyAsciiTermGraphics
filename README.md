# pyAsciiTermGraphics
This is a small library for creating ASCII graphics in the terminal with Python!

## Usage & Installation:
Once Python 3 is installed on your system, you need to clone the repository.
Then in the repositories folder, create a new file - in the file put the following lines of code (From main.py):
`
from pyAsciiTermGraphics import *

printText("Normal Text Outlined", 1, True)
printText("Normal Text", 1, False) # (1 and False are default values so you don't have to put them in in this case - I just included them for demonstration purposes)
print()
printText("Medium Text Outlined", 2, True)
printText("Medium Text", 2, False)
print()
printText("Large Text Outlined", 3, True)
printText("Large Text", 3, False)

mainScene = scene(30, 15)
mainScene.resetCanvas()
mainScene.drawLine((3, 0), (25, 14), "=")
mainScene.drawPixel(29, 14, "#")
mainScene.printCanvas()

printText("Do you like the program?", 3, False)
print()

input("Press enter to clear the screen: ")
clearConsole()
`
If you get no errors, you should be good to go - just have a look at the main.py file to work out how to use the library - it should have enough information.

If you get any errors, bugs, or have any ideas for new features, please feel free to either create a Github issue or contribute to this project - just fork it, clone it, change it, and send a pull request!
