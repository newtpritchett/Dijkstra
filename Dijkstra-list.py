def nonNegativeValueMatrix(matrix):
	modiMatrix=matrix
	for i in range(0,len(matrix)):
		for j in range(0,len(matrix[i])):
			modiMatrix[i][j]=int(matrix[i][j])
			if (matrix[i][j] == -1):
				modiMatrix[i][j] = float('inf')
	return modiMatrix


print("importing the CSV library")
import csv
print("opening csv file...")
with open("graph1.csv") as csvFile:
	print("csv filed is opened")
	reader = csv.reader(csvFile)
	nodes = []
	for row in reader:
		nodes.append(row)
	print("csv files read in the nodes:")
	nodes = nonNegativeValueMatrix(nodes)
	print(nodes)
	visitedNodes = []
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

print("done")
