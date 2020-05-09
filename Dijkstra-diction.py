def nonNegativeValueDict(nodeDict):
	modDict = {}
	for nodeName, edgeList in nodeDict.items():
		print(nodeDict[nodeName])
	return nodeDict

print("importing the CSV library")
import csv
print("opening csv file...")
with open("graph1.csv") as csvFile:
	print("csv filed is opened")
	reader = csv.reader(csvFile)
	nodes = {}
	for i, row in enumerate(reader):
		print(row)
		nodes[str(i)] = row
	#print("csv files read in the nodes: ")
	#print(nodes)
	#print(nodes["0"])
	nodes = nonNegativeValueDict(nodes)
	#print(nodes)
'''	visitedNodes = []
	i=0										#modify this to allow user to specify starting node
	loopcount = 0
	while(len(visitedNodes)) < len(nodes):
		print("\nState:\nIteration: " + str(loopcount) + ", i-value: " +str(i))
		loopcount+=1
		currentNode = nodes[i]
		nodes[i] = []
		print("Current Node: ")
		print(currentNode)
		visitedNodes.append(currentNode)
		print("Visted Nodes: ")
		print(visitedNodes)
		print("Unvisited Nodes: ")
		print(nodes)
		currentNode[i] = float('inf')
		print("Modified Current Node to avoid back-tracking: " + str(currentNode))
		temp = i
		print(str(temp))
		i = currentNode.index(min(currentNode))
		print("Next node index: " + str(i) + " Distance: " + str(min(currentNode)))
		currentNode[temp] = 0
'''
print("done")
