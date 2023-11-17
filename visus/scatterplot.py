import plotly.express as px
from itertools import groupby
from datetime import datetime
# import database.database


def get_data():
    result = db.sncf23.find({
        'gravite_epsf': {'$ne': None},
        'date': {'$gte': '2023-01-01', '$lte': '2023-08-31'}
    }, {'gravite_epsf': 1, 'date': 1})
    data = list(result)

    grouped_data = {k: {'gravités': [x['gravite_epsf'] for x in g]}
                    for k, g in groupby(sorted(data, key=lambda x: x['date'][:7]), key=lambda x: x['date'][:7])}
    for month, values in grouped_data.items():
        values['gravite_moyenne'] = sum(
            values['gravités']) / len(values['gravités'])
    return grouped_data


data = get_data()
df = []
for month, values in data.items():
    df.append({'Mois': datetime.strptime(month, '%Y-%m'),
               'Gravité moyenne': values['gravite_moyenne']})

fig = px.scatter(df, x='Mois', y='Gravité moyenne',
                 title='Gravité moyenne par mois', color='Gravité moyenne', size='Gravité moyenne')
fig.show()
