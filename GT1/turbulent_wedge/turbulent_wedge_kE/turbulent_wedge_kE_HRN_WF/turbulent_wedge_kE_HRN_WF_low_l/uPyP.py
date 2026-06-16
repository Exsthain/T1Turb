import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# parameters
rho = 1 
nu = 2e-03
R = 0.1  # wall position

dfTan = pd.read_csv("postProcessing/surfacesDict0/1000/wall.xy", header=None, sep=r'\s+', skiprows=1)

# cf = shearStress / (.5 * rho * U**2) using vector magnitude
cf = np.sqrt(dfTan.iloc[:, 6]**2 + dfTan.iloc[:, 7]**2 + dfTan.iloc[:, 8]**2) / (.5 * rho * 1**2)

dfNor = pd.read_csv("postProcessing/sampleDict0/1000/profile0.xy", header=None, sep=r'\s+', skiprows=1)

# get wall shear stress at wall closest to profile x-coordinate (profile is at x=7.996, closest is index -1)
tW = np.sqrt(dfTan.iloc[-1, 6]**2 + dfTan.iloc[-1, 7]**2 + dfTan.iloc[-1, 8]**2)
u_tau = np.sqrt(tW / rho)

print("tW:", tW)

# y_dist is distance from wall (R - r)
y_dist = R - dfNor.iloc[:, 0]
yP = y_dist * u_tau / nu

print("yP:", yP.values)

uP = np.sqrt(dfNor.iloc[:, 1]**2 + dfNor.iloc[:, 2]**2 + dfNor.iloc[:, 3]**2) / u_tau

plt.plot(yP, uP)
plt.xscale('log')
plt.xlabel('y+')
plt.ylabel('u+')
plt.title('Dimensionless Velocity Profile')
plt.savefig('uPyP.png')
plt.close()

plt.plot(dfTan.iloc[:, 0], cf)
plt.xlabel('x')
plt.ylabel('Cf')
plt.title('Dimensionless Shear Stress')
plt.savefig('shear_stress.png')
plt.close()
