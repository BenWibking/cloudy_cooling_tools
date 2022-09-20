from cloudy_grids import convert_cooling_tables

# does not work if there are missing table entries due to Cloudy crashes
convert_cooling_tables("./isrf_grains/isrf_ism.run", "isrf_grains.h5")

#convert_cooling_tables("./isrf_nograins/isrf_ism.run", "isrf_nograins.h5")
