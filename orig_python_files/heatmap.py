import os
import math
import datetime
import locale

import pandas as pd
import requests
import numpy as np
import scipy.ndimage
import tilemapbase
from tilemapbase import Extent
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.animation
import matplotlib.patheffects

# Setting french locale
locale.setlocale(locale.LC_ALL, 'fr_FR')

RESULT_TYPE = 'Animation'
# RESULT_TYPE = 'Image'

EXPORT_RESULT = True
EXPORT_FOLDER = './'
# ANIMATION_EXPORT_FORMAT = 'gif'  # Needs ImageMagick installed
ANIMATION_EXPORT_FORMAT = 'mp4'

ASPECT_RATIO = 4 / 3
WIDTH = 12

VMAX = 0.01  # For heatmap stretching
VMIN = 0.0001
BUFFER_SIZE = 10  # Heatmap buffer size
NBINS = 3000  # Heatmap resolution

COLORMAP = 'plasma'  # Heatmap colormap  https://matplotlib.org/users/colormaps.html
REVERSE_COLORMAP = False
COLORMAP_CUT = 0.  # [0,1] For cutting the lower values of the colormap
MIN_ALPHA = 0.1  # Heatmap transparency
MAX_ALPHA = 1

ZOOM_LEVEL = 14  # OSM zoom level
# Xmin, Xmax, Ymin, Ymax   If None, the extent is set automatically according to EXCLUDE_DATA_THRESHOLD
EXTENT = None
EXCLUDE_DATA_THRESHOLD = 3  # in % of data excluded from bounding box
BACKGROUND_SHADING = 0.1

TIME_STEP = 1  # Step for the animation in days
START_DATE = datetime.date(year=2019, month=1, day=1)  # Set to None to begin with first observation
END_DATE = None  # Set to None to end with last observation
FRAME_INTERVAL = 100  # in ms

TEXT_COLOR = 'Black'
TEXT_BUFFER = 4
TEXT_BUFFER_COLOR = '#ececec'

TITLE = "Observations de Vǐgǐlo à Montpellier"
X_TITLE = 0.5
Y_TITLE = 0.95
TITLE_SIZE = 20

DATE_SIZE = 15
X_DATE = 0.01
Y_DATE = 0.05
DATE_HALIGNMENT = 'left'

NB_OBS_SIZE = 15
X_NB_OBS = 0.01
Y_NB_OBS = 0.01
NB_OBS_HALIGNMENT = 'left'

LICENSE_INFO = "Vélocité Montpellier\nOpenStreetMap contributors"
LICENSE_SIZE = 8
X_LICENSE = 0.995
Y_LICENSE = 0.01
LICENSE_HALIGNMENT = 'right'

# Getting data
resp = requests.get('https://vigilo.jesuisundesdeux.org/get_issues.php')
df = pd.DataFrame(resp.json())
df.time = pd.to_datetime(df.time, unit='s')
df.coordinates_lat = pd.to_numeric(df.coordinates_lat)
df.coordinates_lon = pd.to_numeric(df.coordinates_lon)

# Getting OSM Background
tilemapbase.start_logging()
# tilemapbase.init(create=True)  # Run this on first time
t = tilemapbase.tiles.OSM


class CustomExtent(Extent):
    def _to_aspect(self, aspect):
        """ Overriding this class to resize by augmenting and not shrinking"""
        width = self._xmax - self._xmin
        height = self._ymax - self._ymin
        if width < (height * aspect):
            width = height * aspect
        elif height < (width / aspect):
            height = width / aspect
        midx = (self._xmin + self._xmax) / 2
        midy = (self._ymin + self._ymax) / 2
        return (midx - width / 2, midx + width / 2,
                midy - height / 2, midy + height / 2)

    @staticmethod
    def from_lonlat(longitude_min, longitude_max, latitude_min, latitude_max):
        """Construct a new instance from longitude/latitude space."""
        xmin, ymin = tilemapbase.project(longitude_min, latitude_max)
        xmax, ymax = tilemapbase.project(longitude_max, latitude_min)
        return CustomExtent(xmin, xmax, ymin, ymax)

if EXTENT:
    extent = EXTENT
else:
    extent = list(np.percentile(df.coordinates_lon, (EXCLUDE_DATA_THRESHOLD, 100 - EXCLUDE_DATA_THRESHOLD))) + \
             list(np.percentile(df.coordinates_lat, (EXCLUDE_DATA_THRESHOLD, 100 - EXCLUDE_DATA_THRESHOLD)))

map_extent = CustomExtent.from_lonlat(*extent)
map_extent = map_extent.to_aspect(ASPECT_RATIO)

# Reprojecting extant
extent = [map_extent.xmin, map_extent.xmax, map_extent.ymin, map_extent.ymax]

# Reprojecting coordinates
df.coordinates_lon = df.coordinates_lon.apply(lambda x: tilemapbase.project(x, 0)[0])
df.coordinates_lat = df.coordinates_lat.apply(lambda x: tilemapbase.project(0, x)[1])

# Editing colormap
ref_cm = plt.get_cmap(COLORMAP)
if REVERSE_COLORMAP:
    ref_cm = ref_cm.reversed()
# Giving colormap a gradual alpha
color_list = ref_cm(np.arange(ref_cm.N))
color_list = color_list[math.floor(len(color_list) * COLORMAP_CUT):, ]
color_list[:, -1] = [MAX_ALPHA * (MIN_ALPHA + (math.log(1 + x, len(color_list)) * (1 - MIN_ALPHA))) for x in
                     range(0, len(color_list))]  # Log distribution of alpha
