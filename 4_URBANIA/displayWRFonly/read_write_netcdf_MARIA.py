#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import xarray as xr
from netCDF4 import Dataset
from netCDF4 import date2num #, num2date
from datetime import datetime, timedelta

filename = 'xy.nc'
savename = 'cf-conform.nc'


# read in netcdf as xarray dataset
ds = xr.open_dataset(filename)

# parameter to read and write
param = 'pr'

# read latitude and longitude from dataset
lat1d = ds['lat']
lon1d = ds['lon']

# define startdate of data
startdate = datetime(2010,1,1)

# save dataset as CF-conform netcdf file

# open new netCDF file in write mode:        
dataset = Dataset(savename,'w',format='NETCDF4_CLASSIC')

# create dimensions
time = dataset.createDimension("time",None) # None: unlimited dimension
lat = dataset.createDimension("lat", len(lat1d))
lon = dataset.createDimension("lon",len(lon1d))
#bnds = dataset.createDimension("bnds",2)

# create variables
times = dataset.createVariable("time","f8",("time",), zlib=True)
lats = dataset.createVariable("lat","f4",("lat",), zlib=True, fill_value = -9999)
lons = dataset.createVariable("lon","f4",("lon",), zlib=True, fill_value = -9999)
#time_bnds = dataset.createVariable("time_bnds", "f4",("time","bnds"))
var = dataset.createVariable(param, "f4", ("time","lat","lon",), zlib=True, fill_value = -9999)
crs = dataset.createVariable('crs', 'c', ()) # projection information

# add attributes
times.units = 'days since 1950-01-01T00:00:00Z'
times.calendar = 'standard'     # use calendar from original file!
#times.bounds = 'time_bnds'
times.standard_name = 'time'
times.long_name = 'time'
times.axis = 'T'

lats.units = 'degrees_north'
lats.long_name = 'latitude'
lats.standard_name = 'latitude'

lons.units = 'degrees_east'
lons.long_name = 'longitude'
lons.standard_name = 'longitude'

if param == 'pr':
    var.units = 'mm'
    var.long_name = 'total daily precipitation'
    var.stnadard_nbame = 'precipitation amount'
    dataset.title='Total daily precipitation'
    dataset.comment='Total daily precipitation bias corrected (scaled distribution mapping) data of the EURO-CORDEX model. The reference period is 1981-2010, the years 2006-2010 are taken from the corresponding rcp4.5 scenario.'
    #var[:] = var_array
    
elif param == 'tasmax':
    var.units = 'degree_Celsius'
    var.long_name = 'daily maximum near-surface air temperature'
    var.standard_name = 'air_temperature'
    dataset.title='Daily maximum near-surface air temperature'
    dataset.comment='Daily maximum near-surface air temperature bias corrected (scaled distribution mapping) data of the EURO-CORDEX model. The reference period is 1981-2010, the years 2006-2010 are taken from the corresponding rcp4.5 scenario.'
    
elif param == 'tasmin':
    var.units = 'degree_Celsius'
    var.long_name = 'daily minimum near-surface air temperature'
    var.standard_name = 'air_temperature'       
    dataset.title='Daily minimum near-surface air temperature'
    dataset.comment='Daily minimum near-surface air temperature bias corrected (scaled distribution mapping) data of the EURO-CORDEX model. The reference period is 1981-2010, the years 2006-2010 are taken from the corresponding rcp4.5 scenario.'
    
elif param == 'rsds':
    var.units = 'W m-2'
    var.long_name = 'surface downwelling shortwave flux'
    var.standard_name = 'surface_downwelling_shortwave_flux_in_air'       
    dataset.title='Daily global radiation'
    dataset.comment='Daily global radiation bias corrected (scaled distribution mapping) data of the EURO-CORDEX model. The reference period is 1981-2010, the years 2006-2010 are taken from the corresponding rcp4.5 scenario.'
    
var.grid_mapping = 'latitude_longitude'

# projection information
crs.longitude_of_prime_meridian = 0.0 
crs.semi_major_axis = 6378137.0
crs.inverse_flattening = 298.257223563
crs.comment = 'Latitude and longitude on the WGS 1984 datum'

# write data to netCDF variable
var[:] = ds[param].data
lats[:] = lat1d
lons[:] = lon1d

# fill in times
dates = [startdate+k*timedelta(days=1) for k in range(ds[param].data.shape[0])]
times[:] = date2num(dates, units=times.units, calendar=times.calendar)

# global attributes

dataset.project= "Climaproof, funded by the Austrian Development Agency (ADA) and co-funded by the United Nations Environmental Programme (UNEP)"
dataset.source = 'Bias Correction Method: Switanek et al., 2017, doi.org/10.5194/hess-21-2649-2017, Regridding Method: Higher-order patch recovery (patch) by Earth System Modelling Framework (ESMF) software ESMF_RegridWeightGen (http://www.earthsystemmodeling.org/esmf_releases/public/last/ESMF_refdoc/)'
dataset.contact = 'Maria Wind <maria.wind@boku.ac.at>, Herbert Formayer <herbert.formayer@boku.ac.at>'
dataset.institution = 'Institute of Meteorology, University of Natural Resources and Life Sciences, Vienna, Austria'
dataset.referencees = 'https://data.ccca.ac.at/group/climaproof'
dataset.conventions = 'CF-1.6'

# close dataset        
dataset.close()