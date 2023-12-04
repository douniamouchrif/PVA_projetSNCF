from dash import dcc

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