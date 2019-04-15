import textwrap
import datetime

import requests
import overpy
import geopy.distance
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("darkgrid")
sns.set_context("talk", font_scale=0.8)
sns.set_color_codes("pastel")

BUFFER_SIZE = 150  # Max distance between schools and GCUM in m

# Getting GCUM data
resp = requests.get('https://vigilo.jesuisundesdeux.org/get_issues.php?c=2')
gcum = resp.json()

# Getting schools
api = overpy.Overpass()
bbox = '43.517, 3.777, 43.685, 4.035'
query = """(
  node["school:FR"="maternelle"]({bbox});
  way["school:FR"="maternelle"]({bbox});
  node["school:FR"="élémentaire"]({bbox});
  way["school:FR"="élémentaire"]({bbox});
  node["school:FR"="primaire"]({bbox});
  way["school:FR"="primaire"]({bbox});
  );
  out center;""".format(bbox=bbox)

result = api.query(query)

schools = [{'name': x.tags['name'], 'lat': float(x.lat), 'lon': float(x.lon)} for x in result.nodes] + \
          [{'name': x.tags['name'], 'lat': float(x.center_lat), 'lon': float(x.center_lon)} for x in result.ways]

# Counting GCUM within X meters of schools

# Filtering gcum on day and time
week_gcum = [x for x in gcum
             if datetime.datetime.fromtimestamp(int(x['time'])).weekday() < 4
             and (datetime.time(hour=7, minute=30) < datetime.datetime.fromtimestamp(
        int(x['time'])).time() < datetime.time(hour=9)
                  or datetime.time(hour=16) < datetime.datetime.fromtimestamp(int(x['time'])).time() < datetime.time(
                hour=17, minute=30))]

near_school_gcum = set()
for school in schools:
    school['gcum'] = [x for x in week_gcum if (geopy.distance.great_circle((x['coordinates_lat'], x['coordinates_lon']),
                                                                           (school['lat'],
                                                                            school['lon'])).meters < BUFFER_SIZE)]
    school['nb_gcum'] = len(school['gcum'])
    near_school_gcum.update([x['token'] for x in school['gcum']])

schools.sort(key=lambda x: len(x['gcum']), reverse=True)

print('\n'.join(['{} - {}'.format(x['nb_gcum'], x['name']) for x in schools if x['nb_gcum'] != 0]))

fig, ax = plt.subplots(figsize=(6, 7))

sns.barplot(x=[x['nb_gcum'] for x in schools[:10]],
            y=['\n'.join(textwrap.wrap(x['name'], 25)) for x in schools[:10]],
            color="b",
            ax=ax)

plt.title("Classement des écoles de Montpellier\npar nombre de stationnement gênant\nà proximité (moins de {} m)".format(BUFFER_SIZE))

plt.tight_layout()
plt.show()

df = pd.DataFrame(gcum)
df.time = pd.to_datetime(df.time, unit='s')
df['hour'] = 'Journée et weekend'
df.loc[df.token.apply(lambda x: x in [y['token'] for y in week_gcum]), 'hour'] = "Horaires d'école"

# Separating obs near schools
df["school"] = 'Non'

for school in schools:
    df.loc[df.apply(lambda row: geopy.distance.great_circle((row['coordinates_lat'], row['coordinates_lon']),
                                                            (school['lat'],
                                                             school['lon'])).meters < BUFFER_SIZE,
                    axis=1), "school"] = 'Oui'

fig, ax = plt.subplots(figsize=(5, 5))

size = 0.3
cmap = plt.get_cmap("tab20c")
outer_colors = cmap([2, 5])
inner_colors = cmap([1, 4])

ax.pie(x=(df[df.hour == 'Journée et weekend'][df.school == 'Non'].token.count(),
          df[df.hour == 'Journée et weekend'][df.school == 'Oui'].token.count()),
       radius=1,
       wedgeprops=dict(width=size, edgecolor='w'),
       startangle=90,
       colors=outer_colors)
ax.pie(x=(df[df.hour == "Horaires d'école"][df.school == 'Non'].token.count(),
          df[df.hour == "Horaires d'école"][df.school == 'Oui'].token.count()),
       radius=1 - size,
       wedgeprops=dict(width=size, edgecolor='w'),
       startangle=90,
       colors=inner_colors)

plt.title("Localisation des stationnements gênants\nselon l'heure de la journée")

ax.annotate("Horaires d'école",
            xy=(0.5, 0.31),
            xycoords='axes fraction',
            fontweight='bold',
            verticalalignment='top',
            horizontalalignment='center')

ax.annotate("Journée et weekend",
            xy=(0.5, 0.19),
            xycoords='axes fraction',
            fontweight='bold',
            verticalalignment='top',
            horizontalalignment='center')

legend = ax.legend(title="Proximité\nd'une école", labels=("Non", "Oui"), handlelength=0, handletextpad=-0.5)

for n, text in enumerate(legend.texts):
    print(n, text)
    text.set_color(inner_colors[n])
    text.set_fontweight('bold')

plt.tight_layout()

plt.show()
