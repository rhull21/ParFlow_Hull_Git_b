# Experimenting with Python Integration into ParFlow
# From Garrett's Presentation Recently 
# Initiated 09282020 

# ----------------------------------------------------------------------------------------------------------------------
# Outline
# ----------------------------------------------------------------------------------------------------------------------

# 0) Set up and General
# 1) Water Table <- use combo of saturation index to find saturated depth, and pressure profile to find the depth of water within the cell.
# 2) Total Storage <- saturation x porosity
# 3) Time Series <- over time
# 4) Surface Water <- Mask, or translate pressure to water depth over area


# %%
# ----------------------------------------------------------------------------------------------------------------------
# 0) Setup and general
# ----------------------------------------------------------------------------------------------------------------------
from parflow import Run
from parflow.tools.fs import get_absolute_path
from parflowio.pyParflowio import PFData
import numpy as np


# %%
