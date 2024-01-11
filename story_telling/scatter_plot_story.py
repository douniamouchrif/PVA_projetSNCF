from dash import html


def get_text_below_scatter():
    return html.Div([
        html.P("Scatterplot visualisant la gravité moyenne des incidents de sécurité par mois de 2016 à 2023. On rappelle que les gravités sont enregistrées entre 1 (la plus faible) et 6 (la plus forte) pour les incidents de sécurité, et que la notion de gravité n'a été introduite qu'en 2016 dans ces bases de données."),
        html.P("Remarquons le fait que les moyennes de gravité varient entre 3 et 4 chaque année jusqu'en 2022, puis entre 4 et 5 en 2023. La raison est qu'en 2023, chaque incident est à minimum 4 de gravité et nous ignorons la raison de cette spécificité, à part le fait que la base de données de 2023 n'apparait pas sur la même table de données que les autres années."),
        html.P("Concernant la visualisation, il n'y a globalement pas de mois qui se démarque d'un autre durant chaque année. Cependant, en 2020, pendant la crise du coronavirus, on remarque que les bases de données n'ont plus été remplies à partir de Mai 2020, ce qui peut s'expliquer par la mise en place du prolongement du confinement."),
        html.P("Pour conclure, il y a globalement une consistance durant ces 8 dernières années concernant les gravités des incidents de la sécurité.")
    ], style={'margin-top': '20px', 'font-size': '16px',  'fontSize': '1.25em'})
