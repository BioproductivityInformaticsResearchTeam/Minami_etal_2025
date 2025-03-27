#Python
#Python 3.9.13

#install related libraries
#pip install matplotlib cartopy
#pip install cartopy

#import related libraries
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

##Bd21-3-type accessions (97)
data = [
("Bd21-3", 33 + 45/60 + 39.18/3600, 44 + 24/60 + 11.07/3600),
("Bd18-1", 39 + 22/60 + 4.25/3600, 33 + 43/60 + 48.91/3600),
    ("Adi-1", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-2", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-3", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-4", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-5", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-6", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-7", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-8", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-9", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-10", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-11", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-12", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-13", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-14", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-15", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-16", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-17", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-18", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Bis-1", 37 + 52/60 + 35.6/3600, 41 + 0/60 + 54.3/3600),
    ("Gaz-2", 37 + 7/60 + 39.8/3600, 37 + 23/60 + 26.9/3600),
    ("Gaz-4", 37 + 7/60 + 39.8/3600, 37 + 23/60 + 26.9/3600),
    ("Gaz-7", 37 + 7/60 + 39.8/3600, 37 + 23/60 + 26.9/3600),
    ("Gaz-9", 37 + 7/60 + 39.8/3600, 37 + 23/60 + 26.9/3600),
    ("Kah-2", 37 + 44/60 + 2.3/3600, 38 + 32/60 + 0.2/3600),
    ("Kah-3", 37 + 44/60 + 2.3/3600, 38 + 32/60 + 0.2/3600),
    ("Kah-5", 37 + 44/60 + 2.3/3600, 38 + 32/60 + 0.2/3600),
    ("Kah-6", 37 + 44/60 + 2.3/3600, 38 + 32/60 + 0.2/3600),
    ("Koz-1", 38 + 9/60 + 8.2/3600, 41 + 36/60 + 34.8/3600),
    ("Koz-2", 38 + 9/60 + 8.2/3600, 41 + 36/60 + 34.8/3600),
    ("Koz-4", 38 + 9/60 + 8.2/3600, 41 + 36/60 + 34.8/3600),
    ("Tek-1", 41 + 0/60 + 40.1/3600, 27 + 31/60 + 8.8/3600),
    ("Tek-2", 41 + 0/60 + 40.1/3600, 27 + 31/60 + 8.8/3600),
    ("Tek-3", 41 + 0/60 + 40.1/3600, 27 + 31/60 + 8.8/3600),
    ("Tek-5", 41 + 0/60 + 40.1/3600, 27 + 31/60 + 8.8/3600),
    ("Tek-9", 41 + 0/60 + 40.1/3600, 27 + 31/60 + 8.8/3600),
    ("Tek-10", 41 + 0/60 + 40.1/3600, 27 + 31/60 + 8.8/3600),
    ("BdTR3A", 37 + 46/60 + 4.28/3600, 33 + 31/60 + 10.58/3600),
    ("BdTR3B", 37 + 6/60 + 31.87/3600, 34 + 4/60 + 17.06/3600),
    ("BdTR3D", 40 + 24/60 + 19.91/3600, 34 + 38/60 + 10.10/3600),
    ("BdTR3E", 39 + 44/60 + 53.45/3600, 34 + 39/60 + 1.15/3600),
    ("BdTR3F", 39 + 5/60 + 31.64/3600, 35 + 11/60 + 18.62/3600),
    ("BdTR3H", 37 + 46/60 + 43.23/3600, 35 + 12/60 + 9.55/3600),
    ("BdTR3I", 39 + 44/60 + 51.33/3600, 36 + 48/60 + 56.85/3600),
    ("BdTR3J", 38 + 45/60 + 25.33/3600, 36 + 16/60 + 56.90/3600),
    ("BdTR3K", 38 + 25/60 + 12.10/3600, 37 + 23/60 + 26.99/3600),
    ("BdTR3M", 37 + 45/60 + 58.01/3600, 37 + 53/60 + 23.56/3600),
    ("BdTR3N", 37 + 26/60 + 4.39/3600, 36 + 49/60 + 9.55/3600),
    ("BdTR3O", 37 + 7/60 + 2.52/3600, 39 + 1/60 + 49.56/3600),
    ("BdTR3P", 37 + 45/60 + 41.57/3600, 39 + 34/60 + 56.72/3600),
    ("BdTR3R", 37 + 26/60 + 13.88/3600, 40 + 7/60 + 50.51/3600),
    ("BdTR3S", 38 + 5/60 + 43.50/3600, 40 + 39/60 + 30.84/3600),
    ("BdTR3T", 37 + 27/60 + 31.68/3600, 41 + 14/60 + 39.03/3600),
    ("BdTR5A", 36 + 45/60 + 59.24/3600, 44 + 32/60 + 6.90/3600),
    ("BdTR5B", 37 + 46/60 + 43.23/3600, 35 + 12/60 + 9.55/3600),
    ("BdTR5E", 37 + 46/60 + 41.64/3600, 31 + 53/60 + 5.68/3600),
    ("BdTR5F", 40 + 23/60 + 37.13/3600, 32 + 59/60 + 7.32/3600),
    ("BdTR5G", 39 + 45/60 + 23.35/3600, 32 + 25/60 + 56.46/3600),
    ("BdTR5H", 39 + 45/60 + 16.02/3600, 33 + 32/60 + 16.37/3600),
    ("BdTR5J", 40 + 23/60 + 37.13/3600, 32 + 59/60 + 7.32/3600),
    ("BdTR5K", 40 + 23/60 + 37.13/3600, 32 + 59/60 + 7.32/3600),
    ("BdTR5M", 40 + 23/60 + 37.13/3600, 32 + 59/60 + 7.32/3600),
    ("BdTR5N", 40 + 23/60 + 37.13/3600, 32 + 59/60 + 7.32/3600),
    ("BdTR5O", 39 + 45/60 + 16.02/3600, 33 + 32/60 + 16.37/3600),
    ("BdTR8C", 39 + 24/60 + 46.28/3600, 32 + 59/60 + 17.24/3600),
    ("BdTR8F", 37 + 46/60 + 4.28/3600, 33 + 31/60 + 10.58/3600),
    ("BdTR8M", 39 + 5/60 + 31.64/3600, 35 + 11/60 + 18.62/3600),
    ("BdTR10A", 38 + 25/60 + 46.78/3600, 31 + 18/60 + 33.71/3600),
    ("BdTR10B", 38 + 25/60 + 40.97/3600, 32 + 24/60 + 16.47/3600),
    ("BdTR10D", 40 + 23/60 + 37.13/3600, 32 + 59/60 + 7.32/3600),
    ("BdTR10F", 37 + 45/60 + 41.57/3600, 39 + 34/60 + 56.72/3600),
    ("BdTR10G", 37 + 26/60 + 13.88/3600, 40 + 7/60 + 50.51/3600),
    ("BdTR10H", 38 + 5/60 + 43.50/3600, 40 + 39/60 + 30.84/3600),
    ("BdTR10I", 37 + 27/60 + 31.68/3600, 41 + 14/60 + 39.03/3600),
    ("BdTR10J", 37 + 47/60 + 51.69/3600, 41 + 46/60 + 25.09/3600),
    ("BdTR10K", 38 + 5/60 + 48.94/3600, 42 + 19/60 + 18.79/3600),
    ("BdTR10M", 41 + 25/60 + 17.86/3600, 27 + 28/60 + 36.81/3600),
    ("BdTR10N", 41 + 5/60 + 7.15/3600, 26 + 55/60 + 53.29/3600),
    ("BdTR10O", 39 + 44/60 + 17.39/3600, 28 + 2/60 + 24.71/3600),
    ("BdTR11B", 41 + 25/60 + 17.86/3600, 27 + 28/60 + 36.81/3600),
    ("BdTR11C", 41 + 5/60 + 7.15/3600, 26 + 55/60 + 53.29/3600),
    ("BdTR11D", 37 + 27/60 + 31.68/3600, 41 + 14/60 + 39.03/3600),
    ("BdTR11F", 38 + 5/60 + 48.94/3600, 42 + 19/60 + 18.79/3600),
    ("BdTR11H", 41 + 5/60 + 7.15/3600, 26 + 55/60 + 53.29/3600),
    ("BdTR12A", 36 + 46/60 + 58.92/3600, 32 + 57/60 + 46.71/3600),
    ("BdTR12B", 40 + 24/60 + 19.91/3600, 34 + 38/60 + 10.10/3600),
    ("BdTR13B", 39 + 45/60 + 16.02/3600, 33 + 32/60 + 16.37/3600),
    ("BdTR13D", 37 + 46/60 + 4.28/3600, 33 + 31/60 + 10.58/3600),
    ("BdTR13E", 37 + 6/60 + 31.87/3600, 34 + 4/60 + 17.06/3600),
    ("BdTR13F", 39 + 5/60 + 31.64/3600, 35 + 11/60 + 18.62/3600),
    ("BdTR13G", 38 + 24/60 + 16.86/3600, 35 + 9/60 + 34.32/3600),
    ("BdTR13H", 37 + 27/60 + 31.68/3600, 41 + 14/60 + 39.03/3600),
    ("BdTR13I", 37 + 47/60 + 51.69/3600, 41 + 46/60 + 25.09/3600),
    ("BdTR13J", 38 + 5/60 + 48.94/3600, 42 + 19/60 + 18.79/3600),
    ("BdTR13K", 38 + 5/60 + 48.94/3600, 42 + 19/60 + 18.79/3600),
    ("BdTR13M", 37 + 28/60 + 28.23/3600, 43 + 26/60 + 45.08/3600),
    ("BdTR13N", 36 + 45/60 + 59.24/3600, 44 + 32/60 + 6.90/3600),
    ("BdTR13O", 38 + 5/60 + 48.94/3600, 42 + 19/60 + 18.79/3600),
]

