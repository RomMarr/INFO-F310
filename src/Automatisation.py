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
    """
    Convert all LP files in the specified directory to solution files using glpsol.
    
    Args:
        directory (str): The path to the directory containing LP files.
    """
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".lp"):
            lp_file = os.path.join(directory, filename)
            sol_file = os.path.splitext(lp_file)[0] + ".sol"
            solve_lp_file(lp_file, sol_file)
            print(f"Solution saved to '{sol_file}'.")

def solve_lp_file(lp_file, sol_file):
    """
    Solve an LP file using glpsol and save the solution to a file.
    
    Args:
        lp_file (str): The path to the LP file.
        sol_file (str): The path to save the solution file.
    """
    # Construct the command
    command = ["glpsol", "--lp", lp_file, "-o", sol_file]
    
    # Execute the command
    subprocess.run(command)


def testTout():
    root = "./instances/"
    for path, subdir, files in os.walk(root):
        for name in files:
            print(name)
            main(name, 0)
            time.sleep(1)
            print("-----------------")
            print("Name 1 incoming")
            print("-----------------")
            time.sleep(1)
            main(name, 1)
            print("-----------------")
            print("Done")