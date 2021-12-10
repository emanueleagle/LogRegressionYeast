class GUI:

    def __init__(self):
        self.input = " "
        print("Hello!")
        print("Look at impacts of Silver (Ag), Arsenic (As), Cadmium (Cd), Chromium (Cr), Copper (Cu), Mercury (Hg), and Zinc (Zn) on Model Organism Saccharomyces cerevisiae")
        print("Enter abbreviations of the listed metals with spaces in between to search for combinations")
        print("Example: Ag Cd Cu\n")

    def setInput(self):
        self.input = input("Enter names of metals you're interested in analyzing: ") #recieve the user's input
    

    def getInput(self):
        return self.input.split(" ") #get the input from the user
