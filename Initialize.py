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

# ZONE PROPERTIES
# 1
a1 = 0.067
gamma_1 = 0.1076
# 2
a2 = 0.183
gamma_2 = 0.2277
# 3
a3 = 0.25
gamma_3 = 0.3045
# 4
a4 = 0.25
gamma_4 = 0.3045
# 5
a5 = 0.183
gamma_5 = 0.2277
# 6
a6 = 0.067
gamma_6 = 0.1076

# INTRA-ZONAL EXCHANGES
# boundary 12 (60deg S)
L12 = 2.0015*10^7 # boundary length [m]
k12 = 1*10^7 # thermal exchange coefficient [W/mK]
# boundary 23 (30deg S)
L23 = 3.4667*10^7
k23 = 1*10^7
# boundary 34 (0deg)
L34 = 4.003*10^7
k34 = 1*10^7
# boundary 45
L45 = 3.4667*10^7
k45 = 5*10^7
# boundary 56
L56 = 2.0015*10^7
k56 = 1*10^7