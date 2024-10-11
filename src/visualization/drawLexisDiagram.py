# reference: https://plotly.com/python/heatmaps/#basic-heatmap-with-plotlygraphobjects
#            https://blog.csdn.net/qq_25443541/article/details/121479144?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166704801916782427461331%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166704801916782427461331&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-121479144-null-null.142^v62^control,201^v3^control,213^v1^control&utm_term=%E7%83%AD%E5%8A%9B%E5%9B%BEplotly&spm=1018.2226.3001.4187


# color scale for heatmap: 
# https://plotly.com/r/builtin-colorscales/#builtin-diverging-color-scales
# https://plotly.com/python/reference/heatmap/
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta
import plotly.offline as py
from APCAnalysis import *
import math
start_date = datetime(2016,1,1)


def draw_Lexis_Diagram_Real(data,language = "English",isDark = False):
    """
    Defining a function to draw a Lexis diagram
    parameter:
    data (pandas DataFrame): The input data for Age-Period-Cohort analysis.
    isDark (bool): If True, use colorblind-friendly colors in the visualizations. 
                    Default is False.
    error (str): The type of error for visualization. Default is "0".
    Returns:
    None
    """
    # Adding a new column to the DataFrame
    data['int_c'] = data['v'] + data['t']
    # Grouping the data by 't' and 'int_c' columns
    grouped_data = data.groupby(['t','int_c']).agg(def_num = ('y','sum'),
                                         number = ('t','count'),dr=('y','sum'))
    # Calculating the weighted mean
    grouped_data["dr"] = grouped_data["dr"]/grouped_data["number"]


    #generate index for x,y,z
    int_c_indices = []
    t_indices = []
    for index in grouped_data.index:
        int_c_indices.append(index[1])
        t_indices.append(index[0])
    int_c_indices = list(set(int_c_indices))
    t_indices = list(set(t_indices))

    # Creating a list of all possible index combinations
    all_index = []
    for y in t_indices:
        for x in int_c_indices:
            all_index.append((y, x))
    
    # Adding None for missing data
    z_values = []
    for index in all_index:
        if index in grouped_data.index:
            z_values.append(grouped_data._get_value(index, 'dr'))
        else:
            z_values.append(None)
    
    # Reshaping the list into a matrix
    default_rate = []
    for line in np.reshape(z_values, (len(t_indices), len(int_c_indices))):
        default_rate.append(list(line))

    # Creating a list of time intervals
    c_indices =[]
    for i in int_c_indices:
        c = start_date + relativedelta(months=i)
        c_indices.append(c)
    c_indices

    # Defining a list of color themes
    theme = ["hot_r","YlGnBu","OrRd","greys",[[0, 'rgb(255,255,204)'],
        [1, 'rgb(97,97,189)']], [[0, 'rgb(205,255,153)'],
        [1, 'rgb(51,102,0)']],[[0, 'rgb(153,255,255)'],
        [1, 'rgb(0,153,153)']],"Spectral","PiYG"]
        
    theme_name = ["hot_r","YlGnBu","OrRd","greys",
                  "yellows","greens","blues","Spectral","PiYG"]
    default_rate = np.array(default_rate).astype(float)
    # Visualizing the Lexis diagram for each theme
    for i in range(0,len(theme)):
        visualize_lexis_diagram(theme[i],theme_name[i],
                        int_c_indices,t_indices,default_rate,
                        "",language,isDark)
        visualize_lexis_diagram(theme[i],theme_name[i],
                        int_c_indices,t_indices,np.sinh(default_rate),
                        "sinh_",language,isDark)
        visualize_lexis_diagram(theme[i],theme_name[i],
                        int_c_indices,t_indices,np.exp(default_rate),
                        "exp_",language,isDark)


