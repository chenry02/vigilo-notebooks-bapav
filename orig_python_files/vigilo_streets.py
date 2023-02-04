import textwrap

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

MIN_COUNT = 5  # Minimum number of observation per street

# Getting data
resp = requests.get('https://vigilo.jesuisundesdeux.org/get_issues.php')
df = pd.DataFrame(resp.json())

resp = requests.get('https://vigilo.jesuisundesdeux.org/get_categories.php')
cat = resp.json()
cat['2'] = cat['2'].replace(' (gcum)', '')

df.address = df.address.apply(lambda x: x.split(',')[0])
df.address = df.address.apply(lambda x: x.replace('Avenue', 'Av.').
                              replace('Boulevard', 'Bd.').
                              replace('Professeur', 'Pr.').
                              replace('Faubourg', 'Fb.').
                              replace('Gabriel Buchet', ''))
df = df.replace({'categorie': cat})

streets = df.groupby(by='address').token.count()
streets = streets.sort_values(ascending=False)

df.address = df.address.apply(lambda x: x if streets[x] > MIN_COUNT else 'Autre')

categories = df.groupby(by='categorie').token.count()
categories = categories.sort_values(ascending=False)

tab = pd.crosstab(df.address, df.categorie, margins=True, margins_name='Total')
tab = tab.sort_values(by='Total', ascending=False)

cols = list(tab)
cols.remove('Autre')
cols.remove('Total')
cols.append('Autre')
cols.append('Total')

rows = list(tab.index)
rows.remove('Autre')
rows.remove('Total')
rows.append('Autre')
rows.append('Total')

tab = tab.loc[rows, cols]

fig, ax = plt.subplots(figsize=(8, 8))
sns.heatmap(tab, annot=tab.applymap(lambda x: '' if x == 0 else str(x)),
            cbar=False, fmt='s', ax=ax, cmap="YlGnBu", vmin=0, vmax=50)

plt.ylabel('')
plt.xlabel('')
# plt.xticks(rotation=70)

plt.title("Principales localisations des observations de Vǐgǐlo")

plt.tight_layout()
plt.show()

a = 0
