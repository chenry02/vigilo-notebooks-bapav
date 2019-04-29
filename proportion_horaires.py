import math

import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches

# Getting data
resp = requests.get('https://vigilo.jesuisundesdeux.org/get_issues.php')
df = pd.DataFrame(resp.json())
df.time = pd.to_datetime(df.time, unit='s')
df['daytype'] = 'Semaine'
df.loc[df.time.dt.weekday > 4, 'daytype'] = 'Weekend'

resp = requests.get('https://vigilo.jesuisundesdeux.org/get_categories.php')
cat_names = resp.json()

colors = plt.get_cmap('tab10').colors
cat_color = {cat[0]: colors[x] for x, cat in
             enumerate(df.groupby(by='categorie').token.count().sort_values(ascending=False).iteritems())}

hours = range(5, 22)

fig, axs = plt.subplots(2, len(hours), figsize=(18, 4))

for row, daytype in enumerate(('Semaine', 'Weekend')):
    for col, hour in enumerate(hours):
        if hour == min(hours):
            data = df[(df.daytype == daytype) & (df.time.dt.hour <= hour)].groupby(
                by='categorie').token.count().sort_values(ascending=False)
            label = 'Avant {}h'.format(hour+1)
        elif hour == max(hours):
            data = df[(df.daytype == daytype) & (df.time.dt.hour >= hour)].groupby(
                by='categorie').token.count().sort_values(ascending=False)
            label = 'Après {}h'.format(hour-1)
        else:
            data = df[(df.daytype == daytype) & (df.time.dt.hour == hour)].groupby(
                by='categorie').token.count().sort_values(ascending=False)
            label = '{}h'.format(hour)
        colors = [cat_color[x] for x in data.index]
        data.plot.pie(ax=axs[row][col],
                      y='token',
                      labels=None,
                      legend=None,
                      colors=colors,
                      radius=math.sqrt(data.sum()) / 6,
                      startangle=90,
                      counterclock=False)
        if col == 0:
            axs[row][col].set_ylabel(daytype)
        else:
            axs[row][col].set_ylabel('')
        if row == 1:
            axs[row][col].set_title(label)

fig.legend(handles=[matplotlib.patches.Patch(facecolor=col, label=cat_names[cat]) for cat, col in cat_color.items()],
           bbox_to_anchor=(0.75, 0.2), ncol=3, frameon=False)

fig.suptitle("Proportion des observations de Vǐgǐlo par catégorie et par heure", size=16)
plt.tight_layout()
plt.show()
