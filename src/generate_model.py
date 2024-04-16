import sys
import os
import file_to_data

def isFileInFolder(fileName):
    # Get a list of all files in the folder
    filesInFolder = os.listdir("instances")

    # Check if the file's name matches any of the files in the folder
    return fileName in filesInFolder



def main(instanceName, p):
    if not isFileInFolder(instanceName):  # Check if the file exists in the instances folder
        raise ValueError("File name does not exist in instances folder")
    else: 
        p = int(p)  # Convert p to an integer
        if p == 0:
            print("p is 0")
        elif p ==1:
            print("p is 1")
        else:  # P parameter does not match the expected values
            raise ValueError("Parameter p must be 0 or 1")




if __name__ == '__main__':
    instanceName = './instances/' + sys.argv[1]  # instance's file's name
    p = sys.argv[2]  # p parameter
    listEdges,listSources,listDestinations = file_to_data.file_to_data(instanceName)
    #main(instanceName, p)


def generateAggregateModel(listEdges,listSources,listDestinations) :
     file = open("myfile.txt", "w") 
     file.write("Minimize")
     toOptimize = "obj: "
     for edge in listEdges:
         toOptimize.add(to_string(edge.averageCost))

         
