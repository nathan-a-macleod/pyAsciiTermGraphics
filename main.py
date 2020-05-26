import pyAsciiTermGraphics as patg

mainScene = patg.scene(60, 30)
mainScene.resetCanvas()
mainScene.drawLine((55, 1), (1, 23), "=")
mainScene.drawPixel(55, 1, "#")
mainScene.drawPixel(1, 23, "#")
mainScene.printCanvas()
