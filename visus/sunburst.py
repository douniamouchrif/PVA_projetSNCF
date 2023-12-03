import plotly.graph_objects as go
from dash import dcc


def build_sunburst(df_all_trees):
    colors = {
        1 : 'purple',
        2 : 'blue',
        3 : 'green',
        4 : 'yellow',
        5 : 'orange',
        6 : 'red',
        'Réseau': 'pink',
        'Mobilités': 'olive',
        'Voyageur': 'grey',
        'Cause Tiers Réseau': 'brown',
        'Cause Tiers Mobilités': 'cyan',
        'Cause Tiers Voyageur': 'magenta',
        'Indéterminé': 'lime',
        'CT': 'teal',
        'ACCIDENTS SNCF' : 'white'
    }
    df_all_trees['color'] = df_all_trees['id'].map(colors)

    fig = go.Figure(go.Sunburst(
        labels=df_all_trees['id'],
        parents=df_all_trees['parent'],
        values=df_all_trees['value'],
        branchvalues='total',
        hovertemplate='<b>%{label} </b> <br> Count: %{value}',
        maxdepth=2,
        marker=dict(
            colors=df_all_trees['color'],  
            line=dict(color='black', width=1)  
        ),
    ))
    fig.update_layout(margin=dict(t=15, b=15, r=15, l=15))
    return fig

def build_dropdown_year(item_list):
    options = [{"label": x, "value": x} for x in item_list]
    return dcc.Dropdown(id='dropdown',
                        options=options,
                        value=item_list[2],
                        style={'color': 'black'})

def build_dropdown_year_multi(item_list):
    options = [{"label": x, "value": x} for x in item_list]
    return dcc.Dropdown(id='dropdown',
                        options=options,
                        value=item_list, 
                        multi=True, 
                        style={'color': 'black'})