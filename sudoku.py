#this class represents a Sudoku object and functionality for it
import csv

class sudoku:
	def __init__(self):
		self.numGrid = []
		self.referenceBoxes = []
		#blankChar = ' '
		print("e")
		for i in range(0, 9):
			row = []
			objectNum = 1
			for j in range (0, 9):
				row.append(objectNum)
				objectNum += 1
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
			if i > 1:
				return false
		return true
	
	def checkRow(self, rowNum):
		checkArray = [0]*9
		for num in self.numGrid[rowNum]:
			checkArray[num] += 1
			if checkArray[num] > 1: #if more than 1 of a number in a row
				return false
		return true
		
	def checkColumn(self, columnNum):
		checkArray = [0]*9
		for row in self.numGrid:
			n = row[columnNum]
			checkArray[n] += 1
			if checkArray[num] > 1: #if more than 1 of a number in a column
				return false
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
		tempArray = [] #this is the array that will be checked
		for i in range(minX, maxX+1):
			for j in range(minY, maxY+1):
				tempArray.append(self.numGrid[i][j])
		
	#this function builds a reference grid so that checking to see
	#if a move satisfies legal requirements for its box is more efficient
	def buildReferenceBox(self):
		self.referenceBoxes = []#reset reference boxes array
		for i in range(0, 3):
			for j in range(0, 3):
				#build a box
				x = i * 3
				y = j * 3
				newBox = []
				for a in range(x, x+3):
					for b in range(y, y+3):
						newBox.append(self.numGrid[a][b])
				self.referenceBoxes.append(newBox)

	def buildGridFromList(self, data):
		rowCounter = 0
		columnCounter = 0
		for num in data:
			self.numGrid[rowCounter][columnCounter] = num
			columnCounter += 1
			if columnCounter > 8:
				columnCounter = 0
				rowCounter += 1
		
		
	def readFromCSV(self, filePath):
		with open(filePath, newline='\n') as csvfile:
    			fileReader = csv.reader(csvfile, delimiter='.', quotechar='|')
    			#name = fileReader.readLine()
    			#data = fileReader.readLine()
    			firstLine = True
    			data = []
    			for row in fileReader:
    				if firstLine:
    					firstLine = False
    				else:
    					for num in row:
    						data.append(num)
					#print(', '.join(row))
			buildGridFromList(self, data)
		
	
	
s = sudoku()
print(s.numGrid)
print("/n")
s.buildReferenceBox()
print(s.referenceBoxes)
s.numGrid[5][5] = 999999
print(s.referenceBoxes)
s.referenceBoxes[3][3] = 77777
print(s.numGrid)
#s.printGrid()
s.readFromCSV("bin/easySudoku.csv")
print("end")
