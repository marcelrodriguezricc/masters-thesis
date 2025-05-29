# Packages
import numpy as np # Numpy
import matplotlib.pyplot as plt # Plotting
import getpass # API keys
import xarray as xr # Data handling
import cartopy.crs as ccrs # Coordinate reference system
import cartopy.feature as cfeature # Map features
import copernicusmarine # Copernicus Marine Services Python API
import cmocean # Oceanography colormaps

# Load Copernicus daily mean datasets
thetao_ds = copernicusmarine.open_dataset(dataset_id="cmems_mod_glo_phy-thetao_anfc_0.083deg_P1D-m") # Temperature
so_ds = copernicusmarine.open_dataset(dataset_id="cmems_mod_glo_phy-so_anfc_0.083deg_P1D-m") # Salinity
zos_ds = copernicusmarine.open_dataset(dataset_id="cmems_mod_glo_phy_anfc_0.083deg_P1D-m") # Physical

# Set latitudinal and longitudinal bounds
lat_bounds = slice(15.0, 65.0)
lon_bounds = slice(-145.0, -112.0)
time_coord = '2025-06-06'

# Temperature
thetao_subset = thetao_ds['thetao'].sel(
    time=time_coord,
    latitude=lat_bounds,
    longitude=lon_bounds
    ).isel(depth=0)

# Salinity
salinity_subset = so_ds['so'].sel(
    time=time_coord,
    latitude=lat_bounds,
    longitude=lon_bounds
).isel(depth=0)

# Sea surface height
zos_subset = zos_ds['zos'].sel(
    time=time_coord,
    latitude=lat_bounds,
    longitude=lon_bounds
)

# Setup figure and axes
fig, axs = plt.subplots(
    1, 3,
    figsize=(18, 8),
    subplot_kw={'projection': ccrs.PlateCarree()}
)

# Subset variables
data_dict = {
    "Sea Surface Temperature (°C)": (thetao_subset, cmocean.cm.thermal),
    "Sea Surface Salinity (psu)": (salinity_subset, cmocean.cm.haline),
    "Sea Surface Height (m)": (zos_subset, cmocean.cm.delta)
}

# Generate plots
for ax, (title, (data, cmap)) in zip(axs, data_dict.items()): # For each subset...

    # Add map features
    ax.set_extent([-145, -112, 15, 65], crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND, facecolor='lightgray', zorder=0)
    ax.add_feature(cfeature.COASTLINE, linewidth=0.8)
    ax.add_feature(cfeature.BORDERS, linestyle=':', linewidth=0.5)
    ax.add_feature(cfeature.LAKES, facecolor='lightblue', alpha=0.5)
    ax.add_feature(cfeature.RIVERS, edgecolor='blue', alpha=0.3)

    # Extract and plot data
    lon = data.longitude.values
    lat = data.latitude.values
    values = data.values
    img = ax.imshow(
        values,
        extent=[lon.min(), lon.max(), lat.min(), lat.max()],
        origin='lower',
        transform=ccrs.PlateCarree(),
        cmap=cmap,
        interpolation='bilinear',
        aspect='auto'
    )

    # Title and colorbar
    ax.set_title(title, fontsize=14)
    cbar = plt.colorbar(img, ax=ax, orientation='vertical', shrink=0.7, pad=0.04)
    cbar.ax.tick_params(labelsize=8)

# Plot params
plt.rcParams['font.family'] = 'Helvetica'
plt.tight_layout()

# Save figure and show
plt.savefig("maps/cmems-thetao-so-zos.png", dpi=300, bbox_inches='tight')
plt.show()