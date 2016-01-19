import sys,getopt
import operator
from collections import OrderedDict
import heapq
import time

def dfs(source,destList,graph,startTime):
	print "inside dfs"
	frontier = [[source]]
	frontierList=[source]
	explored = set()
	while True:

		if(len(frontier)==0):
			return None,0
		print "frontier"
		print frontier
		print "frontierList"
		print frontierList
		node = frontier.pop()
		print "node"
		print node
		vertex=node[-1]
		for z in range(0,len(destList)):
			if vertex == destList[z]:
				return vertex,startTime+len(node)-1
		explored.add(vertex)

		print "explored"
		print explored
		for child in graph.get(vertex, []):
			print "child"
			print child
			if child not in explored and child not in frontierList:
				
				new_path = list(node)
				new_path.append(child)
				frontier.append(new_path)
				frontierList.append(child)

def bfs(source,destList,graph,startTime):
	print "inside bfs1"
	frontier = [[source]]
	frontierList=[source]
	explored = set()
	for z in range(0,len(destList)):
		if source == destList[z]:
			return source,startTime
	while True:

		if(len(frontier)==0):
			return None,0
		print "frontier"
		print frontier
		print "frontierList"
		print frontierList
		node = frontier.pop(0)
		print "node"
		print node
		vertex=node[-1]
		explored.add(vertex)

		print "explored"
		print explored
		for child in graph.get(vertex, []):
			print "child"
			print child
			if child not in explored and child not in frontierList:
				for z in range(0,len(destList)):
					if child == destList[z]:
						return child,startTime+len(node)
				new_path = list(node)
				new_path.append(child)
				frontier.append(new_path)
				frontierList.append(child)
						


				
		
			
					

			
				







	
	
def ucs(source,destList,middleNodesList,noOfPipes,graphucs,startTime,graphList):
	print "inside ucs"
	def flatten(L):       
		while len(L) > 0:
			yield L[0]
			L = L[1]

	q = [(0, source, ())]
	frontierList=[source]
	
	explored = set() 
	     
	
	
	while True:
		if(len(q)==0):
			print "node not reachable"
			return (None,0)
		
		(cost, v1, path) = heapq.heappop(q)

		print "frontierList"
		print frontierList
		flag1=0
		print "cost v1 path"
		print cost, v1,path
		
		for z in range(0,len(destList)):
			if v1 == destList[z]:
				print cost
				print list(flatten(path))[::-1] + [v1]
				return v1,(cost+startTime)%24
		if v1 not in explored:
			explored.add(v1)
		node = (v1, path)
		print "path"
		print node
		try:
			for (v2, cost2) in graphucs[v1].iteritems():
				print "v2"
				print v2
				print explored
				for y in range(0,noOfPipes):
						#print graphList[y][0]
						if(v1==graphList[y].split(" ")[0] and v2==graphList[y].split(" ")[1]):
							print "v1,v2"
							print v1,v2
							offList=graphList[y].split(" ")[4:]
							print "offlist"
							print offList
				print "totalCost"
				print cost 
				flag2=0
				for w in range(0,len(offList)):
					temp=[]
					print "offtime is present"
					print offList[w].split("-")[0]
					if((cost+startTime)%24>=int(offList[w].split("-")[0])%24 and (startTime+cost)%24<=int(offList[w].split("-")[1])%24):
						print "applying offlist.Disfunctional nodes present"
						print int(offList[w].split("-")[0])%24
						#temp=[v1,v2]
						
						disfunctionalNode=v2
						print disfunctionalNode
						print "disfunctionalNode present"
						flag2=1
						break
				if(flag2):
					continue
				else:
					if v2 not in explored and v2 not in frontierList:
						print "not explored"
						#print graphList
						heapq.heappush(q, ((cost + int(cost2)), v2, node))
						frontierList.append(v2)
							
						
					elif( v2 in frontierList):

						print "node in frontier"
						for a in range(0,len(q)):
						 	if(q[a][1]==v2 and ((cost + int(cost2)))<q[a][0]):
						 		print "time to pop the unnecessary node"
						 	 	q[a]=q[-1]
						 	 	q.pop()
						 	 	heapq.heappush(q, ((cost + int(cost2)), v2, node))


			

			q = sorted(q, key=lambda tup: (tup[0],tup[1]))
			print q
			print "--------------------------------"
		except:
			print "its not a closed circuit"






start_time = time.time()
filewrite = open('output.txt', 'w+')
argv=sys.argv[1:]
try:
	opts, args = getopt.getopt(argv,"i")
except getopt.GetoptError:
	print 'usage is: python waterFlow.py -i <inputfile>'

print args
f=open(args[0], 'r') 
try:
	noOfTrials = int(f.readline().strip())
	for i in range(0,noOfTrials):
		graphList=[]
		algoType=f.readline().strip()
		source=f.readline().strip()
		destination=f.readline().strip()
		middleNodes=f.readline().strip()
		noOfPipes=int(f.readline().strip())
		for j in range(0,noOfPipes):
			graphList.append(f.readline().strip())
		startTime=int(f.readline().strip())
		f.readline().strip()
		destList=destination.split(" ")
		middleNodesList=middleNodes.split(" ")
		graph = {}
		for k in range(0,noOfPipes):
			key=graphList[k].split(" ")[0]
			value=graphList[k].split(" ")[1]
			if not graph.has_key(key):
				graph[key] = [value]
			else:
				graph[key].append(value)

		for l in graph.keys():
			graph[l]=sorted(graph[l])	
		

		print graph

		if(algoType=="BFS"):
			vertex,cost=bfs(source,destList,graph,startTime)
			if(vertex==None):
				solution="None"
			else:
				solution=vertex+" "+str(cost)
			print "solution bfs"
			print vertex,cost
			filewrite.write(solution+"\n")
			

		elif(algoType=="DFS"):
			graphdfs={}
			for l in graph.keys():
				graphdfs[l]=sorted(graph[l],reverse=True)
			print graphdfs
			vertexdfs,costdfs=dfs(source,destList,graphdfs,startTime)
			if(vertexdfs==None):
				solutiondfs="None"
			else:
				solutiondfs=vertexdfs+" "+str(costdfs)
			print "solution dfs"
			print vertexdfs,costdfs
			filewrite.write(solutiondfs+"\n")


		elif(algoType=="UCS"):
			graphucs={}
			for k in range(0,noOfPipes):
				temp={}
				key=graphList[k].split(" ")[0]
				value=graphList[k].split(" ")[1]
				weight=graphList[k].split(" ")[2]
				temp[value]=weight
				if not graphucs.has_key(key):
					graphucs[key] = temp
				else:
					graphucs[key].update(temp)
			print "hi"
			print graphucs
			#for l in graphucs.keys():
				#graphucs[l]=sorted(graphucs[l])	
			#print graphucs
			

			vertexucs,costucs=ucs(source,destList,middleNodesList,noOfPipes,graphucs,startTime,graphList)

			if(vertexucs==None):
				solutionucs="None"
			else:
				solutionucs=vertexucs+" "+str(costucs)
			print "solution ucs"
			print vertexucs,costucs
			filewrite.write(solutionucs+"\n")
except:
	filewrite.write("None")
filewrite.close()
print("--- %s seconds ---" % (time.time() - start_time))




