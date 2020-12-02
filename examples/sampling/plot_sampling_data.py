"""
Sampling data from a 3D model
=============================
"""
###############################################################################
# First, load the required modules.
from psipy.model import MASOutput
import astropy.constants as const
import astropy.units as u

import matplotlib.pyplot as plt
import numpy as np

###############################################################################
# Load a set of MAS output files.
mas_path = '/Users/dstansby/github/psipy/data/helio'
model = MASOutput(mas_path)

###############################################################################
# Get the number density variable from the model run
rho = model['rho']

###############################################################################
# Choose a set of 1D points to interpolate the model output at.
#
# Here we keep a constant radius, and a set of longitudes that go all the way
# from 0 to 360 degrees. Then we choose two different, but close latitude
# values, and plot the results.
fig, ax = plt.subplots()

npoints = 1000
r = 50 * np.ones(npoints) * const.R_sun
lon = np.linspace(0, 360, npoints) * u.deg

for latitude in [0, 1] * u.deg:
    lat = latitude * np.ones(npoints)
    samples = rho.sample_at_coords(lon, lat, r)

    ax.plot(lon, samples, label='lat = ' + str(latitude))

ax.legend()
ax.set_xlim(0, 360)
ax.set_xlabel('Longitude (deg)')
ax.set_ylabel(r'$\rho$ (cm$^{-3}$)')
plt.show()
