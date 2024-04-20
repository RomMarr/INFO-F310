from statistics import median
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
        self.medianCost = median(self.listCost)
        
    
    def toString(self,i=None): # i == None when no i parameter is given -> i == nbrItems
        if i == None:
            return "E%s_%s_%s" % (self.id,self.start,self.end)
        else : 
            return "E%s_O%s_%s_%s" % (self.id, i,self.start,self.end)

    def print(self):
        print(f"ID: {self.id}, Start: {self.start}, End: {self.end}, ListCost: {self.listCost}, AverageCost: {self.averageCost}")

        
class Node : 
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
    
    def print(self):
        print(f"{self.type} - ID: {self.id}, X: {self.x}, Y: {self.y}, ListData: {self.listData}")

    def getDataI(self,i = None):
        if i == None:
            return self.getTotalCapacity()
        elif self.listData == []:
            return 0
        else:
            return self.listData[i]
