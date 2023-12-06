import plotly.express as px
import plotly.graph_objects as go

# Boxplot


def build_boxplot(data):
    fig = px.box(data, x='year', y=data.groupby('year').cumcount(), labels={'y': 'Nombre d incidents'},
                 title='Nombre d\'incidents par année',
                 category_orders={'year': sorted(data['year'].unique())},
                 animation_group='origine')
    fig.add_trace(go.Scatter(
        x=['2019', '2019'],
        y=[0, data.groupby('year').cumcount().max() + 1],
        mode="lines",
        line=dict(color="red", width=2, dash='dash'),
        showlegend=True,  # Afficher la légende pour cette trace
        name='Début de la crise du COVID-19'
    ))
    fig.update_layout(
        title_font=dict(size=24),
        xaxis=dict(
            title=dict(text='Années', font=dict(size=18)),
            tickfont=dict(size=18),
        ),
        yaxis=dict(title=dict(text='Nombre d\'incidents', font=dict(size=22)),
                   tickfont=dict(size=18),),
        legend=dict(
            x=1.02,
            y=0.5,
            traceorder='normal',
            font=dict(size=16),
            bgcolor='rgba(255, 255, 255, 0.5)',
        )
    )
    return fig


# Scatter 2015-2022
def build_scatter(df, year):
    if year == '2023':
        gravite = 'gravite_epsf'
    else:
        gravite = 'niveau_gravite'
    df['Mois'] = df['Mois'].dt.strftime('%Y-%m')
    fig = px.scatter(df, x='Mois', y=gravite,
                     title=f'Gravité moyenne par mois', color=gravite, size=gravite)
    return fig


# Lineplot
def build_lineplot(data):
    df_grouped = data.groupby(
        ['year', 'origine']).size().reset_index(name='count')
    df_grouped['cumulative_count'] = df_grouped.groupby('origine')[
        'count'].cumsum()
    fig = px.line(df_grouped, x='year', y='cumulative_count', color='origine',
                  labels={
                      'cumulative_count': 'Nombre cumulatif d\'événements', 'year': 'Année'},
                  title='Évolution du nombre cumulatif d\'événements par origine au fil des années')
    fig.update_layout(
        title_font=dict(size=24),
        xaxis=dict(
            title=dict(text='Années', font=dict(size=18)),
            tickfont=dict(size=18),
        ),
        yaxis=dict(title=dict(text='Nombre cumulatif d\'événements', font=dict(size=22)),
                   tickfont=dict(size=18),),
        legend=dict(
            x=1.02,
            y=0.5,
            traceorder='normal',
            font=dict(size=16),
            bgcolor='rgba(255, 255, 255, 0.5)',
        )
    )
    return fig


# Sunburst
def build_sunburst(df_all_trees):
    colors = {
        1: 'purple',
        2: 'blue',
        3: 'green',
        4: 'yellow',
        5: 'orange',
        6: 'red',
        'Réseau': 'pink', 'Mobilités': 'olive',
        'Voyageur': 'grey',
        'Cause Tiers Réseau': 'brown',
        'Cause Tiers Mobilités': 'cyan',
        'Cause Tiers Voyageur': 'magenta',
        'Indéterminé': 'lime',
        'CT': 'teal',
        'Accident de personne': 'maroon',
        'Collision passage à niveau': 'aliceblue',
        'Voyageurs': 'lightcoral',
        'Electrisation tiers': 'mediumseagreen',
        'Collision hors passage à niveau': 'slategray',
        'FRET': 'wheat',
        'EF CAP TRAIN': 'tomato',
        'EF Ext': 'navy',
        'Externe': 'orchid',
        'Heurt installation par tiers': 'aquamarine',
        'ACCIDENTS SNCF': 'white'
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


# Barplot
def barplot_1522(data):
    fig = px.bar(data, barmode='group')
    fig.update_layout(
        xaxis={'title': 'Région'},
        yaxis={'title': 'Gravité Moyenne'},
        title='Gravité Moyenne des 5 Principaux Types d\'Incidents dans les 5 Principales Régions'
    )
    return fig
