import matplotlib.pyplot as plt
import seaborn as sns

def barplot_2023(data):

    # Gestion des couleurs
    sns.set_palette("husl")

    ax = data.plot(kind='bar', figsize=(12, 8))
    ax.set_xlabel('Région')
    ax.set_ylabel('Gravité Moyenne')
    ax.set_title('Gravité Moyenne des 5 Principaux Types d\'Incidents dans les 5 Principales Régions')

    ax.legend(title='Type d\'Incident', bbox_to_anchor=(1, 1), loc='upper left')

    plt.show()