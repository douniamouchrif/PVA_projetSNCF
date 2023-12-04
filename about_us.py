from dash import html

def about_content():
    return html.Div([
        html.H1("About Us", style={'textAlign': 'center'}),
        html.P("Bienvenue sur notre page de présentation ! ", style={'textAlign': 'center', 'textDecoration': 'underline', 'fontSize': '1.5em'}),
        html.P("Qui sommes-nous ? ",style={'fontSize': '3em'}),
        html.P(["Nous sommes un groupe de 4 étudiantes, ABARKAN Suhaila, MOUCHRIF Dounia, ROMAN Karina et TISSANDIER Mathilde en master 1 du ",
               html.A("Cursus Master en Ingénierie (CMI) en Ingénierie Statistique et Informatique (ISI)",
                      href='https://formations.u-bordeaux.fr/#/details-formation?type=parcours-type&id=39693', target='_blank'), " à l'Université de Bordeaux."])
    ])