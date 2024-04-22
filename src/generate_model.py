import sys
import os
import file_to_data
import Automatisation as auto

def isFileInFolder(fileName):
    filesInFolder = os.listdir("instances") # Get a list of all files in the folder
    return fileName in filesInFolder  # Check if the file's name matches any of the files in the folder


def writeEqua(node,equa,listEdges,i=None): # i == None when no i parameter is given
    for edge in listEdges:
        edgeName = edge.toString(i)
        if edge.start != edge.end:
            if edge.end == node.id :
                equa += "+ " + edgeName
            elif edge.start == node.id :
                equa += "- " + edgeName
    equa += ">=" + str(node.getDataI(i)) + "\n"
    return equa


def combinedTest(listEdges, p):
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


def generateObjective(listEdges, variant):
    to_optimize = "obj: "
    nbr_objet = len(listEdges[0].listCost) if variant == 1 else 1
    
    for edge in listEdges:
        for i in range(nbr_objet):
            cost = edge.medianCost if variant == 0 else edge.listCost[i]
            if cost >= 0:
                to_optimize += f"+ {cost} {edge.toString(i)}"
            else:
                to_optimize += f"- {abs(cost)} {edge.toString(i)}"
    return to_optimize.replace("+ ", "", 1)  # Adjusted replace function


def generateSubjectTo(listNode, listEdges, variant):
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
    new_file_name = f"{fileName}_{variant}.lp"
    with open(new_file_name, "w") as file:
        file.write("Minimize\n")
        file.write(combinedTest(listEdges, variant))
        #file.write(generateObjective(listEdges, variant) + "\n")
        file.write("Subject To\n")
        file.writelines(generateSubjectTo(listNode, listEdges, variant))
        file.write("End")


def main(instanceName, p):
    if not os.path.exists('./instances/' + instanceName):   # Check if the file exists in the instances folder
        raise ValueError("File name does not exist in instances folder")
    else: 
        listEdges,listNodes = file_to_data.fileToData('./instances/' +instanceName)
        resultFile = instanceName [:-4] 
        print(resultFile)
        p = int(p)  # Convert p to an integer
        if p in [0, 1]:
            generateModel(listEdges,listNodes, resultFile, p)
        else:  # P parameter does not match the expected values
            raise ValueError("Parameter p must be 0 or 1")


if __name__ == '__main__':
    #instanceName = sys.argv[1]  # instance's file's name
    #p = sys.argv[2]  # p parameter
    auto.testTout()
    auto.convertToSol("./")
    auto.showResults()
    #main(instanceName, p)

