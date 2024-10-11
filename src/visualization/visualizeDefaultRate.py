import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys
sys.path.insert(1, '../../visualization/')
from adjustSlope import adjust_slope

import plotly.express as p
import plotly.offline as py
# py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.figure_factory as ff    

from datetime import datetime
from dateutil.relativedelta import relativedelta


def default_cohort(data,isDark = False,colorVision = "None",language = "English"):
    """
    visualize default rate and cohort.
    parameter:
    - data (pandas DataFrame): The input data for Age-Period-Cohort analysis.
    - isDark (bool): If True, use colorblind-friendly colors in the visualizations. (Default is False)
    - colorVision (str): mode of color vision dificiency. possible choice: "redGreen", "blueYellow","full". (default is "full")
    - language (str): Language user choose. (default is "English")
    """
    current_month = 20
    #pre processing
    data['cal'] = data['t'] + data['v']
    grouped_cal = data.groupby('cal')[['cal','y','pd']]
    pct_cal = grouped_cal.agg({'cal' : 'count','y':'sum','pd':'sum'})


    data['cal'] = data['t'] + data['v']
    pct_cal = data.groupby(['cal']).agg(number = ('cal','count'),
                                        dr=('y','sum'),edr=('pd','sum'))
    

    pct_cal["dr"] = pct_cal["dr"]/pct_cal["number"]
    pct_cal["edr"] = pct_cal["edr"]/pct_cal['number']

    xTitle = "calendar time"
    if (language == "Chinese"):
        xTitle = "日期"
    

    x_range = [pct_cal.index.min(),pct_cal.index.max()]
    y_range = [pct_cal["dr"].append(pct_cal["edr"]).min(),
               pct_cal["dr"].append(pct_cal["edr"]).max()]
    visualize_data("dr_cal",pct_cal.index[0:current_month],pct_cal["dr"][0:current_month],
                  pct_cal["edr"][0:current_month],x_range,y_range,
                  xTitle,isDark,colorVision,language=language)
    visualize_data("dr_cal_predicted",pct_cal.index,pct_cal["dr"],
                  pct_cal["edr"],x_range,y_range,xTitle,isDark,colorVision,language=language)
    
    # apply sinh scale
    pct_cal["sinhdr"] = pct_cal["dr"].apply(np.sinh)
    pct_cal["sinhedr"] = pct_cal["edr"].apply(np.sinh)
    sinh_y_range = [pct_cal["sinhdr"].append(pct_cal["sinhedr"]).min(),
               pct_cal["sinhdr"].append(pct_cal["sinhedr"]).max()]
    visualize_data("sinh_dr_cal",pct_cal.index[0:current_month],pct_cal["sinhdr"][0:current_month],
                  pct_cal["sinhedr"][0:current_month],x_range,sinh_y_range,
                  xTitle,isDark,colorVision,"sinh ",language=language)
    visualize_data("sinh_dr_cal_predicted",pct_cal.index,pct_cal["sinhdr"],
                  pct_cal["sinhedr"],x_range,sinh_y_range,xTitle,
                  isDark,colorVision,"sinh ",language=language)
    
    # apply exp scale
    pct_cal["expdr"] = pct_cal["dr"].apply(np.exp)
    pct_cal["expedr"] = pct_cal["edr"].apply(np.exp)
    exp_y_range = [pct_cal["expdr"].append(pct_cal["expedr"]).min(),
               pct_cal["expdr"].append(pct_cal["expedr"]).max()]
    visualize_data("exp_dr_cal",pct_cal.index[0:current_month],pct_cal["expdr"][0:current_month],
                  pct_cal["expedr"][0:current_month],x_range,exp_y_range,
                  xTitle,isDark,colorVision,"exp ",language=language)
    visualize_data("exp_dr_cal_predicted",pct_cal.index,pct_cal["expdr"],
                  pct_cal["expedr"],x_range,exp_y_range,xTitle,
                  isDark,colorVision,"exp ",language=language)
    

