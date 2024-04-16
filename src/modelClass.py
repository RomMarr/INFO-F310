class Edge :
    
    def __init__(self,id,start,end):
        self.id = id
        self.start = start
        self.end = end
        self.listCost = []
        self.averageCost = 0
    
    def add_cost(self,costItem):
        self.listCost.append(costItem)
        self.updateAverageCost()
    
    def updateAverageCost(self):
        sumCost = 0
        for cost in self.listCost:
            sumCost+=cost
        self.averageCost = sumCost/ len(self.listCost)

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
