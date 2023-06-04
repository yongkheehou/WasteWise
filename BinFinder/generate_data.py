import pandas as pd

from generate_csv import generate_csv
from config import *





if __name__ == "__main__":
    # From Config
    sg_coords = (min_lat, min_lon, max_lat, max_lon)
    sg_grid = (lat_grid, lon_grid)

    df = pd.read_csv(r"data\raw_recycling_bin.csv")
    generate_csv(df, sg_coords, sg_grid, csv_path=r"data\final_recycling_bin.csv")

    df = pd.read_csv(r"data\raw_second_hand_goods.csv")
    generate_csv(df, sg_coords, sg_grid, csv_path=r"data\final_second_hand_goods.csv")

    df = pd.read_csv(r"data\raw_e_waste.csv")
    generate_csv(df, sg_coords, sg_grid, csv_path=r"data\final_e_waste.csv")
    