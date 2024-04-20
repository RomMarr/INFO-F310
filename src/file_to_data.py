from modelClass import Edge
from modelClass import Node


def fileToData(fileName):
    section = splitFileBySections(fileName)
    return sectionToData(section)


def splitFileBySections(fileName):
    sections = []
    currentSection = []

    with open(fileName, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line:  # Non-empty line
                currentSection.append(line)
            else:  # Blank line, start a new section
                if currentSection:
                    sections.append(currentSection)
                    currentSection = []
    # Append the last section
    if currentSection:
        sections.append(currentSection)
    return sections

def sectionToData(sections):
    for section in sections:
        print(section)
    print("______________")
    nbrItems = int(sections[0][0].split()[1]) # get the element after the space (ex : ITEMS 2 -> nbrItems = 2)
    listNodes = createNodes(sections[1])
    listEdges = createEdges(sections[2], nbrItems)
    updateNodeSources(sections[3], listNodes, nbrItems)
    updateNodeDestinations(sections[4], listNodes, nbrItems)
    return listEdges,listNodes

def createNodes(section):
    listNodes = []
    for line in section[2:]:
        splitedLine = line.split()
        listNodes.append(Node(int(splitedLine[0]),float(splitedLine[1]), float(splitedLine[2])))
    return listNodes


def createEdges(section, nbrItems):
    listEdges = []
    for line in section[2:]:
        splitedLine = line.split()
        edge = Edge(int(splitedLine[0]),int(splitedLine[1]), int(splitedLine[2]))
        for i in range(nbrItems):
            edge.add_cost(int(splitedLine[i+3]))
        listEdges.append(edge)
    return listEdges

def updateNodeSources(section, listNodes, nbrItems):
    for line in section[2:]:
        splitedLine = line.split()
        sourceID = int(splitedLine[0])
        for node in listNodes:
            if node.getID() == sourceID: 
                node.changeTypeToSource()
                for i in range(nbrItems):
                    node.add_data(-int(splitedLine[i+1]))


def updateNodeDestinations(section, listNodes, nbrItems):
    for line in section[2:]:
        splitedLine = line.split()
        destinationID = int(splitedLine[0])
        for node in listNodes:
            if node.getID() == destinationID: 
                node.changeTypeToDestination()
                for i in range(nbrItems):
                    node.add_data(int(splitedLine[i +1]))
                