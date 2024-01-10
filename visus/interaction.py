from dash import dcc, html

# Dropdown
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


# Range slider
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

#radio item
def build_radioitems():
    radioitems = dcc.RadioItems(
        id='origine-radio',
        options=[
            {'label': 'Distinction des origines', 'value': 'distinct'},
            {'label': 'Globale', 'value': 'all'},
        ],
        value='distinct',  # Valeur par défaut
        inline=True,
        style={'fontSize': 20, 'textAlign': 'center'}
    )

    cumulative_radioitem = dcc.RadioItems(
        id='cumulative-radio',
        options=[
            {'label': 'Cumulatif', 'value': True},
            {'label': 'Non Cumulatif', 'value': False},
        ],
        value=False,  # Valeur par défaut
        inline=True,
        style={'fontSize': 20, 'textAlign': 'center'}
    )

    return html.Div([radioitems, cumulative_radioitem])