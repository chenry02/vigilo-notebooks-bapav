import datetime

import requests
import pandas as pd
import folium
import folium.plugins

TIME_DELTA = 2  # Size of the time window between animations
ANIMATION_START = datetime.datetime(year=2019, month=1, day=1)  # Set to None to get all obs
SHOW_OBS_BEFORE_ANIMATION_START = False

# Getting data
resp = requests.get('https://vigilo.jesuisundesdeux.org/get_issues.php')
df = pd.DataFrame(resp.json())
df.time = pd.to_datetime(df.time, unit='s')
if (ANIMATION_START is not None) and not SHOW_OBS_BEFORE_ANIMATION_START:
    df = df[df.time > ANIMATION_START]
df.coordinates_lat = pd.to_numeric(df.coordinates_lat)
df.coordinates_lon = pd.to_numeric(df.coordinates_lon)

resp = requests.get('https://vigilo.jesuisundesdeux.org/get_categories.php')
categories = resp.json()

center = [df.coordinates_lat.mean(), df.coordinates_lon.mean()]

hm_map = folium.Map(location=center, zoom_start=13)


def perdelta():
    curr = ANIMATION_START or df.time.min()
    while curr < df.time.max():
        yield curr
        curr += datetime.timedelta(days=TIME_DELTA)


data = [[[x[1].coordinates_lat, x[1].coordinates_lon] for x in df[(df.time < t)].iterrows()] for t in perdelta()]

hm = folium.plugins.HeatMapWithTime(data=data,
                                    index=[x.strftime('%Y-%m-%d') for x in perdelta()],
                                    min_opacity=0.5,
                                    max_opacity=0.9,
                                    use_local_extrema=False,
                                    radius=10,
                                    auto_play=True,
                                    min_speed=1,
                                    overlay=True,
                                    control=True,
                                    show=True)
hm_map.add_child(hm)

hm_map.save("./heatmap_with_time.html")
