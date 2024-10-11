# can use random testing and metamorphic testing later
def adjust_slope(x_list, y_list,error):
    """
    This function takes x_list and y_list which is used to plot a graph. 
    The error is applied to the slop to adjust the graph.
    Parameters:
    x_list (list): list of x values.
    y_list (list): list of y values.
    error (str): The value of error for the slop.
    Returns:
    None
    """
    y_adjust = []
    pre_x = 0
    pre_y = 0
    pre_y_adjust = 0
    y_adjust.append(y_list[0])
    for i in range(0,len(x_list) - 1):
        x1 = x_list[i]
        y1 = y_list[i]
        k1 = (y1 - pre_y) / (x1 - pre_x)
        k2 = k1 + float(error)
        y2 = k2 * (x1 - pre_x) + pre_y_adjust
        pre_x = x1
        pre_y = y1
        pre_y_adjust = y2
        y_adjust.append(y2)

    return y_adjust