def default_age(data,isDark = False,colorVision ="None",language = "English"):
    """
    visualize default rate and age.
    parameter:
    - data (pandas DataFrame): The input data for Age-Period-Cohort analysis.
    - isDark (bool): If True, use colorblind-friendly colors in the visualizations. (Default is False)
    - colorVision (str): mode of color vision dificiency. possible choice: "redGreen", "blueYellow","full". (default is "full")
    - language (str): Language user choose. (default is "English")
    """
    current_age = 10 
    # pre processing
    pct_age = data.groupby(['t']).agg(number = ('t','count'),
                                      dr=('y','sum'),edr=('pd','sum'),std = ('pd','std'))
    pct_age["dr"] = pct_age["dr"]/pct_age["number"]
    pct_age["edr"] = pct_age["edr"]/pct_age["number"]

    xTitle = "age(month)"
    if (language == "Chinese"):
        xTitle = "年龄（月）"
    
    x_range = [pct_age.index.min(),pct_age.index.max()]
    y_range = [pct_age["dr"].append(pct_age["edr"]).min(),
               pct_age["dr"].append(pct_age["edr"]).max()]
    visualize_data("dr_age",pct_age.index[0:current_age],pct_age["dr"][0:current_age],
                  pct_age["edr"][0:current_age],x_range,y_range,xTitle,isDark,colorVision,language=language)
    visualize_data("dr_age_predicted",pct_age.index,pct_age["dr"],
                  pct_age["edr"],x_range,y_range,xTitle,isDark,colorVision,language=language)
    
    
    
    # apply sinh scale
    pct_age["sinhdr"] = pct_age["dr"].apply(np.sinh)
    pct_age["sinhedr"] = pct_age["edr"].apply(np.sinh)
    sinh_y_range = [pct_age["sinhdr"].append(pct_age["sinhedr"]).min(),
               pct_age["sinhdr"].append(pct_age["sinhedr"]).max()]
    visualize_data("sinh_dr_age",pct_age.index[0:current_age],pct_age["sinhdr"][0:current_age],
                  pct_age["sinhedr"][0:current_age],x_range,sinh_y_range,xTitle,isDark,colorVision, "sinh ",language=language)
    visualize_data("sinh_dr_age_predicted",pct_age.index,pct_age["sinhdr"],
                  pct_age["sinhedr"],x_range,sinh_y_range,xTitle,isDark,colorVision, "sinh ",language=language)
    
    # apply exp scale
    pct_age["expdr"] = pct_age["dr"].apply(np.exp)
    pct_age["expedr"] = pct_age["edr"].apply(np.exp)
    exp_y_range = [pct_age["expdr"].append(pct_age["expedr"]).min(),
               pct_age["expdr"].append(pct_age["expedr"]).max()]
    visualize_data("exp_dr_age",pct_age.index[0:current_age],pct_age["expdr"][0:current_age],
                  pct_age["expedr"][0:current_age],x_range,exp_y_range,xTitle,isDark,colorVision,"exp ",language=language)
    visualize_data("exp_dr_age_predicted",pct_age.index,pct_age["expdr"],
                  pct_age["expedr"],x_range,exp_y_range,xTitle,isDark,colorVision,"exp ",language=language)
    

    


def visualize_data(filename,x,realy,predictedy,xrange,yrange,xTitle,isDark = False,colorVision = "None",prefix = "",language = "English"):
    """
    visualize default rate according to given information
    parameter:
    - filename (str): a string indicating the name of the graph.
    - x (list): list of x values
    - realy (list): real value of y
    - predictedy (list): list of predicted y values
    - xrange (list): range of x values
    - yrange (list): range of y values
    - xTitle (str): title of x axis
    - isDark (bool): If True, use colorblind-friendly colors in the visualizations. (Default is False)
    - colorVision (str): mode of color vision dificiency. possible choice: "redGreen", "blueYellow","full". (default is "full")
    - prefix (str): prefix of file name. (default is "")
    - language (str): Language user choose. (default is "English")
    """
    if(language == "Chinese"):
        yTitile = prefix + "违约率(%)"
        trace0_name = "违约率"
        trace1_name = "期望违约率"
    else:
        yTitile = prefix + "default rate(%)"
        trace0_name = "default rate"
        trace1_name = "expected default rate"

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
            title=xTitle,
            range=xrange
        ),
        yaxis=dict(
            title= yTitile,
            range=yrange
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
    
    trace0 = go.Scatter(
        x = x,
        # y = [ i + float(error) for i in pct_age["dr"][0:current_age]] ,
        y = realy,
        mode = 'lines',
        name = trace0_name
    )
    

    trace1 = go.Scatter(
        x = x,
        # y = [ i + float(error) for i in pct_age["edr"][0:current_age]],
        y = predictedy,
        mode = 'lines',
        name = trace1_name
    )

    if(colorVision == "redGreen"):
        trace0.update(marker_color = "green")
    elif(colorVision =="blueYellow"):
        trace1.update(marker_color = "green")
    

    figure = go.Figure({'data': [trace1,trace0],'layout': layout})

    figure.update_yaxes(exponentformat= "power")

    if(colorVision == "full"):
        figure.update_traces(marker_color="grey")

    # figure.show()
    # save image
    if(isDark):
        figure.update_layout(
            plot_bgcolor='rgb(63, 71, 79)',
            paper_bgcolor ='rgb(63, 71, 79)',
            font_color="white")

    py.plot(figure,filename = '../../../res/' + filename + '.html',auto_open = False)