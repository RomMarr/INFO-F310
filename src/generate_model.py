import sys
import os
import Automatisation as auto
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
    
    def add_cost(self,costItem):
        self.listCost.append(costItem)
        self.updateMedianCost()
    
    def updateMedianCost(self):
        sumCost = 0
        for cost in self.listCost:
            sumCost+=cost
        self.medianCost = median(self.listCost)
        
    
    def toString(self,i=None): # i == None when no i parameter is given -> i == nbrItems
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
        self.type = "Node"

    def changeTypeToSource(self):
        self.type = "Source"

    def changeTypeToDestination(self):
        self.type = "Destination"

    def getID(self):
        return self.id

    def add_data (self,data):
        self.listData.append(data)
    
    def getTotalCapacity(self):
        totalCapacity = 0
        for cap in self.listData:
            totalCapacity+=cap
        return totalCapacity

    def getDataI(self,i = None):
        if i == None:
            return self.getTotalCapacity()
        elif self.listData == []:
            return 0
        else:
            return self.listData[i]
        

def splitFileBySections(fileName):
    """
    Split the file into sections based different parts of the txt file
    """
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
    """
    Transform each section into the data needed to create the model
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
    for line in section[2:]:
        splitedLine = line.split()
        listNodes.append(Node(int(splitedLine[0]),float(splitedLine[1]), float(splitedLine[2])))
    return listNodes

def createEdges(section, nbrItems):
    """
    Create the edges with the data from the section
    """
    listEdges = []
    for line in section[2:]:
        splitedLine = line.split()
        edge = Edge(int(splitedLine[0]),int(splitedLine[1]), int(splitedLine[2]))
        for i in range(nbrItems):
            edge.add_cost(int(splitedLine[i+3]))
        listEdges.append(edge)
    return listEdges

def updateNodeSources(section, listNodes, nbrItems):
    """
    Update the source nodes with the data from the section
    """
    for line in section[2:]:
        splitedLine = line.split()
        sourceID = int(splitedLine[0])
        for node in listNodes:
            if node.getID() == sourceID: 
                node.changeTypeToSource()
                for i in range(nbrItems):
                    node.add_data(-int(splitedLine[i+1]))

def updateNodeDestinations(section, listNodes, nbrItems):
    """
    Update the destination nodes with the data from the section
    """
    for line in section[2:]:
        splitedLine = line.split()
        destinationID = int(splitedLine[0])
        for node in listNodes:
            if node.getID() == destinationID: 
                node.changeTypeToDestination()
                for i in range(nbrItems):
                    node.add_data(int(splitedLine[i +1]))

def isFileInFolder(fileName):
    # Check if the file exists in the instances folder
    filesInFolder = os.listdir("instances") # Get a list of all files in the folder
    return fileName in filesInFolder  # Check if the file's name matches any of the files in the folder

def writeEqua(node,equa,listEdges,i=None): # i == None when no i parameter is given
    """
    Write the equation for the given node
    """
    for edge in listEdges:
        edgeName = edge.toString(i)
        if edge.start != edge.end:  # If the edge is not a loop
            if edge.end == node.id :
                equa += "+ " + edgeName
            elif edge.start == node.id :
                equa += "- " + edgeName
    equa += ">=" + str(node.getDataI(i)) + "\n"
    return equa

def generateObjective(listEdges, p):
    """
    Generate the part of the model that defines the objective function
    """
    toOptimize = "obj: "
    nbrObjet = len(listEdges[0].listCost) if p == 1 else 1
    for edge in listEdges:
        for i in range(nbrObjet) :
            cost = edge.medianCost if p == 0 else edge.listCost[i]
            edgeToString = edge.toString(i) if p == 1 else edge.toString()
            if cost >= 0:
                toOptimize += "+ " + str(cost) +" " + edgeToString
            else:
                toOptimize += "- " + str(abs(cost)) +" " + edgeToString
    toOptimize = toOptimize.replace("+","",1)
    return (toOptimize + "\n")

def generateSubjectTo(listNode, listEdges, variant):
    """
    Generate the part of the model that defines the constraints
    """
    counter_node = 0
    counter_source = 0
    counter_destination = 0
    equa_node = []
    equa_source = []
    equa_destination = []
    for node in listNode:
        for i in range(len(listEdges[0].listCost) if variant == 1 else 1):
            if node.type == "Source":
                counter_source += 1
                equa = f"s_{counter_source}: "
            elif node.type == "Destination":
                counter_destination += 1
                equa = f"d_{counter_destination}: "
            else:
                counter_node += 1
                equa = f"n_{counter_node}: "  
            equa = writeEqua(node, equa, listEdges, i) if variant == 1 else writeEqua(node, equa, listEdges)
            if node.type == "Source":
                equa_source.append(equa)
            elif node.type == "Destination":
                equa_destination.append(equa)
            else:
                equa_node.append(equa)
    return equa_source+ equa_destination +equa_node

def generateModel(listEdges, listNode, fileName, variant=0):
    """ 
    Generate the model into the .lp file
    """
    new_file_name = f"{fileName}_{variant}.lp"
    with open(new_file_name, "w") as file:
        file.write("Minimize\n")
        file.write(generateObjective(listEdges, variant))
        file.write("Subject To\n")
        file.writelines(generateSubjectTo(listNode, listEdges, variant))
        file.write("End")


def main(instanceName, p):
    """
    Control the flow of the program, with the good parameters raise an error if the parameters are not correct
    """
    fileName = './instances/' +instanceName
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
    #auto.testTout()
    #auto.convertToSol("./")
    #auto.showResults()
    main(instanceName, p)
