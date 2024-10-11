import pandas as pd
import pandas as pd
from datetime import datetime
import sys
sys.path.insert(1, '../../visualization/')
start_date = datetime(2016,1,1)

class GraphController:
    """
    Contains all the information necessary to generate graphs
    """
    filename = "sim"
    isDark = False
    error = "0"
    age_unit = "Month"
    cohort_unit = "Month"
    data = None
    colorVision = "None"
    language = "English"

    
    def __init__(self, filename="sim", isDark=False, colorVision = "None",error="0", 
                 age_unit="Month", cohort_unit="Month", separator=",", decimal=".",language="English"):
        """
        initialize graphController
        parameter:
        - filename (str): a string indicating the name of the graph.
        - isDark (bool): If True, use colorblind-friendly colors in the visualizations. (Default is False)
        - colorVision (str): mode of color vision dificiency. possible choice: "redGreen", "blueYellow","full". (default is "full")
        - error: a string indicating the error to add to the slope of the predicted data (default is "0")
        - ageUnit (str): unit of age. Possible value: "Month", "Year", "Day". (default is "Month")
        - cohortUnit (str): unit of cohort. Possible value: "Month", "Year", "Day". (default is "Month")
        - separator (str): separator of database. (default is ",")
        - decimal (str): decimal of database. (default is ".")
        - language (str): Language user choose. (default is "English")
        
        """
        self.filename =filename
        try:
            self.data = pd.read_csv(f"../../visualization/{filename}.csv", decimal=decimal, sep=separator)
        except:
            self.data = pd.read_csv(f"{filename}.csv", decimal=decimal, sep=separator)
        self.isDark = isDark
        self.colorVision = colorVision
        self.error = error
        self.age_unit = age_unit
        self.cohort_unit = cohort_unit
        self.language = language
        self.data['pd'] = self.data['pd']
        if(age_unit == "Day"):
            self.data["t"] = self.data["t"]/365.25 * 12 
            self.data = self.data.astype({'t':'int'})
        elif(age_unit == "Year"):
            self.data["t"] = self.data["t"] * 12
            self.data = self.data.astype({'t':'int'})
        if(cohort_unit == "Day"):
            self.data["v"] = self.data["v"]/365.25 * 12
            self.data = self.data.astype({'v':'int'})
            self.data = self.data.iloc[:][self.data["v"] <= 36]   #TODO
        elif(cohort_unit == "Year"):
            self.data["v"] = self.data["v"] * 12
            self.data = self.data.astype({'v':'int'})

    def data_filter(self,feature,condition,value):
        """
        filter data according to given conditinos
        parameter:
        feature (str): String of feature
        condition (str): condition. Possible value: "<",">"
        value (str): value.
        i.e. featuer condition value   e.g. x1 < 400
        """
        if condition == ">":
            data = self.data.iloc[:][self.data[feature] > int(value)]
        elif condition == "<":
            data = self.data.iloc[:][self.data[feature] < int(value)]
        else:
            data = self.data
        return data
