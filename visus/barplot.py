import plotly.express as px
from dash import dcc

def barplot_1522(data):
    fig = px.bar(data, barmode='group')
    fig.update_layout(
        xaxis={'title': 'Région'},
        yaxis={'title': 'Gravité Moyenne'},
        title='Gravité Moyenne des 5 Principaux Types d\'Incidents dans les 5 Principales Régions'
    )
    return fig


def build_range_slider(min_val, max_val, default_values, marks_list):
    marks = {str(mark): str(mark) for mark in marks_list}
    return dcc.RangeSlider(
        id='rangeslider',
        min=min_val,
        max=max_val,
        value=default_values,
        marks=marks,
        step=1,
    )
