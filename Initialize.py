import numpy as np

## INITIALIZES VALUE TO USE IN SOLVING RADIATIVE ENERGY BALANCE MODEL

# MODEL PARAMETERS
SIGMA_B = 5.6696*10^(-8) # Stefan-Boltzmann constant [W/m^2K^4]
S0 = 1368 # solar constant [W/m^2]
RE = 6371*10^3 # radius of Earth [m]
AE = np.pi*RE^2 # surface area of Earth [m^2]
EPS = 1 # total emissivity of Earth (= 1 -> ideal black body)
TAU = 0.63 # atmospheric transmissivity
ALPHA_SKY = 0.2 # atmospheric albedo
ALPHA_LS = 0.4 # land surface albedo
ALPHA_OS = 0.1 # ocean surface albedo
ALPHA_ICE = 0.6 # ice albedo
RHO_LS = 2500 # density of land surface [kg/m^3]
RHO_OW = 1028 # density of ocean water [kg/m^3]
RHO_ICE = 900 # density of ice [kg/m^3]
Z_S = 1 # thermal scale depth for land [m]
Z_W = 70 # thermal scale depth for ocean [m]
Z_ICE = 1 # thermal scale depth for ice [m]
C_S = 790 # specific heat capacity for land [J*kg/K]
C_W = 4187 # specific heat capacity for water [J*kg/K]
C_I = 2060 # specific heat capacity for ice [J*kg/K]

