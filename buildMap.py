from random import randint
from SimpleGraphics import *
from time import *

def drawMap(wide,tall):
	map = list()
	for y in range(tall):
		map.append([])
		for x in range(wide):
			map[y].append(0)
	return map
		
def drawPath(map,x,y,z):
	if((x>=0 and x<len(map[0])) and (y>=0 and y<len(map))):
		if(map[y][x]==0):
			xDir = [-1,0,1,0]
			yDir = [0,-1,0,1]
			filled = 0
			for dir in range(4):
				x1=x+xDir[dir]
				y1=y+yDir[dir]
				if((x1>=0 and x1<len(map[0])) and (y1>=0 and y1<len(map))):
					if(map[y1][x1]>0):
						filled+=1
			if(filled<=1):
				map[y][x]=1
				z+=1
				for dir in range(5):
					curDir = randint(0,3)
					x1=x+xDir[curDir]
					y1=y+yDir[curDir]
					map = drawPath(map,x1,y1,z)
	return map
	
def makeMaze(wide,tall,startX,startY):
	map = drawMap(wide-2,tall-2)
	map = drawPath(map,startX-1,startY-1,1)
	for y in range(tall-2):
		map[y].insert(0,0)
		map[y].insert(wide-1,0)
	map.insert(0,[0]*wide)
	map.insert(tall-1,[0]*wide)
	path = findLongestPath(map,startX,startY)
	map[startY][startX]=5
	end = path[0]
	map[end[0]][end[0]] = 6
	return map
	
def findLongestPath(map,x,y):
	longPath=[]
	if(map[y][x]==1):
		map[y][x]=2
		xDir=[0,-1,0,1]
		yDir=[-1,0,1,0]
		for dir in range(4):
			xNew = x+xDir[dir]
			yNew = y+yDir[dir]
			newPath = findLongestPath(map,xNew,yNew)
			if(len(newPath)>len(longPath)):
				longPath=newPath
		longPath.append((x,y))
		map[y][x]=1
	return longPath
	
def multilevelMaze(levels,wide,tall,initX,initY):
	maze = []
	startX = initX
	startY = initY	
	for level in range(levels):
		map = makeMaze(wide,tall,startX,startY)
		maze.append(map)
		for y in range(tall):
			for x in range(wide):
				if(map[y][x]==6):
					startX=x
					startY=y
	game = {"maze":maze, "player":{"x":initX,"y":initY},"currentLvl":0}
	return maze

def multiToString(maze):
	outStr = ""
	for i in maze:
		for y in i:
			for x in y:
				if(x==0):
					outStr=outStr+"##"
				if(x==1):
					outStr=outStr+"  "
				if(x==5):
					outStr=outStr+"OO"
				if(x==6):
					outStr=outStr+"XX"
			outStr=outStr+"\n"
		outStr=outStr+"\n"	
	return outStr
	
def drawMaze(maze,pixelSize):
	setOutline("seashell2")
	for y in range(len(maze)):
		for x in range(len(maze[0])):
			if(maze[y][x]==1):
				setFill("seashell")
			if(maze[y][x]==0):
				setFill("seashell4")
			if(maze[y][x]==5):
				setFill("spring green")
				start = [x,y]
			if(maze[y][x]==6):
				setFill("tomato")
				end = [x,y]
			rect((x*pixelSize),(y*pixelSize),pixelSize,pixelSize)
	
def moveLeft(maze):
	if(maze[player][x]>=1):
		if(maze[maze][maze[currentLvl]][maze[player[y]][maze[player[x]-1]]==1 or maze[maze][maze[currentLvl]][maze[player[y]][maze[player[x]-1]]==5):
			maze[player][x]--
			sleep(1)
			return maze
		elif(maze[maze][maze[currentLvl]][maze[player[y]][maze[player[x]-1]]==6):
			maze[player][x]--
			maze[currentLvl]++
	return maze

def moveUp(maze):
	if(maze[player][y]>=1):
		if(maze[maze][maze[currentLvl]][maze[player[y]-1][maze[player[x]]]==1 or maze[maze][maze[currentLvl]][maze[player[y]-1][maze[player[x]]]==5):
			maze[player][y]--
			sleep(1)
			return maze
		elif(maze[maze][maze[currentLvl]][maze[player[y]-1][maze[player[x]]]==6):
			maze[player][y]--
			maze[currentLvl]++
	return maze

def moveRight(maze):
	if(maze[player][x]<len(maze[maze])-1):
		if(maze[maze][maze[currentLvl]][maze[player[y]][maze[player[x]+1]]==1 or maze[maze][maze[currentLvl]][maze[player[y]][maze[player[x]+1]]==1):
			maze[player][x]++
			sleep(1)
			return maze
		elif(maze[maze][maze[currentLvl]][maze[player[y]][maze[player[x]+1]]==6):
			maze[player][x]++
			maze[currentLvl]++
	return maze
	
def moveDown(maze):
	if(maze[player][x]<len(maze[maze])-1):
		if(maze[maze][maze[currentLvl]][maze[player[y]+1][maze[player[x]]]==1 or maze[maze][maze[currentLvl]][maze[player[y]+1][maze[player[x]]]==5):
			maze[player][y]++
			sleep(1)
			return maze
		elif(maze[maze][maze[currentLvl]][maze[player[y]+1][maze[player[x]]]==6):
			maze[player][y]++
			maze[currentLvl]++
	return maze

	
	
