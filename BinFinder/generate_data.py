import pandas as pd

from generate_csv import generate_csv
from config import *



df = pd.read_csv(r"data/dummy_data.csv")

# From Config
sg_coords = (min_lat, min_lon, max_lat, max_lon)
sg_grid = (lat_grid, lon_grid)

generate_csv(df, sg_coords, sg_grid)