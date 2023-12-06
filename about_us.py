from dash import html

def about_content():
    return html.Div([
        html.H1("About Us", style={'textAlign': 'center'}),
        html.P("Bienvenue sur notre page de présentation ! ", style={'textAlign': 'center', 'textDecoration': 'underline', 'fontSize': '1.5em'}),
        html.Div(style={'display': 'flex', 'alignItems': 'center'}, children=[
            html.Img(src="/static/IMG/Groupe.jpg", style={'width': '30%', 'height': 'auto'}),
            html.P(["Nous sommes un groupe de 4 étudiantes, TISSANDIER Mathilde, MOUCHRIF Dounia, ABARKAN Suhaila et ROMAN Karina en master 1 du ",
                    html.A("Cursus Master en Ingénierie (CMI) en Ingénierie Statistique et Informatique (ISI)",
                           href='https://formations.u-bordeaux.fr/#/details-formation?type=parcours-type&id=39693', target='_blank'),
                    " à l'Université de Bordeaux. Nous réalisons un projet de visualisation sur les données de la SNCF. Pour ce faire, nous utilisons différentes bases de données disponibles aux adresses suivantes : "
            ], style={'marginLeft': '20px'}),
            html.Div(children=[
                html.Li(html.A("Incidents de sécurité (Evénements de sécurité remarquables - ESR) de janvier 2015 à décembre 2022", href='https://data.sncf.com/explore/dataset/incidents-securite/table/?sort=date', target='_blank')),
                html.Li(html.A("Incidents de sécurité (EPSF) depuis janvier 2023", href='https://data.sncf.com/explore/dataset/incidents-de-securite-epsf/table/?sort=date&calendarview=month&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoiZ3Jhdml0ZV9lcHNmIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI0ExMDA2QiJ9XSwieEF4aXMiOiJkYXRlIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoibW9udGgiLCJzb3J0IjoiIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJpbmNpZGVudHMtZGUtc2VjdXJpdGUtZXBzZiIsIm9wdGlvbnMiOnsic29ydCI6ImRhdGUifX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZSwidGltZXNjYWxlIjoiIn0%3D', target='_blank')),
                html.Li(html.A("Liste des lignes électrifiées", href='https://data.sncf.com/explore/dataset/liste-des-lignes-electrifiees/table/', target='_blank')),
                html.Li(html.A("Lignes par type", href='https://data.sncf.com/explore/dataset/lignes-par-type/table/', target='_blank')),
                html.Li(html.A("Lignes par région administrative", href='https://data.sncf.com/explore/dataset/lignes-par-region-administrative/table/', target='_blank'))

            ])
        ])
    ])
