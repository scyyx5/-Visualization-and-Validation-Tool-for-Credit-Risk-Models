import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score 
from sklearn.model_selection import KFold 
import numpy as np
import pandas as pd
from sklearn import model_selection
import plotly.graph_objs as go
from datetime import datetime
from dateutil.relativedelta import relativedelta
import plotly.offline as py
import sys
import math
sys.path.insert(1, '../../visualization/')
from adjustSlope import adjust_slope
start_date = datetime(2016,1,1)




def apc_analysis(data,isDark = False,colorVision ="None",error = "0",language = "English"):
    """
    This function takes in a pandas DataFrame and returns the Age-Period-Cohort analysis
    including the visualizations of the effects of age, period, and cohort.
    Parameters:
    data (pandas DataFrame): The input data for Age-Period-Cohort analysis.
    isDark (bool): If True, use colorblind-friendly colors in the visualizations. Default is False.
    error (str): a string indicating the error to add to the slope of the predicted data (default is "0")
    Returns:
    None
    """
    # Get the coefficients for age, period, and cohort
    para = get_effect(data)
    effect_list_predicted = para['effect_list_predicted']
    effect_list_real =para['effect_list_real']
    
    len_v = para['len_v']
    len_t = para['len_t']
    len_c = para['len_c']
    v = para['v']
    t = para['t']
    c = para['c']
    default_rate = para['default_rate']
    default_rate_real = para['default_rate_real']

    cohort_effect_predicted = effect_list_predicted.coef_[0:len_v-1]
    age_effect_predicted = effect_list_predicted.coef_[len_v :len_t + len_v - 1]
    period_effect_predicted = effect_list_predicted.coef_[len_t + len_v : len_t + len_v + len_c]
    cohort_effect_real = effect_list_real.coef_[0:len_v-1]
    age_effect_real = effect_list_real.coef_[len_v :len_t + len_v - 1]
    period_effect_real = effect_list_real.coef_[len_t + len_v : len_t + len_v + len_c]
    
    cohort_effect_predicted = np.array(cohort_effect_predicted).astype(float)
    cohort_effect_real = np.array(cohort_effect_real).astype(float)
    # Visualize the effects of age, period, and cohort
    visualize_effect("cohort",v,cohort_effect_predicted,cohort_effect_real,isDark,colorVision,error,language)
    visualize_effect("age",t,age_effect_predicted,age_effect_real,isDark,colorVision,error,language)
    visualize_effect("period",c,period_effect_predicted,period_effect_real,isDark,colorVision,error,language)
    
    # apply sinh scale
    visualize_effect("sinh_cohort",v,np.sinh(cohort_effect_predicted),np.sinh(cohort_effect_real),
                     isDark,colorVision,error,language)
    visualize_effect("sinh_age",t,np.sinh(age_effect_predicted),np.sinh(age_effect_real),
                     isDark,colorVision,error,language)
    visualize_effect("sinh_period",c,np.sinh(period_effect_predicted),np.sinh(period_effect_real),
                     isDark,colorVision,error,language)

    # apply exp scale
    visualize_effect("exp_cohort",v,np.exp(cohort_effect_predicted),
                     np.exp(cohort_effect_real),isDark,colorVision,error,language)
    visualize_effect("exp_age",t,np.exp(age_effect_predicted),
                     np.exp(age_effect_real),isDark,colorVision,error,language)
    visualize_effect("exp_period",c,np.exp(period_effect_predicted),
                     np.exp(period_effect_real),isDark,colorVision,error,language)
    
    
    
   
    # Visualize the Lexis diagrams
    default_rate = np.array(default_rate).astype(float)
    default_rate_real = np.array(default_rate_real).astype(float)
    theme = ["hot_r","YlGnBu","OrRd","greys",[[0, 'rgb(255,255,204)'], 
            [1, 'rgb(97,97,189)']], [[0, 'rgb(205,255,153)'], [1, 'rgb(51,102,0)']],
            [[0, 'rgb(153,255,255)'], [1, 'rgb(0,153,153)']],"Spectral","PiYG"]
    theme_name = ["hot_r","YlGnBu","OrRd","greys","yellows","greens","blues","Spectral","PiYG" ]
    for i in range(0,len(theme)):
        visualize_lexis_diagram(theme[i],theme_name[i],c,t,default_rate,"apc_",language,isDark)
        visualize_lexis_diagram(theme[i],theme_name[i],c,t,default_rate_real,"real_apc_",language,isDark)
        visualize_lexis_diagram(theme[i],theme_name[i],c,t,np.sinh(default_rate),"sinh_apc_",language,isDark)
        visualize_lexis_diagram(theme[i],theme_name[i],c,t,np.exp(default_rate),"exp_apc_",language,isDark)
        visualize_lexis_diagram(theme[i],theme_name[i],c,t,np.sinh(default_rate),"sinh_real_apc_",language,isDark)
        visualize_lexis_diagram(theme[i],theme_name[i],c,t,np.exp(default_rate_real),"exp_real_apc_",language,isDark)
    


