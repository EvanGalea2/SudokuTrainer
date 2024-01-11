#this class represents a Sudoku object and functionality for it

class sudoku:
	def __init__(self):
		self.objectNum = 0
		self.numGrid = []
		#blankChar = ' '
		print("e")
		for i in range(0, 9):
			row = []
			for j in range (0, 9):
				row.append(self.objectNum)
				self.objectNum += 1
			self.numGrid.append(row)

	#helper method that prints grid to console
	def printGrid(self):
		for i in self.numGrid:
			for j in i:
				print(j)
				#print(self.numGrid[i][j])
		
	#helper method that ensures each number occurs once
	def checkArray(array):
		for i in array:
			if i != 1:
				return false
		return true
	
	def checkRow(self, rowNum):
		print("wip")
	def checkColumn(self, columnNum):
		print("wip")
	#This
	def checkBox(self, rowNum, columnNum):
		#first determine the bounds of the box
		minX = 0
		maxX = 0
		minY = 0
		maxY = 0
		if rowNum < 3:
			minX = 0
		elif rowNum < 5:
			minX = 3
		else:
			minX = 5
		maxX = minX + 2
		
		if columnNum < 3:
			minY = 0
		elif columnNum < 5:
			minY = 3
		else:
			minY = 5
		maxY = minY + 2
		#Now check to ensure
		
		
	
	
	
s = sudoku()
print(s.numGrid)
#s.printGrid()
print("end")
