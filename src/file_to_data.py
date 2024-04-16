from modelClass import Edge
from modelClass import Source
from modelClass import Destination


def file_to_data(fileName):
    with open(fileName,'r') as file:
        listEdges = []
        listSources = []
        listDestinations = []
        
        line = newline(file)
        numberItems = int(line[1])
        file.readline()
        
        line = newline(file)
        numberNodes = int(line[1])
        file.readline()
        for _ in range(numberNodes+1):
            file.readline()
        
        line = newline(file)
        numberEdges = int(line[1])
        file.readline()
        for _ in range(numberEdges):
            line = newline(file)
            start = int(line[1])
            end = int(line[2])
            newEdge = Edge(int(line[0]),start,end)
            for i in range(numberItems):
                newEdge.add_cost(int(line[i+3]))
            listEdges.append(newEdge)
        file.readline()

        line = newline(file)
        numberSources = int(line[1])
        file.readline()
        for _ in range (numberSources):
            line = newline(file)
            newSource = Source(line[0])
            for i in range(numberItems):
                newSource.add_capacity(int(line[i+1]))
            listSources.append(newSource)
        file.readline()

        line = newline(file)
        numberDestinations = int(line[1])
        file.readline()
        for _ in range (numberDestinations):
            line = newline(file)
            newDestination = Destination(line[0])
            for i in range(numberItems):
                newDestination.add_Demands(int(line[i+1]))
            listDestinations.append(newDestination)
    return listEdges,listSources,listDestinations


        





def newline(file):
    return file.readline().split(' ')

