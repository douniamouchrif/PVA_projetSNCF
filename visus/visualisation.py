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


# Scatter
def build_scatter(df, year):
    if year == '2023':
        gravite = 'gravite_epsf'
    else:
        gravite = 'niveau_gravite'
    df['Mois'] = df['Mois'].dt.strftime('%Y-%m')
    fig = px.scatter(df, x='Mois', y=gravite,
                     title=f'Gravité moyenne par mois', color=gravite, size=gravite)
    fig.update_traces(marker=dict(size=12), selector=dict(mode='markers'))
    fig.update_layout(clickmode='event+select', yaxis_title="Gravité")
    return fig


# Lineplot
def build_lineplot(df, selected_option, cumulative_mode):
    incidents_par_annee = df.groupby(['year', 'origine']).size().reset_index(name='nombre_incidents')
    
    if cumulative_mode:
        incidents_par_annee['cumulative_incidents'] = incidents_par_annee.groupby('origine')['nombre_incidents'].cumsum()
        y_column = 'cumulative_incidents'
        title = 'Nombre cumulatif d\'incidents au cours des années'
    else:
        y_column = 'nombre_incidents'
        title = 'Nombre d\'incidents au cours des années'

    if selected_option == 'all':
        aggregated_df = incidents_par_annee.groupby('year')[y_column].sum().reset_index()
        fig_line = px.line(aggregated_df, x='year', y=y_column, title=title,
                           labels={'nombre_incidents': 'Nombre d\'incidents', 'year': 'Années'})
    else:
        filtered_df_line = incidents_par_annee[incidents_par_annee['origine'].isin(df['origine'].unique())]
        fig_line = px.line(filtered_df_line, x='year', y=y_column, color='origine',
                           title=title, labels={'nombre_incidents': 'Nombre d\'incidents', 'year': 'Années'})
        fig_line.update_layout(showlegend=True)

    fig_line.update_layout(yaxis=dict(showline=False, showgrid=False, zeroline=False))
    return fig_line

def build_heapmap(df, selected_option, click_data):
    incidents_par_region_annee = df.groupby(['year', 'origine', 'region']).size().reset_index(name='nombre_incidents')
    
    if click_data and 'points' in click_data and click_data['points']:
        if selected_option == 'all' : 
            fig_heatmap = px.imshow(incidents_par_region_annee.pivot_table(index='year', columns='region', values='nombre_incidents'),
                                labels=dict(x="Régions", y="Années", color="Nombre d'incidents"),
                                title='Heatmap du nombre d\'incidents par région au cours des années pour toutes les origines confondues')
        else :
            clicked_origine = click_data['points'][0]['curveNumber']
            filtered_df = incidents_par_region_annee[incidents_par_region_annee['origine'] == df['origine'].unique()[clicked_origine]]
            clicked_origine_label = incidents_par_region_annee['origine'].unique()[clicked_origine]

            fig_heatmap = px.imshow(filtered_df.pivot_table(index='year', columns='region', values='nombre_incidents'),
                                    labels=dict(x="Régions", y="Années", color="Nombre d'incidents"),
                                    title=f'Heatmap du nombre d\'incidents causés par {clicked_origine_label} par région au cours des années')
    else:
        fig_heatmap = px.imshow(incidents_par_region_annee.pivot_table(index='year', columns='region', values='nombre_incidents'),
                                labels=dict(x="Régions", y="Années", color="Nombre d'incidents"),
                                title='Heatmap du nombre d\'incidents par région au cours des années pour toutes les origines confondues')
        
    fig_heatmap.update_layout(xaxis=dict(showline=False, showgrid=False, zeroline=False, tickangle=45),
                            yaxis=dict(showline=False, showgrid=False, zeroline=False))
    return fig_heatmap


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
