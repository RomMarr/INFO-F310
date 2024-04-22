class Source :

    def __init__(self,id):
        self.id = id
        self.listCapacity = []
        self.totalCapacity = 0
    
    def add_capacity (self,capacity):
        self.listCapacity.append(capacity)
        self.updateTotalCapacity()


    def updateTotalCapacity(self):
        self.totalCapacity = 0
        for capacity in self.listCapacity:
            self.totalCapacity+= capacity

class Destination :

    def __init__(self,id):
        self.id = id
        self.listDemands = []
        self.totalDemands = 0
    
    def add_Demands (self,Demand):
        self.listDemands.append(Demand)
        self.updateTotalDemands()

    def updateTotalDemands(self):
        self.totalDemands = 0
        for Demand in self.listDemands:
            self.totalDemands+= Demand


# def generateAggregateModel(listEdges,listNode,fileName, p) :
#     newFileName = fileName+"_0.lp"
#     file = open(newFileName, "w") 
#     file.write("Minimize\n")
    
    
#     toOptimize = "obj: "
#     for edge in listEdges:
#         if edge.medianCost >=0:
#             toOptimize += "+ " + str(edge.medianCost) +" " + edge.toString()
#         else:
#             toOptimize += "- " + str(abs(edge.medianCost)) +" " + edge.toString()
#     toOptimize = toOptimize.replace("+","",1)
#     file.write(toOptimize + "\n")
#     #file.write(generateObjective(listEdges, p) + "\n")


#     file.write("Subject To\n")
#     equaSource, equaDestination, equaNode = generateSubjectTo(listNode, listEdges, p)

#     file.writelines(equaSource)
#     file.writelines(equaDestination)
#     file.writelines(equaNode)
#     file.write("End")

# def generateModel(listEdges,listNode, fileName, p) :
#     newFileName = fileName+"_1.lp"
#     file = open(newFileName, "w")  
#     file.write("Minimize\n")

    
    # toOptimize = "obj: "
    # nbrObjet = len(listEdges[0].listCost)
    # for edge in listEdges:
    #     for i in range(nbrObjet) :
    #         if (edge.listCost[i]>=0):
    #             toOptimize += "+ " + str(edge.listCost[i]) +" " + edge.toString(i)
    #         else:
    #             toOptimize += "- " + str(abs(edge.listCost[i])) +" " + edge.toString(i)
    # toOptimize = toOptimize.replace("+","",1)
    # file.write(toOptimize + "\n")

    # file.write("Subject To\n")
    
    # equaSource, equaDestination, equaNode = generateSubjectTo(listNode, listEdges, p)

    # file.writelines(equaSource)
    # file.writelines(equaDestination)
    # file.writelines(equaNode)
    # file.write("End")


    # def test0(listEdges):
#     toOptimize = "obj: "
#     for edge in listEdges:

#         if edge.medianCost >=0:
#             toOptimize += "+ " + str(edge.medianCost) +" " + edge.toString()
#         else:
#             toOptimize += "- " + str(abs(edge.medianCost)) +" " + edge.toString()

#     toOptimize = toOptimize.replace("+","",1)
#     return (toOptimize + "\n")


# def test1(listEdges):
#     toOptimize = "obj: "
#     nbrObjet = len(listEdges[0].listCost)
#     for edge in listEdges:
#         for i in range(nbrObjet) :

#             if (edge.listCost[i]>=0):
#                 toOptimize += "+ " + str(edge.listCost[i]) +" " + edge.toString(i)
#             else:
#                 toOptimize += "- " + str(abs(edge.listCost[i])) +" " + edge.toString(i)

#     toOptimize = toOptimize.replace("+","",1)
#     return (toOptimize + "\n")

# def generateObjective(listEdges, variant):
#     to_optimize = "obj: "
#     nbr_objet = len(listEdges[0].listCost) if variant == 1 else 1
    
#     for edge in listEdges:
#         for i in range(nbr_objet):
#             cost = edge.medianCost if variant == 0 else edge.listCost[i]
#             if cost >= 0:
#                 to_optimize += f"+ {cost} {edge.toString(i)}"
#             else:
#                 to_optimize += f"- {abs(cost)} {edge.toString(i)}"
#     return to_optimize.replace("+ ", "", 1)  # Adjusted replace function