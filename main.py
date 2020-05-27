import pyAsciiTermGraphics as patg

mainScene = patg.scene(60, 30)
mainScene.resetCanvas()
mainScene.drawLine((13, 17), (47, 28), "=")
mainScene.drawPixel(13, 17, "#")
mainScene.drawPixel(47, 28, "#")
mainScene.printCanvas()
