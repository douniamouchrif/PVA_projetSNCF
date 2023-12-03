import plotly.graph_objects as go
from dash import dcc


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
    #fig.show()
    return fig

def build_dropdown_year(item_list):
    options = [{"label": x, "value": x} for x in item_list]
    return dcc.Dropdown(id='dropdown',
                        options=options,
                        value=item_list[2])