'''

#old version
def drawLexisDiagram(filename = "sim",feature = None, condition = None, 
                     value = None, ageUnit = "Month", cohortUnit = "Month",
                     separator = ",",decimal = "."):
    #data = pd.read_csv('simDTS2.csv')
    data = pd.read_csv('../../visualization/' + filename + '.csv',decimal=decimal,sep=separator)

    if(condition == ">"):
        data = data.iloc[:][data[feature] > int(value)]
    elif(condition == "<"):
        data = data.iloc[:][data[feature] < int(value)]

    if(ageUnit == "Day"):
        data["t"] = data["t"]/365.25 * 12
        data = data.astype({'t':'int'})
    elif(ageUnit == "Year"):
        data["t"] = data["t"] * 12
        data = data.astype({'t':'int'})
    if(cohortUnit == "Day"):
        data["v"] = data["v"]/365.25 * 12
        data = data.astype({'v':'int'})
    elif(cohortUnit == "Year"):
        data["v"] = data["v"] * 12
        data = data.astype({'v':'int'})
        
    data['int_c'] = data['v'] + data['t']
    grouped_data = data.groupby(['t','int_c']).agg(def_num = ('y','sum'),number = ('t','count'),dr=('y','sum'))
    grouped_data["dr"] = grouped_data["dr"]/grouped_data["number"]


    #generate index for x,y,z
    int_c_indices = []
    t_indices = []
    for index in grouped_data.index:
        int_c_indices.append(index[1])
        t_indices.append(index[0])
    int_c_indices = list(set(int_c_indices))
    t_indices = list(set(t_indices))
    #print(len(int_c_indices), len(t_indices))
    #print(grouped_data.index)
    all_index = []
    for y in t_indices:
        for x in int_c_indices:
            all_index.append((y, x))
    #print(int_c_indices)
    z_values = []
    for index in all_index:
        if index in grouped_data.index:
            z_values.append(grouped_data._get_value(index, 'dr'))
        else:
            z_values.append(None)
    default_rate = []
    for line in np.reshape(z_values, (len(t_indices), len(int_c_indices))):
        default_rate.append(list(line))
    #print(default_rate)
    c_indices =[]
    for i in int_c_indices:
        c = start_date + relativedelta(months=i)
        c_indices.append(c)
    c_indices



#--------------------------hot-------------------
    fig_hot = go.Figure(data=go.Heatmap(
                    z=default_rate,
                    x=int_c_indices,
                    y=t_indices,
                    colorscale='hot_r',
                    hoverongaps = True))

    fig_hot.update_layout(
                title_x=0.5,
                xaxis_title = "calendar time",
                yaxis_title = "age",
                font = dict(
                    size = 20
                ))

    #fig.show()
    py.plot(fig_hot, filename='../../../res/lexis_diagram_hot_r.html',auto_open = False)
    #py.plot(fig, filename='lexis_diagram.html',auto_open = False)


#---------------------YlGnBu
    fig_YlGnBu = go.Figure(data=go.Heatmap(
                    z=default_rate,
                    x=int_c_indices,
                    y=t_indices,
                    colorscale='YlGnBu',
                    hoverongaps = True))

    fig_YlGnBu.update_layout(
                title_x=0.5,
                xaxis_title = "calendar time",
                yaxis_title = "age",
                font = dict(
                    size = 20
                ))

    #fig.show()
    py.plot(fig_YlGnBu, filename='../../../res/lexis_diagram_YlGnBu.html',auto_open = False)



#---------------------OrRd-------------
    fig_OrRd = go.Figure(data=go.Heatmap(
                    z=default_rate,
                    x=int_c_indices,
                    y=t_indices,
                    colorscale='OrRd',
                    hoverongaps = True))

    fig_OrRd.update_layout(
                title_x=0.5,
                xaxis_title = "calendar time",
                yaxis_title = "age",
                font = dict(
                    size = 20
                ))

    #fig.show()
    py.plot(fig_OrRd, filename='../../../res/lexis_diagram_OrRd.html',auto_open = False)



#---------------------greys-------------
    fig_greys = go.Figure(data=go.Heatmap(
                    z=default_rate,
                    x=int_c_indices,
                    y=t_indices,
                    colorscale='greys',
                    hoverongaps = True))

    fig_greys.update_layout(
                title_x=0.5,
                xaxis_title = "calendar time",
                yaxis_title = "age",
                font = dict(
                    size = 20
                ))

    #fig.show()
    py.plot(fig_greys, filename='../../../res/lexis_diagram_greys.html',auto_open = False)




'''