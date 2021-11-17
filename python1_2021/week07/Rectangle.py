class Rectangle:
    ' class that represents rectangles'
    def setSize(self, x, y):
	'constructor set width and length'
	self.width = x
	self.length = y
    def getSize(self):
	return self.width, self.length
    def perimeter(self):
	' returns perimeter of the rectangle '
	return 2*(self.width + self.length) 
    def area(self):
	' returns area of a rectangle'
	return self.width * self.length 