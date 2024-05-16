import os
import subprocess
from generate_model import main
import time


directory = ''


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# iterate over files in
# that directory
def showResults():
    for filename in sorted(os.listdir()):
        f = os.path.join(directory, filename)
        if filename.endswith(".sol"):
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                print(bcolors.OKCYAN + bcolors.BOLD +
                    "Filename: ", filename + bcolors.ENDC + " " + lines[5], end="")
                
def convertToSol(directory):
    tempMin = 999999999
    tempsMax = 0
    tempTot = 0
    with open("SolvingTimeResults.txt", "w") as f:
        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".lp"):
                print("Solving LP file:", filename)
                lp_file = os.path.join(directory, filename)
                sol_file = os.path.splitext(lp_file)[0] + ".sol"
                beginTime= time.time()
                solve_lp_file(lp_file, sol_file)
                endTime= time.time()
                if endTime - beginTime < tempMin:
                    tempMin = endTime - beginTime
                if endTime - beginTime > tempsMax:
                    tempsMax = endTime - beginTime
                f.write(f"{sol_file} : {endTime - beginTime} \n")
                tempTot += endTime - beginTime
                print(f"Solution saved to '{sol_file}'.")
        f.write(f"\nTemps min : {tempMin} \n")
        f.write(f"Temps max : {tempsMax} \n")
        f.write(f"Temps moyen : {tempTot/44} \n")
        f.write(f"Temps total : {tempTot} \n")
    f.close()

def solve_lp_file(lp_file, sol_file):
    # Construct the command
    command = ["glpsol", "--lp", lp_file, "-o", sol_file]
    
    # Execute the command
    subprocess.run(command)


def testTout():
    root = "./instances/"
    with open("GenerationTimeResults.txt", "w") as f:
        for path, subdir, files in os.walk(root):
            for name in files:
                beginTime_0= time.time()
                main(name, 0)
                endTime_0= time.time()
                f.write(f"{name}_0 : {endTime_0 - beginTime_0} \n")
                beginTime_1= time.time()
                main(name, 1)
                endTime_1= time.time()
                f.write(f"{name}_1 : {endTime_1 - beginTime_1} \n")
    f.close()


if __name__ == '__main__':
    testTout()
    convertToSol("./")
    showResults()