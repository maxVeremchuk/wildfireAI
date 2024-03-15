import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def multiple_y_axes_figure(x_data: list, y_data: list, legend_title: list=[''], markers: list=[go.Bar], yax_title: list=['a','b','c','d']):
    if len(x_data) != len(y_data) != len(legend_title) != len(markers):
        return

    dynamic_fig = go.Figure()
    
    i_int = 1
    i_str = '1'
    for x, y, name, trace in zip(x_data, y_data, legend_title, markers):
        dynamic_fig.add_trace(trace(x=x, y=y, name=name, yaxis=f'y{i_str}'))
        i_int += 1
        i_str = i_int
    
    dynamic_fig.update_layout(
        yaxis1=dict(
            title=yax_title[0],
            side="right",
        ),
        yaxis2=dict(
            title=yax_title[1],
            side="left",
            overlaying="y1",
        ),
        yaxis3=dict(
            title=yax_title[2],
            side="right",
            overlaying="y1",
            position = 0.99
        ),
        yaxis4=dict(
            title=yax_title[3],
            side="left",
            overlaying="y1",
            position = 0.01
        )
    )

    # dynamic_fig.show()
    return dynamic_fig

def correlation(data):
    cm = np.corrcoef(data.values.T)
    sns.set(font_scale=1)
    f, ax = plt.subplots(figsize=(20, 13))
    hm = sns.heatmap(cm, annot=True, square=True, fmt='.2f', annot_kws={'size': 15}, yticklabels=data.columns, xticklabels=data.columns)
    # plt.show()
    return plt
