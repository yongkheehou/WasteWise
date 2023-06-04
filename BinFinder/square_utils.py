from geopy.distance import geodesic


def generate_square_centres(min_lat, min_lon, max_lat, max_lon, num_lat_squares, num_lon_squares):
    """Takes in the max and min lat and lon coordinates surrounding a region
    and divides into specified number of grids.

    Returns a list of the centre lat coordinates and centre lon coordinates
    of the grids.
    """
    sg_centre_lat = (max_lat + min_lat) / 2
    sg_centre_lon = (max_lon + min_lon) / 2

    # SG Lat and Lon distance
    sg_lat_dist = geodesic((min_lat, sg_centre_lon), (max_lat, sg_centre_lon)).km
    sg_lon_dist = geodesic((sg_centre_lat, min_lon), (sg_centre_lat, max_lon)).km
    print(f"Overall Map Size: {sg_lat_dist:.3f} km x {sg_lon_dist:.3f} km")

    # # SG Lat_unit and Lon_unit distance/km (approx based on restaurants)
    sg_lat_unit_dist = sg_lat_dist / num_lat_squares
    sg_lon_unit_dist = sg_lon_dist / num_lon_squares
    print(f"Grid Size: {sg_lat_unit_dist:.3f} km x {sg_lon_unit_dist:.3f} km")

    # Generate a list of centre coordinates
    lat_unit = (max_lat-min_lat) / num_lat_squares
    lon_unit = (max_lon-min_lon) / num_lon_squares
    lat_center = min_lat + lat_unit/2
    lon_center = min_lon + lon_unit/2

    square_centre_lat_list = [lat_center + (i * lat_unit) for i in range(num_lat_squares)]
    square_centre_lon_list = [lon_center + (i * lon_unit) for i in range(num_lon_squares)]

    return square_centre_lat_list, square_centre_lon_list


def find_square_lat(lat_input, square_centre_lat_list):
    lat = min(square_centre_lat_list, key=lambda x:abs(x-lat_input))
    return square_centre_lat_list.index(lat)


def find_square_lon(lon_input, square_centre_lon_list):
    lon = min(square_centre_lon_list, key=lambda x:abs(x-lon_input))
    return square_centre_lon_list.index(lon)


def all_nearest_squares(user_coordinates, square_centre_lat_list, square_centre_lon_list):
    all_squares = list()
    for lat in square_centre_lat_list:
        for lon in square_centre_lon_list:
            all_squares.append((lat, lon))

    all_squares.sort(key=lambda x: geodesic(user_coordinates, x))
    all_squares = [(find_square_lat(lat, square_centre_lat_list), 
                    find_square_lon(lon, square_centre_lon_list)) 
                   for (lat, lon) in all_squares]
    return all_squares
