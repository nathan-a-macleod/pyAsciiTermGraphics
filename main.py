from pyAsciiTermGraphics import *

printText("Screen Width: " + str(screenWidth), 2)
printText("Screen Height: " + str(screenHeight), 2)

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
