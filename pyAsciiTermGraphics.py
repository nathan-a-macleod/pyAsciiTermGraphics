import os

# Main classes:
class scene:
	def __init__(self, canvWidth, canvHeight):
		self.canvWidth = canvWidth
		self.canvHeight = canvHeight
		self.canvas = []

	# Create the array for the canvas
	def resetCanvas(self):
		self.canvas = []
		for y in range(0, self.canvHeight):
			currentLine = []
			for x in range(0, self.canvWidth):
				currentLine.append(" ") # The background character

			self.canvas.append(currentLine)

	def printCanvas(self):
		# Actually display (print) the canvas
		for i in range(0, len(self.canvas)):
			for y in range(0, len(self.canvas[i])):
				print(self.canvas[i][y], end="")
					
			print()

	def drawPixel(self, vertX, vertY, char):
		self.canvas[vertY][vertX] = char # "/" is the character representing a vertex

	# Basically just Bresenhams line-drawing algorithm (http://www.roguebasin.com/index.php?title=Bresenham%27s_Line_Algorithm#Python):	
	def drawLine(self, start, end, character):
		"""Bresenham's Line Algorithm
		Produces a list of tuples from start and end
		>>> points1 = get_line((0, 0), (3, 4))
		>>> points2 = get_line((3, 4), (0, 0))
		>>> assert(set(points1) == set(points2))
		>>> print points1
		[(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
		>>> print points2
		[(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
		"""
		# Setup initial conditions
		x1, y1 = start
		x2, y2 = end
		dx = x2 - x1
		dy = y2 - y1
		 
		# Determine how steep the line is
		is_steep = abs(dy) > abs(dx)
		 
		# Rotate line
		if is_steep:
			x1, y1 = y1, x1
			x2, y2 = y2, x2
		 
		# Swap start and end points if necessary and store swap state
		swapped = False
		if x1 > x2:
			x1, x2 = x2, x1
			y1, y2 = y2, y1
			swapped = True
		 
		# Recalculate differentials
		dx = x2 - x1
		dy = y2 - y1
		 
		# Calculate error
		error = int(dx / 2.0)
		ystep = 1 if y1 < y2 else -1
		 
		# Iterate over bounding box generating points between start and end
		y = y1
		points = []
		for x in range(x1, x2 + 1):
			coord = (y, x) if is_steep else (x, y)
			points.append(coord)
			error -= abs(dy)
			if error < 0:
				y += ystep
				error += dx
		 
		# Reverse the list if the coordinates were swapped
		if swapped:
			points.reverse()

		# Actually draw it:
		for i in range(0, len(points)):
			self.drawPixel(points[i][0], points[i][1], character)

# Other things for things like drawing text with ASCII:
def printText(string, textSpacing=1, border=False):
    currentString = ""
    
    if textSpacing == 1:
        textSpacing = ""

    elif textSpacing == 2:
        textSpacing = " "

    elif textSpacing == 3:
        textSpacing = "  "

    if border == False:
        if textSpacing != "":
            for i in range(0, len(string)):
                currentString += string[i].upper() + str(textSpacing)

            print(currentString)

        else:
            print(string)

    elif border == True:
        if textSpacing != "":
            for i in range(0, len(string)):
                currentString += string[i].upper() + str(textSpacing)

            print("+", end="")
            for i in range(0, len(currentString)+1):
                print("-", end="")
            print("+")
            print("| " + currentString + "|")
            print("+", end="")
            for i in range(0, len(currentString)+1):
                print("-", end="")
            print("+")

        else:
            print("+", end="")
            for i in range(0, len(string)+2):
                print("-", end="")
            print("+")
            print("| " + string + " |")
            print("+", end="")
            for i in range(0, len(string)+2):
                print("-", end="")
            print("+")

def clearConsole():
    print("Clearing the screen..")
    if os.name == "nt":
        _ = os.system("cls")

    else:
        _ = os.system("clear")