#data
names, latitudes, longitudes = zip(*data)

# map construction
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([25, 50, 30, 50])  # map range

ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.LAKES, edgecolor='black')
ax.add_feature(cfeature.RIVERS)

# plot
sc = ax.scatter(longitudes, latitudes, color='blue', marker='o')


# graph output
plt.title('Bd21-3 in Turkey')
plt.legend()
plt.show()



##Bd21-type accessions (50)

data = [
("Bd21", 33 + 45/60 + 39.18/3600, 44 + 24/60 + 11.07/3600),
("Bd1-1", 39 + 11/60 + 27.44/3600,27+ 36/60 + 28.59/3600),
    ("Adi-10", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Adi-17", 37 + 46/60 + 14.5/3600, 38 + 21/60 + 8.2/3600),
    ("Gaz-1", 37 + 7/60 + 39.8/3600, 37 + 23/60 + 26.9/3600),
    ("Gaz-3", 37 + 7/60 + 39.8/3600, 37 + 23/60 + 26.9/3600),
    ("Gaz-5", 37 + 7/60 + 39.8/3600, 37 + 23/60 + 26.9/3600),
    ("Gaz-6", 37 + 7/60 + 39.8/3600, 37 + 23/60 + 26.9/3600),
    ("Gaz-8", 37 + 7/60 + 39.8/3600, 37 + 23/60 + 26.9/3600),
    ("Kah-1", 37 + 44/60 + 2.3/3600, 38 + 32/60 + 0.2/3600),
    ("Kah-4", 37 + 44/60 + 2.3/3600, 38 + 32/60 + 0.2/3600),
    ("Koz-3", 38 + 9/60 + 8.26/3600, 41 + 36/60 + 34.8/3600),
    ("Koz-5", 38 + 9/60 + 8.26/3600, 41 + 36/60 + 34.8/3600),
    ("Tek-4", 41 + 0/60 + 40.1/3600, 27 + 31/60 + 8.8/3600),
    ("Tek-6", 41 + 0/60 + 40.1/3600, 27 + 31/60 + 8.8/3600),
    ("Tek-7", 41 + 0/60 + 40.1/3600, 27 + 31/60 + 8.8/3600),
    ("Tek-8", 41 + 0/60 + 40.1/3600, 27 + 31/60 + 8.8/3600),
    ("Tek-12", 41 + 0/60 + 40.1/3600, 27 + 31/60 + 8.8/3600),
    ("BdTR1B", 41 + 5/60 + 7.15/3600, 26 + 55/60 + 53.29/3600),
    ("BdTR1C", 39 + 44/60 + 17.39/3600, 28 + 2/60 + 24.71/3600),
    ("BdTR1D", 38 + 45/60 + 50.79/3600, 28 + 35/60 + 6.42/3600),
    ("BdTR1E", 38 + 25/60 + 0.42/3600, 28 + 1/60 + 52.75/3600),
    ("BdTR1F", 41 + 25/60 + 17.86/3600, 27 + 28/60 + 36.81/3600),
    ("BdTR1G", 41 + 5/60 + 7.15/3600, 26 + 55/60 + 53.29/3600),
    ("BdTR1H", 39 + 44/60 + 17.39/3600, 28 + 2/60 + 24.71/3600),
    ("BdTR1I", 38 + 5/60 + 35.03/3600, 28 + 34/60 + 59.02/3600),
    ("BdTR1J", 37 + 25/60 + 38.24/3600, 28 + 35/60 + 6.75/3600),
    ("BdTR1K", 39 + 45/60 + 34.18/3600, 29 + 40/60 + 40.96/3600),
    ("BdTR1M", 39 + 5/60 + 12.20/3600, 30 + 15/60 + 8.93/3600),
    ("BdTR1N", 38 + 5/60 + 59.53/3600, 30 + 14/60 + 44.11/3600),
    ("BdTR2A", 39 + 45/60 + 10.62/3600, 30 + 47/60 + 19.07/3600),
    ("BdTR2C", 39 + 5/60 + 8.89/3600, 31 + 53/60 + 29.40/3600),
    ("BdTR2D", 38 + 25/60 + 46.78/3600, 31 + 18/60 + 33.71/3600),
    ("BdTR2E", 38 + 25/60 + 40.97/3600, 32 + 24/60 + 16.47/3600),
    ("BdTR2F", 37 + 46/60 + 41.64/3600, 31 + 53/60 + 5.68/3600),
    ("BdTR2G", 40 + 23/60 + 37.13/3600, 32 + 59/60 + 7.32/3600),
    ("BdTR2H", 39 + 45/60 + 23.35/3600, 32 + 25/60 + 56.46/3600),
    ("BdTR2I", 39 + 45/60 + 16.02/3600, 33 + 32/60 + 16.37/3600),
    ("BdTR2J", 39 + 24/60 + 46.28/3600, 32 + 59/60 + 17.24/3600),
    ("BdTR2K", 38 + 45/60 + 28.75/3600, 34 + 4/60 + 18.34/3600),
    ("BdTR2M", 38 + 5/60 + 52.78/3600, 34 + 5/60 + 40.38/3600),
    ("BdTR2N", 37 + 46/60 + 4.28/3600, 33 + 31/60 + 10.58/3600),
    ("BdTR2O", 39 + 45/60 + 23.35/3600, 32 + 25/60 + 56.46/3600),
    ("BdTR2P", 39 + 45/60 + 16.02/3600, 33 + 32/60 + 16.37/3600),
    ("BdTR2R", 39 + 24/60 + 46.28/3600, 32 + 59/60 + 17.24/3600),
    ("BdTR2S", 38 + 45/60 + 28.75/3600, 34 + 4/60 + 18.34/3600),
    ("BdTR9A", 39 + 44/60 + 51.33/3600, 36 + 48/60 + 56.85/3600),
    ("BdTR9B", 39 + 44/60 + 17.39/3600, 28 + 2/60 + 24.71/3600),
    ("BdTR9F", 37 + 25/60 + 38.24/3600, 28 + 35/60 + 6.75/3600),
    ("BdTR9G", 39 + 45/60 + 34.18/3600, 29 + 40/60 + 40.96/3600)
]


# data
names, latitudes, longitudes = zip(*data)

# map construction
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([25, 50, 30, 50])  # map range

ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.LAKES, edgecolor='black')
ax.add_feature(cfeature.RIVERS)

# plot
sc = ax.scatter(longitudes, latitudes, color='orange', marker='o')

# graph output
plt.title('Bd21 in Turkey')
plt.legend()
plt.show()




