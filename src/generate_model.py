import sys
import os
from statistics import median

class Edge :
    """
    Edge class that contains the data of the edge
    """
    def __init__(self,id,start,end):
        self.id = id
        self.start = start
        self.end = end
        self.listCost = []
        self.medianCost = 0
    
    def getMedianCost(self):
        return self.medianCost
    
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end
    
    def getCost(self,i):
        return self.listCost[i]
    
    def addCost(self,costItem):
        self.listCost.append(costItem)
        self.medianCost = median(self.listCost) # update the median cost
    
    def toString(self,i=None): # i == None when no i parameter is given -> i == nbrItems
        # return the edge's name
        if i == None:
            return "E%s_%s_%s" % (self.id,self.start,self.end)
        else : 
            return "E%s_O%s_%s_%s" % (self.id, i,self.start,self.end)
        
        
class Node : 
    """
    Node class that contains the data of the node
    """
    def __init__(self,id,x,y):
        self.id = id
        self.x = x
        self.y = y
        self.listData = []
        self.totalCapacity = 0
        self.type = "Node"
    
    def getID(self):
        return self.id
    
    def getType(self):
        return self.type
    
    def getData(self,i = None):
        # return the data of the node
        if i == None:
            return self.totalCapacity
        elif self.listData == []:
            return 0
        else:
            return self.listData[i]

    def changeTypeToSource(self):
        self.type = "Source"

    def changeTypeToDestination(self):
        self.type = "Destination"

    def addData (self,data):
        self.listData.append(data) # add the data to the list
        self.totalCapacity += data # update the total capacity
        

def splitFileBySections(fileName):
    """
    Split the file into sections based different parts of the txt file
    """
    sections = []
    currentSection = []
    with open(fileName, 'r') as file: # Open the file in read mode
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
    """
    Transform each section into the data needed to create the model and returns the list of edges and nodes
    """
    nbrItems = int(sections[0][0].split()[1]) # get the element after the space (ex : ITEMS 2 -> nbrItems = 2)
    listNodes = createNodes(sections[1])
    listEdges = createEdges(sections[2], nbrItems)
    updateNodeSources(sections[3], listNodes, nbrItems)
    updateNodeDestinations(sections[4], listNodes, nbrItems)
    return listEdges,listNodes

def createNodes(section):
    """
    Create the nodes with the data from the section
    """
    listNodes = []
    for line in section[2:]: # Skip the first two lines
        splitedLine = line.split()
        listNodes.append(Node(int(splitedLine[0]),float(splitedLine[1]), float(splitedLine[2])))
    return listNodes

def createEdges(section, nbrItems):
    """
    Create the edges with the data from the section
    """
    listEdges = []
    for line in section[2:]: # Skip the first two lines
        splitedLine = line.split()
        edge = Edge(int(splitedLine[0]),int(splitedLine[1]), int(splitedLine[2]))
        for i in range(nbrItems): # Add the cost for each item
            edge.addCost(int(splitedLine[i+3]))
        listEdges.append(edge)
    return listEdges

def updateNodeSources(section, listNodes, nbrItems):
    """
    Update the source nodes with the data from the section
    """
    for line in section[2:]:  # Skip the first two lines
        splitedLine = line.split()
        sourceID = int(splitedLine[0])
        for node in listNodes:
            if node.getID() == sourceID: 
                node.changeTypeToSource()
                for i in range(nbrItems):  # Add the data for each item
                    node.addData(-int(splitedLine[i+1]))

def updateNodeDestinations(section, listNodes, nbrItems):
    """
    Update the destination nodes with the data from the section
    """
    for line in section[2:]:  # Skip the first two lines
        splitedLine = line.split()
        destinationID = int(splitedLine[0])
        for node in listNodes:
            if node.getID() == destinationID: 
                node.changeTypeToDestination()
                for i in range(nbrItems):  # Add the data for each item
                    node.addData(int(splitedLine[i +1]))

