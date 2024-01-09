import pandas as pd
from data.connect import db


# Boxplot
def get_data_boxplot_t():
    result23 = db.sncf23.find()
    df23 = pd.DataFrame(result23)
    result1522 = db.sncf1522.find()
    df1522 = pd.DataFrame(result1522)
    df23['date'] = pd.to_datetime(
        df23['date'], errors='coerce')  # Conversion en datetime
    df23['year'] = df23['date'].dt.strftime('%Y')
    df_filtered_23 = df23.dropna(subset=['year', 'origine'])
    df1522['date'] = pd.to_datetime(
        df1522['date'], errors='coerce')  # Conversion en datetime
    df1522['year'] = df1522['date'].dt.strftime('%Y')
    df_filtered_1522= df1522.dropna(subset=['year', 'origine'])
    df_filtered = pd.concat([df_filtered_1522,df_filtered_23])
    return df_filtered

# Scatterplot
def get_data_scatterplot(year):
    if year == '2023':
        result = db.sncf23.find()
        df = pd.DataFrame(result)
        gravite = 'gravite_epsf'

    else:
        result = db.sncf1522.find()
        df = pd.DataFrame(result)
        gravite = 'niveau_gravite'
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.strftime('%Y')
    df = df.dropna(subset=['year'])
    df['Mois'] = df['date'].dt.to_period('M')
    df = df[df['year'] == year]
    grouped_data = df.dropna(subset=[gravite]).groupby('Mois')[
        gravite].mean().reset_index()
    return grouped_data


# Lineplot
def get_data_lineplot():
    cursor = db.sncf1522.find({'origine': {'$ne': None}, 'region': {'$ne': None}, 'date': {'$ne': None}}, {
                            'origine': 1, 'region': 1, 'date': 1, '_id': 0})
    data = list(cursor)
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  
    df['year'] = df['date'].dt.strftime('%Y')
    df = df.dropna(subset=['year', 'origine'])
    return df


# Sunburst
def get_data_sunburst(year):
    if year == '2023':
        cursor = db.sncf23.find({'gravite_epsf': {'$ne': None, '$gt': 0, '$lt': 7}}, {
                                'gravite_epsf': 1, 'origine': 1, 'date': 1, '_id': 0})
        df = pd.DataFrame(list(cursor))
        gravite = 'gravite_epsf'
    else:
        cursor = db.sncf1522.find({'niveau_gravite': {'$ne': None, '$gt': 0, '$lt': 7}}, {
                                  'niveau_gravite': 1, 'origine': 1, 'date': 1, '_id': 0})
        df = pd.DataFrame(list(cursor))
        gravite = 'niveau_gravite'
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.strftime('%Y')
    df = df.dropna(subset=['year'])
    df = df[df['year'] == year]
    df = df.groupby([gravite, 'origine']).size().reset_index(name='count')
    levels = ['origine', gravite]
    value_column = 'count'
    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value'])
    for i, level in enumerate(levels):
        df_tree = pd.DataFrame(columns=['id', 'parent', 'value'])
        dfg = df.groupby(levels[i:]).sum(numeric_only=True)
        dfg = dfg.reset_index()
        df_tree['id'] = dfg[level].copy()
        if i < len(levels) - 1:
            df_tree['parent'] = dfg[levels[i+1]].copy()
        else:
            df_tree['parent'] = 'ACCIDENTS SNCF'
        df_tree['value'] = dfg[value_column]
        df_all_trees = pd.concat([df_all_trees, df_tree], ignore_index=True)
    total = pd.Series(dict(id='ACCIDENTS SNCF', parent='',
                      value=df[value_column].sum()))
    df_all_trees = pd.concat([df_all_trees, pd.DataFrame(
        [total], columns=['id', 'parent', 'value'])], ignore_index=True)
    return df_all_trees


# Barplot
def get_data_barplot_1522(years):
    cursor = db.sncf1522.find(
        {}, {'region': 1, 'origine': 1, 'niveau_gravite': 1, 'date': 1})
    df = pd.DataFrame(list(cursor))
    df['year'] = pd.to_datetime(df['date']).dt.year
    df['niveau_gravite'] = pd.to_numeric(df['niveau_gravite'], errors='coerce')
    selected_data = df[(df['year'] >= years[0]) & (df['year'] <= years[1])]
    # Les 5 principales régions et types d'incidents avec le plus d'incidents
    top_regions = selected_data['region'].value_counts().nlargest(5).index
    top_types = selected_data['origine'].value_counts().nlargest(5).index
    top_data = selected_data[selected_data['region'].isin(
        top_regions) & selected_data['origine'].isin(top_types)]
    mean_gravity_df = top_data.groupby(['region', 'origine'])[
        'niveau_gravite'].mean().unstack()
    mean_gravity_df = mean_gravity_df[mean_gravity_df.sum(
    ).sort_values(ascending=False).index]
    mean_gravity_df = mean_gravity_df.loc[mean_gravity_df.sum(
        axis=1).sort_values(ascending=False).index]
    return mean_gravity_df


# Dropdown
def get_years_dropdown():
    cursor = db.sncf1522.find({'niveau_gravite': {'$ne': None, '$gt': 0, '$lt': 7}}, {
                              'niveau_gravite': 1, 'origine': 1, 'date': 1, '_id': 0})
    df = pd.DataFrame(list(cursor))
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.strftime('%Y')
    df = df.dropna(subset=['year'])
    years = df['year'].unique()
    years = sorted(years, key=lambda x: int(x))
    years.append('2023')  # Ajouter l'année 2023 à la liste
    return years


# Range slider
def get_years_range_slider():
    cursor = db.sncf1522.find({'niveau_gravite': {'$ne': None, '$gt': 0, '$lt': 7}}, {
                              'niveau_gravite': 1, 'origine': 1, 'date': 1, '_id': 0})
    df = pd.DataFrame(list(cursor))
    df['date'] = pd.to_datetime(
        df['date'], errors='coerce')
    df['year'] = df['date'].dt.strftime('%Y')
    df = df.dropna(subset=['year'])
    unique_years = df['year'].unique()
    min_val = int(unique_years.min()) if unique_years.size > 0 else 2015
    max_val = int(unique_years.max()) if unique_years.size > 0 else 2022
    default_values = [min_val, max_val]
    marks_list = list(range(min_val, max_val + 1))
    return min_val, max_val, default_values, marks_list
