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