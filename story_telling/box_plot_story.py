from dash import html


def get_text_below_boxplot():
    return html.Div([
        html.P("Box plot montrant la répartition du nombre d'accidents ferroviaires par an de 2015 à 2023."),
        html.P("Vous trouverez ci-dessous une analyse détaillée de chaque année :"),
        "2015 : L’année avec le plus grand nombre d’incidents. La médiane est supérieure à 150 événements et il existe des valeurs extrêmes supérieures à 200 événements.",
        html.Br(),
        "2016 : Une légère diminution par rapport à 2015, avec une médiane d'environ 120 accidents. La dispersion des données est similaire à celle de 2015.",
        html.Br(),
        "2017 : La médiane et la dispersion des événements ont continué à diminuer légèrement par rapport à 2016.",
        html.Br(),
        "2018 : La médiane est similaire à celle de 2017, et la dispersion aussi avec des valeurs extrêmes inférieures.",
        html.Br(),
        "2019 : Nous observons une diminution significative du nombre médian d’événements, envrion 81 événements, avec une moindre dispersion que les années précédentes.",
        html.Br(),
        "2020 : Marqué par la ligne rouge pointillée, qui indique le début de la crise du COVID-19, nous observons que le nombre d’événements a légérement augmenté depuis 2019. La médiane est d'environ 91 événements, et la dispersion a quelque peu augmentée.",
        html.Br(),
        "2021 : Une légère diminution par rapport à 2020, avec une médiane de 78 accidents. La dispersion reste plus faible par rapport aux années antérieures à 2020.",
        html.Br(),
        "2022 : Le nombre d’événements a diminué et minimal, avec une médiane proche de 2019 (69 événements) et une dispersion similaire à 2021.",
        html.Br(),
        "2023 : L’année en cours ou la dernière année enregistrée présente une médiane plus élevée que 2022, avec une dispersion importante et des valeurs extrêmes assez élevées.",
        html.Br(),
        html.Br(),
        html.U("En résumé, il existe une différence significative dans le nombre d’accidents ferroviaires par an entre 2015 et 2023. Le changement le plus important s’est produit entre 2019 et 2020, correspondant au début de la crise du COVID-19, lorsque le nombre d’accidents a considérablement diminué puis réaugmenté. À mesure que les trains circulent moins fréquemment, les risques d’accidents diminueront naturellement, ce qui pourrait entraîner une diminution de la fréquence des accidents signalés. "),
        html.Br(),
        html.P("Par ailleurs, les opérations de maintenance et d'inspection des voies ferrées et du matériel roulant auraient pu être réalisées de manière plus régulière ou avec plus d'attention pendant cette période, car des horaires moins chargés auraient permis un accès plus facile aux infrastructures sans interruption du service. Comme le montrent les données, à mesure que les restrictions liées au COVID-19 seront levées et que la vie commencera à revenir à la normale, le nombre de trains en circulation pourrait commencer à augmenter, entraînant une augmentation progressive du nombre d'accidents. "),
        "L’augmentation est plus importante en 2023, ce qui suggère un retour plus complet du trafic ferroviaire, ou éventuellement d’autres facteurs contribuant à l’augmentation des accidents.",
    ], style={'margin-top': '20px', 'font-size': '16px', 'fontSize': '1.25em'})