def get_effect(data):        
    """
    This function calculates the effect of variables on the response variable and returns relevant information.
    Parameters:
    data (pandas DataFrame): The input data for Age-Period-Cohort analysis.
    """

    # Add a column to the DataFrame that combines 'v' and 't' columns
    data['c'] = data['v'] + data['t']
    # Group the data by 't', 'v', and 'c' columns, then aggregate data 
    # based on count, sum of 'y', and sum of 'pd'
    data = data.groupby(['t','v','c']).agg(number = ('y','count'),
                                        dr=('y','sum'),pd=('pd','sum'))
    
    # Compute the average of 'dr' and 'pd' for each group based on 'number'
    data["dr"] = data["dr"]/data["number"]
    data['pd'] = data['pd']/data['number']

    # Extract 't', 'v', and 'c' from the index of 'data'
    t_list,v_list,c_list = [],[],[]
    for (i,j,k) in data.index:
        t_list.append(i)
        v_list.append(j)
        c_list.append(k)
    

    data['t'] = t_list 
    data['v'] = v_list 
    data['c'] = c_list

    # Prepare 'yTrain1', 'yTrain2', and 'train_encode' based on 'data'
    yTrain1 = data['pd']
    yTrain2 = data['dr']

    # One-hot encode age, cohort, and 'c' values
    train_encode_simplify = data[['v','t','c']]
    train_encode = pd.get_dummies(train_encode_simplify,
                                columns = ['v','t','c'])
    
    # Create feature variable arrays for Ridge regression
    xTrain_encode = train_encode.values

    # Fit linear regression models for pd and dr
    effect_list_predicted = Ridge(alpha=0.001)
    effect_list_predicted.fit(xTrain_encode,yTrain1)

    effect_list_real = Ridge(alpha=2)
    effect_list_real.fit(xTrain_encode,yTrain2)

    # Create arrays of unique age, cohort, and 'c' values for creating Lexis diagrams
    v = data['v'].unique()
    len_v = len(v)
    t = data['t'].unique()
    len_t = len(t)
    c = data['c'].unique()
    len_c = len(c)

    # Create a 2D array of predicted pd values to create a Lexis diagram
    default_rate = get_predicted_default_rate(train_encode,t,c,effect_list_predicted)
    
    # Create a 2D array of predicted dr values to create a Lexis diagram
    default_rate_real = get_predicted_default_rate(train_encode,t,c,effect_list_real)

        

    return { 'len_t': len_t, "len_v": len_v, "len_c":len_c,"effect_list_predicted": 
            effect_list_predicted,"effect_list_real":effect_list_real,
            'v':v, 't':t, 'c':c, "default_rate":default_rate,
            "default_rate_real":default_rate_real}



def get_predicted_default_rate(train_encode,t,c,effect_list_model):
    """
    Create a 2D array of predicted default rate values to create a Lexis diagram
    Parameter: 
    train_encode: encoded a,p,c value
    t: age list
    c: period list
    effect_list_model: model to predict default rate
    """
    # Create a 2D array of predicted pd values to create a Lexis diagram
    default_rate = []
    for i in t:
        templist = []
        for j in c:
            try:
                encode = train_encode.loc[i].loc[j-i]
                y = effect_list_model.predict(encode.values)[0]
            except:
                y = np.nan
            templist.append(y)
        default_rate.append(templist)
    return default_rate



