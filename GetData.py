import pandas
import numpy 

class GetData:

    def __init__(self):
        self.df_first = pandas.read_excel("script/yeast_gene_data.xlsx") #open the excel file
        self.df_second = self.df_first.iloc[1:, :] #remove the first row as its irrelevant
        self.df_three = self.df_second.dropna(axis=0,how="any") #remove all rows (genes with N/A values)

    def getDf(self):
        return self.df_three #return the dataframe
