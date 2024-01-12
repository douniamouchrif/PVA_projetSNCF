from dash import html


def get_text_below_barplot():
    return html.Div([
    html.P("Le barplot représente la gravité moyenne des cinq principaux types d'incidents les plus fréquemment rencontrés dans les cinq régions ayant enregistré le plus grand nombre d'incidents en France pour les années sélectionnées."),
    html.P("En utilisant le range-slider situé au-dessus de la visualisation, nous pouvons choisir les années que nous souhaitons afficher dans l'histogramme."),
    html.P("Comme on peut l'observer, chaque regroupement de barres représente la gravité moyenne des cinq causes les plus courantes au cours de cette période, pour les cinq régions ayant enregistré le plus d'incidents."),
    html.P("Pour les années de 2015 à 2022, nous constatons que les cinq régions ayant enregistré le plus grand nombre d'incidents sont l'Occitanie, l'Île-de-France, la Provence-Alpes-Côte d'Azur, l'Auvergne-Rhône-Alpes et les Pays de la Loire."),
    html.Li("Les principales causes d'incidents sont généralement les Causes Tiers Réseaux, c'est-à-dire des éléments extérieurs au réseau ferroviaire principal."),
    html.Li("Ainsi, l'analyse sera complètement différente pour une période différente d'années. Nous avons également la possibilité de sélectionner une seule année en ajustant les deux points du range-slider au même niveau."),
    html.Br(),
    html.P("En conclusion, l'analyse des incidents ferroviaires dans les cinq régions les plus touchées en France entre 2015 et 2022 met en lumière les principaux types d'incidents et leur gravité moyenne. Les régions telles que l'Occitanie, l'Île-de-France, la Provence-Alpes-Côte d'Azur, l'Auvergne-Rhône-Alpes et les Pays de la Loire ont été particulièrement impactées par un nombre significatif d'incidents."),
    html.P("Les Causes Tiers Réseaux, liées à des éléments extérieurs au réseau ferroviaire principal, émergent comme les principales sources d'incidents. Il est important de souligner que l'analyse peut varier considérablement d'une année à l'autre, soulignant la nécessité de prendre en compte la période spécifique pour des insights pertinents."),
    html.P("En utilisant le range-slider, nous avons la flexibilité de cibler des années spécifiques, permettant ainsi une analyse plus détaillée. Ces informations peuvent orienter les décisions et les efforts visant à renforcer la sécurité ferroviaire dans ces régions, en mettant l'accent sur les causes prédominantes d'incidents."),
    html.P("En résumé, cette visualisation offre un aperçu approfondi des tendances et des facteurs contribuant aux incidents ferroviaires en France, mettant en lumière les régions les plus impactées."),
        ], style={'margin-top': '20px', 'font-size': '16px', 'fontSize': '1.25em'})