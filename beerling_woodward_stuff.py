#!/usr/bin/env python

"""
Me messing about...

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (07.09.2022)"
__email__ = "mdekauwe@gmail.com"

from math import log
import matplotlib.pyplot as plt
import numpy as np
import sys
import math
from quadratic import quadratic

def solve_ci(g, Ko, Kc, Ca, o):
    # Equation 2.12  - write some comments martin

    a = -g * Ko
    b = (g * Ca * Ko) - (g * Ko * Kc) - (g * o * Kc) - (Ko * Vcmax)
    c = (g * Ca * Ko * Kc) + (g * Ca * o * Kc) + (Vomax * o * Kc / 2)

    Ci = quadratic(a=a, b=b, c=c, large=False) # postitive root

    return Ci

def solve_delta13c(Ci, Ca):

    a = 4.4 # discrimination against 13C due to diffusion in air
    b = 27 # discrimination of between 27 and 30%o against 12Co2 by rubisco
    delta_13Ca = -7. # parts per thousand (%o)
    delta_13Cp = delta_13Ca - a - (b - a) * (Ci / Ca)

    return delta_13Cp

# Chp2: Solution for Ci (based on eqn 2.12), given knowledge of stomtal conductance
Ca = 3500 # umol mol-1
g = 0.005 # at 3500 ppm
Vcmax = 50 # umol m-2 s-1
Vomax = 26 # umol m-2 s-1
o = 260 # uM with an external ambient O2 conc of 21%
Kc = 200 # uM at 350 ppm ish
Ko = 500 # range 360 uM to 650

Ci = solve_ci(g, Ko, Kc, Ca, o)
print(Ci, Ci/Ca)



# Solve delta 13
delta_13Cp = solve_delta13c(Ci, Ca)
print(delta_13Cp)

Ca = 350
g = 0.204 # at 350 ppm
Vcmax = 50
Vomax = 26
o = 260 # uM with an external ambient O2 conc of 21%
Kc = 200 # uM at 350 ppm ish
Ko = 500 # range 360 uM to 650

a = -g * Ko
b = (g * Ca * Ko) - (g * Ko * Kc) - (g * o * Kc) - (Ko * Vcmax)
c = (g * Ca * Ko * Kc) + (g * Ca * o * Kc) + (Vomax * o * Kc / 2)

Ci = quadratic(a=a, b=b, c=c, large=False) # postitive root
print(Ci, Ci/Ca)

delta_13Cp = solve_delta13c(Ci, Ca)
print(delta_13Cp)



Ca = 3500
g = 0.005 # at 3500 ppm
Vcmax = 6
Vomax = 3
o = 260 # uM with an external ambient O2 conc of 21%
Kc = 200 # uM at 350 ppm ish
Ko = 500 # range 360 uM to 650

Ci = solve_ci(g, Ko, Kc, Ca, o)
print(Ci, Ci/Ca)


a = 4.4 # discrimination against 13C due to diffusion in air
b = 27 # discrimination of between 27 and 30%o against 12Co2 by rubisco
delta_13Ca = -7. # parts per thousand (%o)
delta_13Cp = delta_13Ca - a - (b - a) * (Ci / Ca)

print(delta_13Cp)

x = np.array([-500, -450, -400, -350, -340, -330, -300, -300, -280, -250, \
              -225, -200, -100, -50, 0])
co2 = np.array([4900, 5000, 4000, 3000, 2000, 1000, 500, 490,  500, \
                1000, 1400, 1300, 900, 500, 300])
Ci = np.zeros(len(co2))


""" This is obv wrong, Vcmax needs to time varying, just looking
g = 0.204 # at 350 ppm
Vcmax = 50
Vomax = 26
o = 260 # uM with an external ambient O2 conc of 21%
Kc = 200 # uM at 350 ppm ish
Ko = 500 # range 360 uM to 650

for i, Ca in enumerate(co2):

    if x[i] < -350:
        Vcmax = 5
    elif x[i] >= -350 and x[i] <-250:
        Vcmax = 100
    elif x[i] >= -250 and x[i] <-50:
        Vcmax = 50
    a = -g * Ko
    b = (g * Ca * Ko) - (g * Ko * Kc) - (g * o * Kc) - (Ko * Vcmax)
    c = (g * Ca * Ko * Kc) + (g * Ca * o * Kc) + (Vomax * o * Kc / 2)

    Ci[i] = quadratic(a=a, b=b, c=c, large=False) # postitive root
plt.plot(x, Ci/co2)
plt.show()

