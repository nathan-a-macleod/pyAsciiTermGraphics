import pyAsciiTermGraphics as patg

patg.printText("Normal Text Outlined", 1, True)
patg.printText("Normal Text", 1, False) # (1 and False are default values so you don't have to put them in in this case)
print()
patg.printText("Medium Text Outlined", 2, True)
patg.printText("Medium Text", 2, False)
print()
patg.printText("Large Text Outlined", 3, True)
patg.printText("Large Text", 3, False)

mainScene = patg.scene(60, 30)
mainScene.resetCanvas()
mainScene.drawLine((13, 17), (47, 28), "=")
mainScene.drawPixel(13, 17, "#")
mainScene.drawPixel(47, 28, "#")
mainScene.printCanvas()
