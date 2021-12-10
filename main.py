from GetData import *
from Analysis import *
from GUI import *

def main():
    gui = GUI() #initialize interface object
    gui.setInput() #request metals from user
    input = gui.getInput() #set the metals list to a variable to be used
    data = GetData() #intialize object to get data from excel file
    analysis = Analysis(data.getDf()) #get that excel file data and import it into the analysis object 
    results = analysis.dummyLogReg(input) #run the logsisitic regression algorithm
    file_name = "Data/"+str(gui.input.replace(" ","_"))+".txt" #create .txt file name
    file = open(file_name, "w") #create the file 
    file.write(results) #export the results to the .txt file
    analysis.createHeatMap() #create heat map of gene expression with exposure to each variable
    print("Completed. Check folder for results .txt file. Includes names of tested metals.\n") #print messsage to screen telling user program is complete

main()