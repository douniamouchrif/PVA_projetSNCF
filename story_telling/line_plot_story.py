from dash import html

def get_text_below_lineplot():
    return html.Div([
        html.P("Nous affichons ici un lineplot montrant l'évolution du nombre d'incidents au cours du temps en distinguant les différentes causes. Par défaut le mode non cumulatif est séléctionné mais nous avons la possibilité d'afficher la version cumulative du graphique. Aussi, nous pouvons afficher une version du lineplot ne distinguant pas les causes, en séléctionnant l'option Globale."),
        html.P("Juste en dessous du lineplot, nous affichons un heapmap montrant la fréquence des incidents en fonction des années et des différentes régions et cela, selon la cause séléctionnée (en cliquant sur la courbe correspondante) sur le graphique au-dessus."),
        html.P("Nous pouvons voir à travers le lineplot, que les causes d'incidents les plus réccurentes sont Réseau, Mobilité et Voyageur, néanmoins la cause Réseau reste largement au dessus de toutes les causes. De plus, nous pouvons appercevoir que la cause Voyageur n'est apparue qu'en 2020."),
        html.P("Si nous nous intéressons à ces 3 causes d'incidents dominantes, nous pouvons observer que : "),
        html.Li("Pour la cause Réseau les incidents sont plus fréquents en Auvergne-Rhône-Alpes, Bourgogne-Franche-Comté, régions Parisiennes et Ile-de-France, Occitanie, Nord-pas-de-Calais et région PACA."),
        html.Li("Pour la cause Mobilité les incidents sont plus fréquents en Auvergne-Rhône-Alpes, Bourgogne-Franche-Comté, Centre-Val de Loire, région Grand-Est, Hauts-de-France, Nouvelle-Aquitaine, et Occitanie."),
        html.Li("Pour la cause Voyageur les incidents sont plus fréquents en Auvergne-Rhône-Alpes, Ile-de-France et Occitanie."),
        html.Br(),
        html.P("Pour conclure, nous avons remarqué 3 causes d'incidents qui sont les plus récurrentes, et en ce qui concerne l'évolution du nombre d'incidents par cause, on observe pas de réelle évolution au cours des années, le nombre d'incidents varie un peu mais reste assez consatant dans l'ensemble pour chaque cause."),
        ], style={'margin-top': '20px', 'font-size': '16px', 'fontSize': '1.25em'})