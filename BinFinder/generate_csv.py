import pandas as pd
import os

from config import *
from square_utils import *


def generate_dataframe(dataframe, square_centre_lat_list, square_centre_lon_list):
    """Given a dataframe containing the data, return a dictionary"""
    square_lat_list = list()
    square_lon_list = list()
    for idx in dataframe.index:
        lat = dataframe['lat'][idx]
        lon = dataframe['lon'][idx]
        square_lat = find_square_lat(lat, square_centre_lat_list)
        square_lon = find_square_lon(lon, square_centre_lon_list)
        square_lat_list.append(square_lat)
        square_lon_list.append(square_lon)

    dataframe['square_lat'] = square_lat_list
    dataframe['square_lon'] = square_lon_list
    return dataframe


def generate_csv(dataframe, bbox_lat_lon_coordinates, grid_dimensions, csv_path=r"data\bins.csv"):
    square_centre_lat_list, square_centre_lon_list = generate_square_centres(*bbox_lat_lon_coordinates, *grid_dimensions)
    dataframe = generate_dataframe(dataframe, square_centre_lat_list, square_centre_lon_list)
    dataframe.to_csv(csv_path)

if __name__ == "__main__":
    df = pd.read_csv(r"data\dummy_data.csv")

    # From Config
    sg_coords = (min_lat, min_lon, max_lat, max_lon)
    sg_grid = (lat_grid, lon_grid)

    generate_csv(df, sg_coords, sg_grid)
