import sys
import os
import file_to_data
import Automatisation as auto

def isFileInFolder(fileName):
    filesInFolder = os.listdir("instances") # Get a list of all files in the folder
    return fileName in filesInFolder  # Check if the file's name matches any of the files in the folder

def generateAggregateModel(listEdges,listNode,fileName, p) :
    newFileName = fileName+"_0.lp"
    file = open(newFileName, "w") 
    file.write("Minimize\n")
    toOptimize = "obj: "
    for edge in listEdges:
        if edge.medianCost >=0:
            toOptimize += "+ " + str(edge.medianCost) +" " + edge.toString()
        else:
            toOptimize += "- " + str(abs(edge.medianCost)) +" " + edge.toString()
    toOptimize = toOptimize.replace("+","",1)
    file.write(toOptimize + "\n")
    file.write("Subject To\n")
    
    # counterNode = 0
    # counterSource = 0
    # counterDestination = 0
    # equaNode = []
    # equaSource = []
    # equaDestination = []
    # for node in listNode:
    #     if node.type == "Source" :
    #         counterSource+=1
    #         equa = "s_%s: " % counterSource
    #         equa = writeEqua(node,equa,listEdges)
    #         equaSource.append(equa)
    #     elif node.type == "Destination" :
    #         counterDestination+=1
    #         equa = "d_%s: " % counterDestination
    #         equa = writeEqua(node,equa,listEdges)
    #         equaDestination.append(equa)
    #     else :
    #         counterNode+=1
    #         equa = "n_%s: " % counterNode
    #         equa = writeEqua(node,equa,listEdges)
    #         equaNode.append(equa)


    # counter_node = 0
    # counter_source = 0
    # counter_destination = 0
    # equa_node = []
    # equa_source = []
    # equa_destination = []
    
    # for node in listNode:
    #     for i in range(1):
    #         if node.type == "Source":
    #             counter_source += 1
    #             equa = f"s_{counter_source}: "
    #         elif node.type == "Destination":
    #             counter_destination += 1
    #             equa = f"d_{counter_destination}: "
    #         else:
    #             counter_node += 1
    #             equa = f"n_{counter_node}: "
                
    #         equa = writeEqua(node, equa, listEdges)
            
    #         if node.type == "Source":
    #             equa_source.append(equa)
    #         elif node.type == "Destination":
    #             equa_destination.append(equa)
    #         else:
    #             equa_node.append(equa)


    # file.writelines(equa_source)
    # file.writelines(equa_destination)
    # file.writelines(equa_node)
    # file.write("End")
    equaSource, equaDestination, equaNode = generateSubjectTo(listNode, listEdges, p)
    file.writelines(equaSource)
    file.writelines(equaDestination)
    file.writelines(equaNode)
    file.write("End")

def generateModel(listEdges,listNode, fileName, p) :
    newFileName = fileName+"_1.lp"
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
    
#     counterNode = 0
#     counterSource = 0
#     counterDestination = 0
#     equaNode = []
#     equaSource = []
#     equaDestination = []
#     for node in listNode:
#         for i in range(nbrObjet):
#             if node.type == "Source" :
#                 counterSource+=1
#                 equa = "s_%s: " % counterSource
#                 equa = writeEqua(node,equa,listEdges,i)
#                 equaSource.append(equa)
#             elif node.type == "Destination" :
#                 counterDestination+=1
#                 equa = "d_%s: " % counterDestination
#                 equa = writeEqua(node,equa,listEdges,i)
#                 equaDestination.append(equa)
#             else :
#                 counterNode+=1
#                 equa = "n_%s: " % counterNode
#                 equa = writeEqua(node,equa,listEdges,i)
#                 equaNode.append(equa)


    # counter_node = 0
    # counter_source = 0
    # counter_destination = 0
    # equa_node = []
    # equa_source = []
    # equa_destination = []
    
    # for node in listNode:
    #     for i in range(len(listEdges[0].listCost)):
    #         if node.type == "Source":
    #             counter_source += 1
    #             equa = f"s_{counter_source}: "
    #         elif node.type == "Destination":
    #             counter_destination += 1
    #             equa = f"d_{counter_destination}: "
    #         else:
    #             counter_node += 1
    #             equa = f"n_{counter_node}: "
                
    #         equa = writeEqua(node, equa, listEdges, i)
            
    #         if node.type == "Source":
    #             equa_source.append(equa)
    #         elif node.type == "Destination":
    #             equa_destination.append(equa)
    #         else:
    #             equa_node.append(equa)

    # file.writelines(equa_source)
    # file.writelines(equa_destination)
    # file.writelines(equa_node)
    # file.write("End")
    equaSource, equaDestination, equaNode = generateSubjectTo(listNode, listEdges, p)
    file.writelines(equaSource)
    file.writelines(equaDestination)
    file.writelines(equaNode)
    file.write("End")


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











# def generateObjective(listEdges, variant):
#     """
#     Generate the objective function for the LP model.
    
#     Args:
#         listEdges (list): List of edges.
#         variant (int): Variant of the model to generate.
        
#     Returns:
#         str: The objective function string.
#     """
#     print("Generating objective function...")
#     to_optimize = "obj: "
#     nbr_objet = len(listEdges[0].listCost) if variant == 1 else 1
    
#     for edge in listEdges:
#         for i in range(nbr_objet):
#             cost = edge.medianCost if variant == 0 else edge.listCost[i]
#             if cost >= 0:
#                 to_optimize += f"+ {cost} {edge.toString(i)}"
#             else:
#                 to_optimize += f"- {abs(cost)} {edge.toString(i)}"
    
#     print("Objective function:", to_optimize)
#     return to_optimize.replace("+ ", "", 1)  # Adjusted replace function


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
    return equa_source + equa_destination + equa_node


# def generateModel(listEdges, listNode, fileName, variant=0):
#     """
#     Generate LP model file based on the given edges and nodes.
    
#     Args:
#         listEdges (list): List of edges.
#         listNode (list): List of nodes.
#         fileName (str): Base name for the output LP file.
#         variant (int): Variant of the model to generate. 
#                        0 for aggregate model, 1 for regular model.
#     """
#     print("Generating LP model...")
#     new_file_name = f"{fileName}_{variant}.lp"
#     with open(new_file_name, "w") as file:
#         file.write("Minimize\n")
#         file.write(generateObjective(listEdges, variant) + "\n")
#         file.write("Subject To\n")
#         file.writelines(generateSubjectTo(listNode, listEdges, variant))
#         file.write("End")
#     print("LP model generated.")

















def main(instanceName, p):
    if not os.path.exists('./instances/' + instanceName):   # Check if the file exists in the instances folder
        raise ValueError("File name does not exist in instances folder")
    else: 
        listEdges,listNodes = file_to_data.fileToData('./instances/' +instanceName)
        resultFile = instanceName [:-4] 
        print(resultFile)
        p = int(p)  # Convert p to an integer
        if p == 0:
            generateAggregateModel(listEdges,listNodes, resultFile, p)
        elif p ==1:
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