cm = matplotlib.colors.ListedColormap(color_list)
cm.set_under(alpha=0)

# Initializing figure
fig, ax = plt.subplots(figsize=(WIDTH, WIDTH / ASPECT_RATIO))
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Plotting map background
plotter = tilemapbase.Plotter(map_extent, t, zoom=ZOOM_LEVEL)
plotter.plot(ax, t)
shading = np.zeros((1, 1), dtype='float')
ax.imshow(shading, extent=extent, origin='lower', cmap='gray', alpha=BACKGROUND_SHADING)

# Plotting title
ax.text(s=TITLE, x=X_TITLE, y=Y_TITLE, size=TITLE_SIZE,
        transform=ax.transAxes,
        horizontalalignment='center',
        color=TEXT_COLOR,
        path_effects=[matplotlib.patheffects.withStroke(linewidth=TEXT_BUFFER, foreground=TEXT_BUFFER_COLOR)],
        zorder=10)

# Plotting license
ax.text(s=LICENSE_INFO, x=X_LICENSE, y=Y_LICENSE,
        horizontalalignment=LICENSE_HALIGNMENT, transform=ax.transAxes, size=LICENSE_SIZE, color=TEXT_COLOR,
        path_effects=[matplotlib.patheffects.withStroke(linewidth=TEXT_BUFFER, foreground=TEXT_BUFFER_COLOR)],
        zorder=11)


def heatmap(x, y, s, bins=1000):
    hm, xedges, yedges = np.histogram2d(x, y, bins=[bins, math.floor(bins / ASPECT_RATIO)],
                                        range=[[extent[0], extent[1]], [extent[2], extent[3]]])
    hm = scipy.ndimage.gaussian_filter(hm, sigma=s)

    return hm.T


if RESULT_TYPE == 'Image':
    img = heatmap(df.coordinates_lon, df.coordinates_lat, BUFFER_SIZE, bins=NBINS)
    ax.imshow(img, extent=extent, origin='lower', cmap=cm, vmin=VMIN, vmax=VMAX)

    ax.text(s=datetime.datetime.now().strftime('%d %B %Y'), x=X_DATE, y=Y_DATE,
            horizontalalignment=DATE_HALIGNMENT, transform=ax.transAxes, size=DATE_SIZE, color=TEXT_COLOR,
            path_effects=[matplotlib.patheffects.withStroke(linewidth=TEXT_BUFFER, foreground=TEXT_BUFFER_COLOR)])

    ax.text(s='{0:n} observations'.format(df.shape[0]), x=X_NB_OBS, y=Y_NB_OBS,
            horizontalalignment=NB_OBS_HALIGNMENT, transform=ax.transAxes, size=NB_OBS_SIZE, color=TEXT_COLOR,
            path_effects=[matplotlib.patheffects.withStroke(linewidth=TEXT_BUFFER, foreground=TEXT_BUFFER_COLOR)])

elif RESULT_TYPE == 'Animation':
    img = np.zeros((1, 1), dtype='float')
    heatmap_img = ax.imshow(img, extent=extent, origin='lower', cmap=cm, vmin=VMIN, vmax=VMAX, animated=True)
    date_text = ax.text(s='', x=X_DATE, y=Y_DATE,
                        horizontalalignment=DATE_HALIGNMENT, transform=ax.transAxes, size=DATE_SIZE, color=TEXT_COLOR,
                        path_effects=[matplotlib.patheffects.withStroke(linewidth=TEXT_BUFFER,
                                                                        foreground=TEXT_BUFFER_COLOR)])
    nb_obs_text = ax.text(s='', x=X_NB_OBS, y=Y_NB_OBS,
                          horizontalalignment=NB_OBS_HALIGNMENT, transform=ax.transAxes, size=NB_OBS_SIZE,
                          color=TEXT_COLOR,
                          path_effects=[matplotlib.patheffects.withStroke(linewidth=TEXT_BUFFER,
                                                                          foreground=TEXT_BUFFER_COLOR)])


    def update(date):
        data = df[df.time <= date]
        img = heatmap(data.coordinates_lon, data.coordinates_lat, BUFFER_SIZE, bins=NBINS)
        heatmap_img.set_array(img)
        date_text.set_text(date.strftime('%d %B %Y'))
        nb_obs_text.set_text('{0:n} observations'.format(data.shape[0]))
        return heatmap_img, date_text, nb_obs_text


    dates = pd.date_range(start=START_DATE or df.time.min().date(),
                          end=END_DATE or df.time.max().date(),
                          freq=str(TIME_STEP) + 'D').tolist()
    anim = matplotlib.animation.FuncAnimation(fig, update, blit=True, frames=dates, interval=FRAME_INTERVAL)

if EXPORT_RESULT:
    if RESULT_TYPE == 'Animation':
        if ANIMATION_EXPORT_FORMAT == 'mp4':
            anim.save(os.path.join(EXPORT_FOLDER, 'heatmap.mp4'))
        elif ANIMATION_EXPORT_FORMAT == 'gif':
            anim.save(os.path.join(EXPORT_FOLDER, 'heatmap.gif'), writer='imagemagick', fps=60)
    elif RESULT_TYPE == 'Image':
        plt.savefig(os.path.join(EXPORT_FOLDER, 'heatmap.png'))
else:
    plt.show()
