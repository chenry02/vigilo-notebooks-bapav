import requests
import pandas as pd
import folium
import folium.plugins

# Getting data
resp = requests.get('https://vigilo.jesuisundesdeux.org/get_issues.php')
df = pd.DataFrame(resp.json())
df.time = pd.to_datetime(df.time, unit='s')
df.coordinates_lat = pd.to_numeric(df.coordinates_lat)
df.coordinates_lon = pd.to_numeric(df.coordinates_lon)

resp = requests.get('https://vigilo.jesuisundesdeux.org/get_categories.php')
categories = resp.json()

center = [df.coordinates_lat.mean(), df.coordinates_lon.mean()]

hm_map = folium.Map(location=center, zoom_start=13)

red_gradient = {0.2: 'gold', 0.7: 'orange', 1: 'red'}
blue_gradient = {0.2: 'deeppink', 0.7: 'purple', 1: 'blue'}

for cat in categories:
    data = list(zip(df[df.categorie == cat].coordinates_lat, df[df.categorie == cat].coordinates_lon))

    hm = folium.plugins.HeatMap(data=data,
                                name=categories[cat],
                                min_opacity=0.7,
                                max_val=5,
                                radius=8,
                                blur=5,
                                max_zoom=18,
                                overlay=True,
                                control=True,
                                gradient=red_gradient if cat in ('2', '7') else blue_gradient,
                                show=True if cat == '2' else False)
    hm_map.add_child(hm)

folium.LayerControl().add_to(hm_map)

hm_map.save("./heatmap.html")