def visualize_effect(graphName,x,predicty,realy,isDark = False,colorVision ="None",error = "0",language = "English"):
    """
    visualize apc effect
    Parameters:
    - graphName: a string indicating the name of the graph
    - x: an array representing the input variable
    - predicty: an array representing the predicted output variable
    - realy: an array representing the actual output variable
    - isDark: a boolean indicating whether the color scheme should be adjusted for color blindness (default is False)
    - error: a string indicating the error to add to the slope of the predicted data (default is "0")
    """
    # Create a list of tuples, each containing a value from x, predicty, and realy
    list_to_sort = list(zip(x.tolist(), predicty.tolist(), realy.tolist()))
    # Sort the list of tuples by the first value (x value)
    list_to_sort.sort(key = lambda a: a[0])
    # Separate the sorted values back into individual lists
    sorted_x = [x[0] for x in list_to_sort]
    sorted_predicty = [x[1] for x in list_to_sort]
    sorted_realy = [x[2] for x in list_to_sort]
    xTitle = ""
    
    if(language == "Chinese"):
        if(graphName == "age"):
            xTitle = "年龄"
        elif(graphName == "period"):
            xTitle = "时期"
        elif(graphName == "cohort"):
            xTitle = "队列"
        yTitle = xTitle + " 效应"
        trace0_name = "基于预测数据的APC"
        trace1_name = "基于真实数据的APC"
    else:
        xTitle = graphName
        yTitle = graphName + " effect"
        trace0_name = "APC by predicted data"
        trace1_name = "APC by real data"

    # Set the layout of the graph with the specified options
    layout = go.Layout(
        paper_bgcolor='rgb(233,233,233)',
        title=
            {
                'y':0.9,
                'x':0.45,
                'xanchor': 'center', 
                'yanchor': 'top'
            },
            xaxis=dict(
                title= xTitle,
                range = [x.min(),x.max()]
            ),
            yaxis=dict(
                title= yTitle,
            ),
        font=dict(
            size=20
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    
    

    # Create a scatter plot trace using the sorted x and predicted y values
    trace0 = go.Scatter(
        x = sorted_x,
        # y = [i + float(error) for i in clf_v],
        # y = clf_v,
        y = adjust_slope(sorted_x,sorted_predicty,error),
        mode = 'lines',
        name = trace0_name
    )

    # Create a scatter plot trace using the sorted x and real y values
    trace1 = go.Scatter(
        x = sorted_x,
        # y = [i + float(error) for i in clf_v],
        # y = clf_v,
        y = adjust_slope(sorted_x,sorted_realy,error),
        mode = 'lines',
        name = trace1_name
    )
    

    if(colorVision == "redGreen"):
        trace1.update(marker_color = "green")
    elif(colorVision =="blueYellow"):
        trace0.update(marker_color = "green")

    # Create the figure object and add the traces and layout
    figure = go.Figure({'data': [trace0,trace1],
                            'layout': layout})

    figure.update_yaxes(exponentformat= "power")

    if(colorVision == "full"):
        figure.update_traces(marker_color="grey")

    # If isDark is True, update the layout
    if(isDark):
        figure.update_layout(
            plot_bgcolor='rgb(63, 71, 79)',
            paper_bgcolor ='rgb(63, 71, 79)',
            font_color="white")
    # Plot the figure and save the file to the specified location with the specified filename
    py.plot(figure, filename='../../../res/' + graphName + 'effect.html',
            auto_open = False)
    


def visualize_lexis_diagram(theme,theme_name,c,t,z,prefix,language = "English",isDark =False):
    """
    Creates a Lexis diagram visualization using the plotly library.
    Parameter:
    - theme: a string representing the color theme of the visualization
    - c: a list of strings representing the calendar time
    - t: a list of strings representing the age
    - z: a 2D list of numerical values representing the heatmap data
    - prefix: a string representing the prefix of the output file name
    """
    # Create a new Figure object with a Heatmap trace using the provided data
    figure = go.Figure(data=go.Heatmap(
                    z=z,                # the heatmap values to be plotted
                    x=c,                # the x-axis values (calendar time)
                    y=t,                # the y-axis values (age)
                    zsmooth="best",     # the smoothing algorithm to use. Other possible value: "fast" | "best" | False
                    colorscale=theme,   # the color scheme to use
                    hoverongaps = True, # whether to display hover information for missing data
                    connectgaps=False))  # whether to connect gaps in the heatmap

    figure.update_layout(
                paper_bgcolor='rgb(233,233,233)',  # the background color of the plot
                title="lexis diagram",             # the title of the plot
                title_x=0.5,                       # the horizontal alignment of the title
                xaxis_title = "calendar time",     # the label for the x-axis
                yaxis_title = "age",               # the label for the y-axis
                font=dict(size=20),                 # the font size of the plot
                )
    if(language == "Chinese"):
        figure.update_layout(
            xaxis_title = "日期",     # the label for the x-axis
            yaxis_title = "年龄",               # the label for the y-axis
            title = "lexis 图"         # the title of the plot
        )
    
    figure.update_traces(colorbar_exponentformat="SI", selector=dict(type='heatmap'))
    figure.update_traces(colorbar_showexponent="first", selector=dict(type='heatmap'))

    # figure.show()
    if(isDark):
        figure.update_layout(
            plot_bgcolor='rgb(63, 71, 79)',
            paper_bgcolor ='rgb(63, 71, 79)',
            font_color="white")
        
    # Save the plot to an HTML file using Plotly and the provided file path and prefix
    py.plot(figure, filename='../../../res/'+ prefix + 'lexis_diagram_' + theme_name +'.html',
           auto_open = False)                # whether to automatically open the plot in a browser


