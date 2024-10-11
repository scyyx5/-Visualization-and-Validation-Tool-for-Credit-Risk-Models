import sys
sys.path.insert(1, '../../visualization/')
import re
import os

def adjust_data(filename, ageTitle, cohortTitle, defaultFlagTitle, predictedDefaultTitle):
    """
    adjust database for the convenience of further processing.
    parameter:
    filename (str): a string indicating the name of the graph.
    ageTitle (str): tile of age
    cohortTitle (str): title of cohort
    defaultFlagTitle (str): title of default flag
    predictedDefaultTitle (str): title of predicted default rate
    """
    filename = '../../visualization/' + filename + ".csv"
    if(ageTitle != "t"):
        alter_title(filename,ageTitle,"t")
    if(cohortTitle != "v"):
        alter_title(filename,cohortTitle,"v")
    if(defaultFlagTitle != "y"):
        alter_title(filename,defaultFlagTitle,"y")
    if(predictedDefaultTitle != "pd"):
        alter_title(filename,predictedDefaultTitle,"pd")



def alter_title(filename,old_str,new_str):
    """"
    change title of the data for further processing
    parameter:
    filename (str): a string indicating the name of the graph.
    old_str (str): origin title
    new_str (str): adjusted title
    """
    with open(filename, "r") as f1,open("%s.bak" % filename, "w") as f2:
        for line in f1:
            if old_str in line:
                line = line.replace(old_str, new_str)
            f2.write(line)
    os.remove(filename)
    os.rename("%s.bak" % filename, filename)

    


