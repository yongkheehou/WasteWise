import pandas as pd
from geopy.distance import geodesic

from .square_utils import *
from .config import *


class BinFinder():
    def __init__(self):
        # Initialise the data frame and grids here
        self.recycling_bin_data = pd.read_csv(r"BinFinder/data/final_recycling_bin.csv")
        self.second_hand_goods_data = pd.read_csv(r"BinFinder/data/final_second_hand_goods.csv")
        self.e_waste_bin_data = pd.read_csv(r"BinFinder/data/final_e_waste.csv")

        self.type_dict = {
            "recycling": self.recycling_bin_data,
            "second_hand": self.second_hand_goods_data,
            "e_waste": self.e_waste_bin_data
        }

        self.square_centre_lat_list, self.square_centre_lon_list = generate_square_centres(min_lat, min_lon, max_lat, max_lon, lat_grid, lon_grid)

    def find_k_nearest_bins(self, user_coordinates, k, type):
        if type not in self.type_dict:
            return {
                "data": f"Type {type} does not exist! Valid: {self.type_dict.keys()}"
            }

        user_lat, user_lon = user_coordinates
        square_lat = find_square_lat(user_lat, self.square_centre_lat_list)
        square_lon = find_square_lon(user_lon, self.square_centre_lon_list)
        all_squares_list = all_nearest_squares(user_coordinates, self.square_centre_lat_list, self.square_centre_lon_list)

        bins = list()
        square_idx = 0
        while len(bins) < k and square_idx < len(all_squares_list):
            square_lat, square_lon = all_squares_list[square_idx]
            data = self.get_data_at_square(square_lat, square_lon, type)
            for idx in data.index:
                lat = data["lat"][idx]
                lon = data["lon"][idx]
                distance = geodesic(user_coordinates, (lat, lon)).km
                
                bin_dictionary = {
                    "coordinates": (lat, lon),
                    "distance from user": distance,
                    "address": data["address"][idx],
                    "description": data["description"][idx],
                    "postal_code": data["postal_code"][idx].item()
                }
                bins.append(bin_dictionary)
            square_idx += 1

        bins.sort(key=lambda x:x["distance from user"])

        if len(bins) < k:
            return bins
        else:
            return bins[:k] 

    def get_data_at_square(self, square_lat_id, square_lon_id, type):
        dataframe = self.type_dict[type]
        condition1 = dataframe['square_lat'] == square_lat_id
        condition2 = dataframe["square_lon"] == square_lon_id
        all_conditions = condition1 & condition2
        new_df = dataframe.loc[all_conditions]
        return new_df


if __name__ == "__main__":
    bf = BinFinder()
    b = bf.find_k_nearest_bins((1.3413321170109964, 103.76839921820817), 2)
    print(b)
