#this class represents a Sudoku object and functionality for it

class sudoku:
	numGrid = ''
	def _init_(self):
		self.numGrid = []
		#blankChar = ' '
		objectNum = 0
		print("e")
		for i in range(0, 8):
			row = []
			for j in range (0, 8):
				row.append(objectNum)
				objectNum += 1
			numGrid.append(row)
			print("row")

	#helper method that 
	def printGrid(self):
		for i in range(0, 8):
			for j in range(0, 8):
				print(self.numGrid[i][j])
		
	def checkRow(self, rowNum):
		print("wip")
	def checkColumn(self, columnNum):
		print("wip")
	#This
	def checkBox(self, rowNum, columnNum):
		print("wip")
	
	
	
s = sudoku()
print(s.numGrid)
s.printGrid()
print("end")
