import pandas
import numpy

from sklearn.linear_model import LogisticRegression

import matplotlib.pyplot as plt

import seaborn as sns

class Analysis:

    def __init__(self, df): 
        self.data = df #global variable that stores the dataframe
        self.log_reg = LogisticRegression() #initialize log regression object in a global variable
        self.new_data = ""


    def createXs(self, list):
        pandas.options.mode.chained_assignment = None  #remove a dumb warning
        new_data = self.data[list] #create a dataframe with just the metals of interest
        return new_data #return new dataframe

    def createYs(self, list):
        pandas.options.mode.chained_assignment = None  #remove a dumb warning
        self.new_data = self.data[list] #create a dataframe with just the metals of interest
        self.new_data["total"] = self.new_data.sum(axis=1, numeric_only=True) #create a new column with the summed gene expression of each gene
        self.new_data["up_down"] = numpy.where(self.new_data["total"] > 0, 1, 0) #create a new column of dummy variables that defines
        #upregulation (magnitude greater is positive) as 1 and downregulation (mag is less negative) as zero
        return self.new_data["up_down"] #return just the new dumb variable list 
 
    def removeSpaces(self, input):
        try:
            while True:
                input.remove(" ") #remove white spaces from a list
        except ValueError:
            pass
            
        return input

    def dummyLogReg(self, param_list):
        list = ["Ag","As","Cd","Cr","Cu","Hg","Zn"] #listof metals
        interesting = [] #empty list to store list of metals that are inputted by user
        interesting_str = "" #string to convert this list into a displayable format
        coeff_str = "" #string to convert coefficients into a displayable format
 
        for i in range(len(list)): #if the inputted metal is in the list of metals
            if list[i] in param_list:
                interesting.append(list[i]) #add to the list of interesting variables
 
        x = self.createXs(param_list) #create variable of x values
        y = self.createYs(param_list) #create variable of y value

        self.log_reg.fit(x,y) #fit the logistic regression model

        intercept = str(self.log_reg.intercept_)[1:-1] #get the intercept
        coefficients = str(self.log_reg.coef_)[2:-2].split(" ") #get list of coefficients
        
        coefficients = self.removeSpaces(coefficients) #remove spaces from this list


        for i in range(len(interesting)):
            coeff_str = coeff_str + interesting[i]+ ": " +str(coefficients[i]) + "\n" #make coefficients look displayable

        for a in range(len(interesting)):
            if a == 0:
                interesting_str = interesting[a]
            else:
                interesting_str = interesting_str + ", "+interesting[a] #make names of metals look displayable
        

        results = "RESULTS...\nTRANSITION METALS OF INTEREST WERE: "+interesting_str+"\n"+"INTERCEPT OF LOGISTIC REGRESSION = "+str(intercept)+"\n"+"METAL IMPACTS ON GENE UP REGULATION OR DOWN REGULATION...\n"+coeff_str

        #format and return results

        return results


    def createHeatMap(self):
        heatmapdf = self.new_data #set the corresponding data set to a local variable
        heatmapdf = heatmapdf.drop('total',axis=1) #remove total gene expression
        heatmapdf = heatmapdf.drop('up_down',axis=1) #remove the up/down dummy variables
        lst = heatmapdf.columns.values.tolist() #create a list of the column names 
        name = "" #create string variable to hold file name 
        for i in range(len(lst)):
            name = name + lst[i] + "_" #format list of columns to file name
        filename = "Data/"+name+".png" #set the file name
        plt.figure(figsize=(9,5), dpi=300) #set figure size and dimensions
        hm = sns.heatmap(heatmapdf, cmap="RdYlGn") #create the heat map
        plt.savefig(filename) #save it with the proper name