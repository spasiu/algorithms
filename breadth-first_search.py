"""A toy program demonstrating breadth-first search in a directional graph. Part of my quest to think algorithmically."""

def dequeue(q):
	"""takes an array representing a queue and removes the first element of that array and returns it"""
	dequeued = q[0]
	del(q[0])
	return dequeued

def check(target, node):
	"""takes a number representing the targeted node and a number representing the current node and 
		compares them, returning True if they are equivalent and false otherwise"""
	print "checking %d" %node
	if target == node: 
		return True
	else: 
		return False

def children(node, graph):
	"""takes a number represnting a node and a graph and returns the children of the node in an array"""
	childs = graph[node]
	if len(childs) == 0:
		print "node %d is a dead end" %node
	return childs

def search(q, graph, target):
	"""takes an array representing a queue, a directed graph and a number representing a targeted node. 
		Follows connections between nodes until it locates the targeted nodes or exhausts the graph. 
		Returns a string explanation of the results"""
	while True:
		print "queue: ", q
		if len(q) == 0:
			return "target node not reachable"
		node = dequeue(q)
		if check(target, node): 
			return "located node %d" %node
		else: 
			for child in children(node, graph):
				q.append(child)

def initialize(start, target, graph):
	"""takes a number representing a starting point on a graph, a number representing the targeted node, 
		and a graph. Then calls the "initialize" function passing it the target and graph and a list 
		containing the start point, representing the starting queue. Displays results of graph search as 
		returned by "search" function"""
	queue = [start]
	print search(queue, graph, target)

SAMPLE_GRAPH = {1:[2,3,4], 2:[5,6,7,8], 3:[9], 4:[10], 5:[9], 6:[3,4], 7:[2,11], 8:[9], 9:[1,2,3,4], 10:[6], 11:[]}

if __name__ == "__main__":
	import json
	gprint = json.dumps(SAMPLE_GRAPH)
	print "This is the starting graph: %s" %gprint
	print "enter target node:"
	target = int(raw_input())
	print "enter starting point:"
	start = int(raw_input())
	initialize(start, target, SAMPLE_GRAPH)