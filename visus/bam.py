import plotly.express as px
import plotly.graph_objects as go

def build_boxplot(df):
   
    fig = px.box(df, x='year', y=df.groupby('year').cumcount(), labels={'y': 'Nombre d incidents'},
                 title='Nombre d incidents par année',
                 category_orders={'year': sorted(df['year'].unique())},
                 animation_group='origine')
    fig.add_trace(go.Scatter(
            x=['2019', '2019'],
            y=[0, df.groupby('year').cumcount().max() + 1],
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
            yaxis=dict(title=dict(text='Nombre d incidents', font=dict(size=22)),
                       tickfont=dict(size=18),),
            legend=dict(
                x=1.02,
                y=0.5,
                traceorder='normal',
                font=dict(size=16),
                bgcolor='rgba(255, 255, 255, 0.5)',
            )
        )
    fig.show()