sys.exit()
"""

sc = 1367
albedo = 0.31
deg2kelvin = 273.15

Ts = ((sc / 4 * (1 - albedo)) + 212) / 1.55

print(Ts, Ts - deg2kelvin)

c = 5000 - 280
Ts = ((sc / 4 * (1 - albedo)) + (6.3 * log((280 + c) / 280)) +  212) / 1.55

print(Ts, Ts - deg2kelvin)

c = 350 - 280
Ts = ((sc / 4 * (1 - albedo)) + (6.3 * log((280 + c) / 280)) +  212) / 1.55

print(Ts, Ts - deg2kelvin)


co2 = np.array([4900, 5000, 4000, 3000, 2000, 500, 400, 400,  400, \
                1000, 1300, 1200, 900, 500, 300])
x = np.array([-500, -450, -400, -350, -340, -330, -300, -300, -280, -250, \
              -225, -200, -100, -50, 0])
plt.plot(x, co2)
plt.show()

c = co2 - 280

l = 1.0
Ts = ((sc * l / 4 * (1 - albedo)) + (6.3 * np.log((280 + c) / 280)) +  212) / 1.55

plt.plot(x, Ts, label="sL = 1")

l = 0.98
Ts = ((sc * l / 4 * (1 - albedo)) + (6.3 * np.log((280 + c) / 280)) +  212) / 1.55

#
plt.plot(x, Ts)


plt.legend(numpoints=1, loc="best")
plt.ylim(280, 305)
plt.show()

ca = co2

ci = ca * 0.7

delta = (4.4 + 22.6 * ci/ca) * 10**-3

plt.plot(x, delta*1000)
plt.show()


co2_pa = co2 * 101.325/ 1000
Sc = 600 * np.exp(-0.02*co2_pa) + 10

plt.plot(x, Sc)
plt.show()

mol_2_mmol = 1000
mm2_2_m2 = 1e-6
mu_m_2_m = 1e-6
#D = 2.42E-5 # might be wrong @ 20 deg, m2 s-1
P = 101325 # Pa
ds = 15 * mu_m_2_m#uM
l = 10 * mu_m_2_m # uM
RH = 80
w = 7 * mu_m_2_m # uM
R = 8.31432 #J⋅K−1⋅mol−1


tc = Ts - deg2kelvin
Ww = w * np.exp(-0.003 * (614 * np.exp( (17.5 * tc) / (241 + tc) ) ) * (1 - RH / 100))

arg1 = 0.37 - 5.7 * 10**-4 * tc**2 + 3.4510**-2 * tc
arg2 = 1 - 0.116 * np.log(co2_pa * 10)
Wt = Ww * arg1 * arg2

Cm = P / (R * Ts)

D = 2.42 * 10**-5 * (Ts / 293)**1.75 * 101325 / P #m-2 s-1

num = 10**12 * (Sc * mm2_2_m2) * D * Cm

#den = ( (ds / (np.pi * l * w)) + (np.log(4 * l / w) / (np.pi * l)) )

#g = num / den

#plt.plot(x, g * mol_2_mmol, label="fixed width")

den = ( (ds / (np.pi * l * Ww)) + (np.log(4 * l / Ww) / (np.pi * l)) )

g = num / den

#plt.plot(x, g * mol_2_mmol, label="temp")

den = ( (ds / (np.pi * l * Wt)) + (np.log(4 * l / Wt) / (np.pi * l)) )

g = num / den

plt.plot(x, g * mol_2_mmol, label="co2 and temp")
plt.legend(numpoints=1, loc="best")
plt.show()





mol_2_mmol = 1000
mm2_2_m2 = 1e-6
mu_m_2_m = 1e-6
#D = 2.42E-5 # might be wrong @ 20 deg, m2 s-1
P = 101325 # Pa
ds = 15 * mu_m_2_m#uM
l = 10 * mu_m_2_m # uM
RH = 80
w = 7 * mu_m_2_m # uM
R = 8.31432 #J⋅K−1⋅mol−1

ca_pa = co2 * 101.325/ 1000


tc = Ts - deg2kelvin
Ww = w * np.exp(-0.003 * (614 * np.exp( (17.5 * tc) / (241 + tc) ) ) * (1 - RH / 100))

arg1 = 0.37 - 5.7 * 10**-4 * tc**2 + 3.4510**-2 * tc
arg2 = 1 - 0.116 * np.log(ca_pa * 10)
Wt = Ww * arg1 * arg2

Cm = P / (R * Ts)

num = 10**12 * (Sc * mm2_2_m2) * D * Cm
den = ( (ds / (np.pi * l * Wt)) + (np.log(4 * l / Wt) / (np.pi * l)) )

g = num / den


Ci = np.zeros(len(co2))

Vcmax = 50
Vomax = 26
o = 260 # uM with an external ambient O2 conc of 21%
Kc = 200 # uM at 350 ppm ish
Ko = 500 # range 360 uM to 650

for i, Ca in enumerate(co2):


    a = -g[i] * Ko
    b = (g[i] * Ca * Ko) - (g[i] * Ko * Kc) - (g[i] * o * Kc) - (Ko * Vcmax)
    c = (g[i] * Ca * Ko * Kc) + (g[i] * Ca * o * Kc) + (Vomax * o * Kc / 2)

    Ci[i] = quadratic(a=a, b=b, c=c, large=False) # postitive root
plt.plot(x, Ci/Ca)
plt.show()
