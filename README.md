# PROJET DE VISUALISATION ANALYTIQUE-MASTER 1

Bienvenue sur notre projet de visualisation analytique de master 1. Ce projet se portera sur l'étude des incidents de la SNCF entre 2015 et 2023.

### Base de données :

Utilisation de [Mongodb](hhttps://www.mongodb.com/fr-fr?utm_source=google&utm_campaign=search_gs_pl_evergreen_atlas_core_prosp-brand_gic-null_emea-fr_ps-all_desktop_fr_lead&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=p&utm_ad_campaign_id=20378068742&adgroup=154980288401&cq_cmp=20378068742&gad_source=1&gclid=Cj0KCQiAnfmsBhDfARIsAM7MKi2ujmjZBeZa1JV3HmlN5dzynEqpp4X-tKcM1gvnhnrEKFHWkFXRmVMaAnOYEALw_wcB) pour la récupération des données.

Pour une expérience plus agréable, nous conseillons l'installation de [MongoDB Compass](https://www.mongodb.com/products/tools/compass) pour la lecture des données.

### Python : 

[__Python (3.10.4)__](https://www.python.org) est un langage de programmation polyvalent qui est célèbre pour sa lisibilité et sa facilité d'utilisation. Il possède une grande bibliothèque standard et prend en charge plusieurs paradigmes de programmation.

### Extensions : 

- __Pandas (1.5.3)__ est une bibliothèque de manipulation et d'analyse de données puissante pour Python. Elle facilite le travail avec des données structurées en fournissant des structures de données telles que Series et DataFrame. Pandas est largement utilisé pour nettoyer, explorer et analyser des données.

- __Dash (2.13.0)__ est un framework Python efficace pour créer des applications web. Il est idéal pour les tableaux de bord interactifs et pilotés par les données. Dash vous permet de créer des applications web en utilisant Python, éliminant ainsi la nécessité de connaissances en HTML, CSS ou JavaScript.

- __Plotly (5.18.0)__ est une bibliothèque de création de graphiques qui vous permet de créer des graphiques qui sont interactifs et faciles à partager. Elle peut être utilisée en ligne et hors ligne et prend en charge un large éventail de types de graphiques. Dash crée des visualisations interactives pour ses applications web avec Plotly.

- __Pymongo (4.5.0)__ est un pilote Python pour la base de données NoSQL MongoDB. Les applications Python peuvent interagir avec les bases de données MongoDB, ce qui simplifie le stockage et la récupération des données. MongoDB est célèbre pour sa capacité à être scalable, à être flexible et à stocker des documents de type JSON.

### Version de chaque extension utilisée pour le projet : 

```bash
Python Version: 3.11.4
Pandas Version: 1.5.3
Dash Version: 2.13.0
Plotly Version: 5.18.0
Pymongo Version: 4.5.0
```

### Installation : 

Pour obtenir toutes les extensions utilisées dans ce projet, veuillez exécuter cette commande : 

```bash 
pip install -r requirements.txt
```

### Mise en place de la base de données : 

Une fois MongoDB et MongoDB Compass installés, vous pouvez télécharger les données se trouvant dans ```database.py```. 
La [base de données de la météo](https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/table/?sort=date&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQVZHIiwieUF4aXMiOiJ0YyIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiNGRjUxNUEifV0sInhBeGlzIjoiZGF0ZSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6ImRheSIsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImRvbm5lZXMtc3lub3AtZXNzZW50aWVsbGVzLW9tbSIsIm9wdGlvbnMiOnt9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D
) étant très volumineuse, cette opération risque de prendre plusieurs heures.

### Lancement de l'app : 

Une fois que les données ont été récupérées, vous pouvez lancer directement l'app : 

```bash 
python app.py
```

### Les différentes API : 

Pour notre projet, nous utilisons 5 API, 4 provenant des données de la SNCF et la dernière provenant du site OpenDataSoft et contenant les observations météorologiques historiques en France.

- [Incidents de sécurité (Evénements de sécurité remarquables - ESR) de janvier 2015 à décembre 2022](https://data.sncf.com/explore/dataset/incidents-securite/table/?sort=date)


- [Incidents de sécurité (EPSF) depuis janvier 2023](https://data.sncf.com/explore/dataset/incidents-de-securite-epsf/table/?sort=date&calendarview=month&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoiZ3Jhdml0ZV9lcHNmIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoiI0ExMDA2QiJ9XSwieEF4aXMiOiJkYXRlIiwibWF4cG9pbnRzIjoiIiwidGltZXNjYWxlIjoibW9udGgiLCJzb3J0IjoiIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJpbmNpZGVudHMtZGUtc2VjdXJpdGUtZXBzZiIsIm9wdGlvbnMiOnsic29ydCI6ImRhdGUifX19XSwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZSwidGltZXNjYWxlIjoiIn0%3D)

- [Liste des lignes électrifiées](https://data.sncf.com/explore/dataset/liste-des-lignes-electrifiees/table/)

- [Lignes par type](https://data.sncf.com/explore/dataset/lignes-par-type/table/)

- [Lignes par région administrative](https://data.sncf.com/explore/dataset/lignes-par-region-administrative/table/)

- [observation météorologique historiques en France (SYNOP)](https://public.opendatasoft.com/explore/dataset/donnees-synop-essentielles-omm/table/?sort=date&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQVZHIiwieUF4aXMiOiJ0YyIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlLCJjb2xvciI6IiNGRjUxNUEifV0sInhBeGlzIjoiZGF0ZSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6ImRheSIsInNvcnQiOiIiLCJjb25maWciOnsiZGF0YXNldCI6ImRvbm5lZXMtc3lub3AtZXNzZW50aWVsbGVzLW9tbSIsIm9wdGlvbnMiOnt9fX1dLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D)

### Contributeurs  : 

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/suhailaabarkan">
        <img src="https://avatars.githubusercontent.com/u/102798630?v=4" width="50" height="50" alt=""/><br />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/douniamouchrif">
        <img src="https://avatars.githubusercontent.com/u/102798610?v=4" width="50" height="50" alt=""/><br />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/k-roman5">
        <img src="https://avatars.githubusercontent.com/u/102798439?v=4" width="50" height="50" alt=""/><br />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/mathildetissandier">
        <img src="hhttps://avatars.githubusercontent.com/u/102798509?v=4" width="50" height="50" alt=""/><br />
      </a>
    </td>
  </tr>
</table>




