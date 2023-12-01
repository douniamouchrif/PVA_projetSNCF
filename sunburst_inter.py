from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from data.connect import db

def hierarchical_dataframe_sunburst(year):
    cursor = db.sncf1522.find({'niveau_gravite': {'$ne': None, '$gt': 0, '$lt': 7}}, {'niveau_gravite': 1, 'origine': 1,'date': 1, '_id': 0})
    df = pd.DataFrame(list(cursor))
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    print(df)
    df['year'] = df['date'].dt.strftime('%Y')
    print(df['year'])
    df = df.dropna(subset=['year'])
    df = df[df['year'] == year]
    df = df.groupby(['niveau_gravite', 'origine']).size().reset_index(name='count')
    levels = ['origine', 'niveau_gravite']
    value_column = 'count'
    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value'])
    for i, level in enumerate(levels):
        df_tree = pd.DataFrame(columns=['id', 'parent', 'value'])
        dfg = df.groupby(levels[i:]).sum()
        dfg = dfg.reset_index()
        df_tree['id'] = dfg[level].copy()
        if i < len(levels) - 1:
            df_tree['parent'] = dfg[levels[i+1]].copy()
        else:
            df_tree['parent'] = 'ACCIDENTS SNCF'
        df_tree['value'] = dfg[value_column]
        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
    total = pd.Series(dict(id='ACCIDENTS SNCF', parent='', value=df[value_column].sum()))
    df_all_trees = df_all_trees.append(total, ignore_index=True)
    return df_all_trees

def get_year():
    cursor = db.sncf1522.find({'niveau_gravite': {'$ne': None, '$gt': 0, '$lt': 7}}, {'niveau_gravite': 1, 'origine': 1, 'date': 1, '_id': 0})
    df = pd.DataFrame(list(cursor))
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Conversion en datetime
    df['year'] = df['date'].dt.strftime('%Y')
    df = df.dropna(subset=['year'])
    return df['year'].unique()

def build_sunburst(df_all_trees):
    marker_colors = ['blue', 'green', 'red', 'purple', 'yellow', 'pink', 'grey', 'orange', 'cyan', 'magenta', 'brown', 'teal', 'lime', 'indigo', 'maroon', 'olive', 'navy', 'aquamarine', 'orchid', 'slategray']
    fig = go.Figure(go.Sunburst(
        labels=df_all_trees['id'],
        parents=df_all_trees['parent'],
        values=df_all_trees['value'],
        branchvalues='total',
        hovertemplate='<b>%{label} </b> <br> Count: %{value}',
        maxdepth=2,
        marker=dict(colors=marker_colors),
    ))
    fig.update_layout(margin=dict(t=15, b=15, r=15, l=15))
    return fig

def build_dropdown_year(item_list):
    options = [{"label": x, "value": x} for x in item_list]
    return dcc.Dropdown(id='dropdown',
                        options=options,
                        value=item_list[2])

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(style={'backgroundColor': '#001F3F', 'color': 'white', 'height': '100vh'}, children=[
    html.H1("Visualisation Sunburst", style={'textAlign': 'center'}),
    
    html.Div([
        html.P("Sélectionner une année (par la suite on rajoutera la possiblité d'en séléctionner plusieurs) :"),
        build_dropdown_year(get_year()),
        dcc.Graph(id='sunburst')
    ])
])

@app.callback(Output(component_id='sunburst', component_property='figure'),
              [Input(component_id='dropdown', component_property='value')])
def graph_update(dropdown_values):
    if dropdown_values is None:
        dropdown_values = get_year()[0]
    dataa = hierarchical_dataframe_sunburst(dropdown_values)
    return build_sunburst(dataa)

if __name__ == '__main__':
    app.run_server(debug=True)
