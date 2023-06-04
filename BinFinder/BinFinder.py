import pandas as pd
from geopy.distance import geodesic

from .square_utils import *
from .config import *


class BinFinder():
    def __init__(self):
        # Initialise the data frame and grids here
        self.data = pd.read_csv(r"BinFinder/data/bins.csv")
        self.square_centre_lat_list, self.square_centre_lon_list = generate_square_centres(min_lat, min_lon, max_lat, max_lon, lat_grid, lon_grid)

    def find_k_nearest_bins(self, user_coordinates, k):
        print(user_coordinates, k)
        user_lat, user_lon = user_coordinates
        square_lat = find_square_lat(user_lat, self.square_centre_lat_list)
        square_lon = find_square_lat(user_lon, self.square_centre_lon_list)
        data = self.get_data_at_square(square_lat, square_lon)

        bins = list()
        for idx in data.index:
            lat = data["lat"][idx]
            lon = data["lon"][idx]
            distance = geodesic(user_coordinates, (lat, lon)).km
            
            bin_dictionary = {
                "coordinates": (lat, lon),
                "distance from user": distance,
                "name": data["name"][idx],
                "address": data["address"][idx],
                "description": data["description"][idx],
                "postal_code": data["postal_code"][idx].item()
            }

            bins.append(bin_dictionary)

        bins.sort(key=lambda x:x["distance from user"])

        if len(bins) < k:
            return bins
        else:
            return bins[:k] 

    def get_data_at_square(self, square_lat_id, square_lon_id):
        condition1 = self.data['square_lat'] == square_lat_id
        condition2 = self.data["square_lon"] == square_lon_id
        all_conditions = condition1 & condition2
        new_df = self.data.loc[all_conditions]
        return new_df


if __name__ == "__main__":
    bf = BinFinder()
    b = bf.find_k_nearest_bins((1.3413321170109964, 103.76839921820817), 2)
    print(b)
