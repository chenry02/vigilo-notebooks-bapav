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

hm_map = folium.Map(location=center, zoom_start=12)

for cat in categories:
    data = list(zip(df[df.categorie == cat].coordinates_lat, df[df.categorie == cat].coordinates_lon))
    hm = folium.plugins.HeatMap(data=data,
                                name=categories[cat],
                                min_opacity=0.5,
                                max_val=10,
                                radius=10,
                                blur=10,
                                max_zoom=1,
                                overlay=True,
                                control=True,
                                show=True)
    hm_map.add_child(hm)

folium.LayerControl().add_to(hm_map)

hm_map.save(r"C:\Users\Gustave\Desktop\heatmap.html")
