
from pprint import pprint  # For pretty printing
import noaa_coops as nc
seattle = nc.Station(9447130)
pprint(seattle.lat_lon['lat'])
pprint(seattle.lat_lon['lon'])

df_water_levels = seattle.get_data(
    begin_date="20150101",
    end_date="20150331",
    product="water_level",
    datum="MLLW",
    units="metric",
    time_zone="gmt")

df_water_levels.head()  # doctest: +NORMALIZE_WHITESPACE