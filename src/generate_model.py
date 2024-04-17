import sys
import os
import file_to_data

def isFileInFolder(fileName):
    # Get a list of all files in the folder
    filesInFolder = os.listdir("instances")

    # Check if the file's name matches any of the files in the folder
    return fileName in filesInFolder

def generateAggregateModel(listEdges,listNode,fileName) :
    newFileName = fileName+".lp"
    file = open(newFileName, "w") 
    file.write("Minimize\n")
    toOptimize = "obj: "
    for edge in listEdges:
        if edge.averageCost >=0:
            toOptimize += "+ " + str(edge.averageCost) +" " + edge.toString()
        else:
            toOptimize += "- " + str(abs(edge.averageCost)) +" " + edge.toString()
    toOptimize = toOptimize.replace("+","",1)
    file.write(toOptimize + "\n")
    file.write("Subject To\n")
    
    counterNode = 0
    counterSource = 0
    counterDestination = 0
    equaNode = []
    equaSource = []
    equaDestination = []
    for node in listNode:
        if node.type == "Source" :
            counterSource+=1
            equa = "s_%s: " % counterSource
            equa = writeEqua(node,equa,listEdges)
            equaSource.append(equa)
        if node.type == "Destination" :
            counterDestination+=1
            equa = "d_%s: " % counterDestination
            equa = writeEqua(node,equa,listEdges)
            equaDestination.append(equa)
        else :
            counterNode+=1
            equa = "n_%s: " % counterNode
            equa = writeEqua(node,equa,listEdges)
            equaNode.append(equa)

    file.writelines(equaSource)
    file.writelines(equaDestination)
    file.writelines(equaNode)
    file.write("End")

def generateModel(listEdges,listNode, fileName) :
    newFileName = fileName+".lp"
    file = open(newFileName, "w")  
    file.write("Minimize\n")
    toOptimize = "obj: "
    nbrObjet = len(listEdges[0].listCost)
    for edge in listEdges:
        for i in range(nbrObjet) :
            if (edge.listCost[i]>=0):
                toOptimize += "+ " + str(edge.listCost[i]) +" " + edge.toString(i)
            else:
                toOptimize += "- " + str(abs(edge.listCost[i])) +" " + edge.toString(i)
    toOptimize = toOptimize.replace("+","",1)
    file.write(toOptimize + "\n")
    file.write("Subject To\n")
    
    counterNode = 0
    counterSource = 0
    counterDestination = 0
    equaNode = []
    equaSource = []
    equaDestination = []
    for node in listNode:
        for i in range(nbrObjet):
            if node.type == "Source" :
                counterSource+=1
                equa = "s_%s: " % counterSource
                equa = writeEqua(node,equa,listEdges,i)
                equaSource.append(equa)
            if node.type == "Destination" :
                counterDestination+=1
                equa = "d_%s: " % counterDestination
                equa = writeEqua(node,equa,listEdges,i)
                equaDestination.append(equa)
            else :
                counterNode+=1
                equa = "n_%s: " % counterNode
                equa = writeEqua(node,equa,listEdges,i)
                equaNode.append(equa)

    file.writelines(equaSource)
    file.writelines(equaDestination)
    file.writelines(equaNode)
    file.write("End")

def writeEqua(node,equa,listEdges,i=None): # i == None when no i parameter is given
    for edge in listEdges:
        edgeName = edge.toString(i)
        if edge.end == node.id :
            equa += "+ " + edgeName
        elif edge.start == node.id :
            equa += "- " + edgeName
    equa += ">=" + str(node.getDataI(i)) + "\n"
    return equa

         


def main(instanceName, p):
    #if not isFileInFolder("./instances/" + instanceName):  # Check if the file exists in the instances folder
    #    raise ValueError("File name does not exist in instances folder")
    if False:
        pass
    else: 
        listEdges,listNodes = file_to_data.fileToData('./instances/' +instanceName)
        resultFile = instanceName [:-4] 
        print(resultFile)
        #for elem in listEdges:
        #    elem.print()
        #for elem in listNodes:
        #    elem.print()
        p = int(p)  # Convert p to an integer
        if p == 0:
            print("p is 0")
            generateAggregateModel(listEdges,listNodes, resultFile)
        elif p ==1:
            print("p is 1")
            generateModel(listEdges,listNodes, resultFile)
        else:  # P parameter does not match the expected values
            raise ValueError("Parameter p must be 0 or 1")




if __name__ == '__main__':
    instanceName = sys.argv[1]  # instance's file's name
    p = sys.argv[2]  # p parameter
    main(instanceName, p)