def writeEqua(node,equa,listEdges,i=None): # i == None when no i parameter is given
    """
    Write the equation for the given node
    """
    for edge in listEdges:
        edgeName = edge.toString(i)
        if edge.getStart() != edge.getEnd():  # If the edge is not a loop
            if edge.getEnd() == node.getID() :  # If the edge is going to the node
                equa += "+ " + edgeName
            elif edge.getStart() == node.getID() :  # If the edge is coming from the node
                equa += "- " + edgeName
    equa += ">=" + str(node.getData(i)) + "\n"  # Add the data of the node
    return equa

def generateObjective(listEdges, p):
    """
    Generate the part of the model that defines the objective function
    """
    toOptimize = "obj: "
    nbrObjet = len(listEdges[0].listCost) if p == 1 else 1
    for edge in listEdges:
        for i in range(nbrObjet) :
            cost = edge.getMedianCost() if p == 0 else edge.getCost(i)  # Get the cost of the edge
            edgeToString = edge.toString(i) if p == 1 else edge.toString()  # Get the edge's name
            if cost >= 0:
                toOptimize += "+ " + str(cost) +" " + edgeToString 
            else:
                toOptimize += "- " + str(abs(cost)) +" " + edgeToString
    toOptimize = toOptimize.replace("+","",1)  # Remove the first +
    return (toOptimize + "\n")

def generateSubjectTo(listNode, listEdges, p):
    """
    Generate the part of the model that defines the constraints and return the list of equations
    """
    counterNode = 0 
    counterSource = 0
    counterDestination = 0
    equaNode = []  # List of equations for the nodes
    equaSource = []  # List of equations for the sources
    equaDestination = []  # List of equations for the destinations
    for node in listNode:
        for i in range(len(listEdges[0].listCost) if p == 1 else 1):  # Loop for each item
            if node.getType() == "Source":
                counterSource += 1
                equa = f"s_{counterSource}: "
            elif node.getType() == "Destination":
                counterDestination += 1
                equa = f"d_{counterDestination}: "
            else:
                counterNode += 1
                equa = f"n_{counterNode}: "  
            
            # Write the equation for the node
            equa = writeEqua(node, equa, listEdges, i) if p == 1 else writeEqua(node, equa, listEdges)

            if node.getType() == "Source":
                equaSource.append(equa)  # Add the equation to the list of source equations
            elif node.getType() == "Destination":
                equaDestination.append(equa)  # Add the equation to the list of destination equations
            else:
                equaNode.append(equa)  # Add the equation to the list of node equations
    return equaSource+ equaDestination +equaNode

def generateModel(listEdges, listNode, fileName, p=0):
    """ 
    Generate the model into the .lp file
    """
    newFileName = f"{fileName}_{p}.lp"  # Name of the .lp file
    with open(newFileName, "w") as file:
        file.write("Minimize\n")
        file.write(generateObjective(listEdges, p))
        file.write("Subject To\n")
        file.writelines(generateSubjectTo(listNode, listEdges, p))
        file.write("End")


def main(instanceName, p):
    """
    Control the flow of the program, with the good parameters raise an error if the parameters are not correct
    """
    fileName = './instances/' +instanceName  # add the path to the file
    if not os.path.exists(fileName):   # Check if the file exists in the instances folder
        raise ValueError("File name does not exist in instances folder")
    else: 
        sections = splitFileBySections(fileName)
        listEdges,listNodes = sectionToData(sections)
        resultFile = instanceName [:-4] 
        p = int(p)  # Convert p to an integer
        if p in [0, 1]:
            generateModel(listEdges,listNodes, resultFile, p)
        else:  # P parameter does not match the expected values
            raise ValueError("Parameter p must be 0 or 1")


if __name__ == '__main__':
    instanceName = sys.argv[1]  # instance's file's name
    p = sys.argv[2]  # p parameter
    main(instanceName, p)
