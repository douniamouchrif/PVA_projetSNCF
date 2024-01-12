from dash import html


def get_text_below_map():
    return html.Div([
        html.P("La carte ci-dessus présente de manière interactive les données relatives aux incidents ferroviaires survenus dans chaque région de la France métropolitaine, couvrant la période allant du 2 janvier 2015 au 30 août 2023."),
        html.P("Ces dates correspondent respectivement à la première et à la dernière entrée dans les bases de données traitant de ce sujet. Il est important de noter que ces informations sont automatiquement mises à jour : dès qu'une nouvelle date est ajoutée à la base de données, elle devient la plus récente, facilitant ainsi une analyse en temps réel."),
        html.P("De plus, cette carte interactive offre la possibilité de choisir entre la représentation du nombre total d'incidents par région ou la moyenne par région du niveau de gravité. Vous pouvez également personnaliser la période d'analyse à l'aide du calendrier situé en haut à gauche."),
        html.P("Cette visualisation permet une observation détaillée des régions en fonction du nombre d'incidents ou du niveau moyen de gravité. Une coloration jaune intense indique soit un nombre élevé d'incidents, soit une gravité moyenne plus élevée par rapport aux autres régions de la France."),
        html.Li("Pendant la période allant du 2 janvier 2015 au 30 août 2023, la région Provence-Alpes-Côte-d'Azur se distingue avec le plus grand nombre d'incidents, totalisant près de 250 événements."),
        html.Li("En revanche, sur la même période, la région Grand Est affiche la moyenne la plus élevée de gravité parmi toutes les régions, avec une valeur d'environ 3.9 sur une échelle de 6."),
        html.Li("Les résultats peuvent ainsi changer en fonction de la période choisie."),
        html.Br(),
        html.P("En conclusion, cette carte interactive offre une perspective approfondie sur les incidents ferroviaires en France métropolitaine entre janvier 2015 et août 2023. La capacité de personnaliser la période d'analyse et de visualiser le nombre total d'incidents ou la gravité moyenne par région facilite une compréhension fine des tendances régionales."),
        html.P("Notamment, la région Provence-Alpes-Côte-d'Azur se distingue par un nombre significatif d'incidents, tandis que le Grand Est présente la moyenne la plus élevée de gravité. Ces informations peuvent orienter les décisions et actions visant à renforcer la sécurité ferroviaire dans des régions spécifiques."),
    ], style={'margin-top': '20px', 'font-size': '16px', 'fontSize': '1.25em'})
