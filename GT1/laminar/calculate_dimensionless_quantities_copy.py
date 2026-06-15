import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#cf = shearStress / (.5 * rho * U**2)
#rho = 1 
#U = 1  
#wall.xy - col 0 = x, col 1 = y, col 2 = z, col 3 = ux, col 4 = uy, col 5 = uz, col 6 = tau_wall_x, col 7 = tau_wall_y, col 8 = tau_wall_z, col 9 = y+
#nu = 2e-03

dfTan = pd.read_csv("postProcessing/surfacesDict0/1000/wall.xy", header=None, sep='\\s+', skiprows=1)

cf = dfTan.iloc[:, 6] / (.5 * 1 * 1**2) # shearStress / (.5 * rho * U**2)

dfNor = pd.read_csv("postProcessing/sampleDict0/1000/profile0.xy", header=None, sep='\\s+', skiprows=1)
#col 0 = dist, col 1 = uX, col 2 = uY, col 3 = uZ,, col 4 = p
#y+ = U * y / nu


dfNor.iloc[:, 1] = dfNor.iloc[:, 1].values[::-1]  # reversed because the velocity profile is from the wall to the center, and we want it from the center to the wall

tW = np.sqrt((dfNor.iloc[28,5])**2 + (dfNor.iloc[28,6])**2 + (dfNor.iloc[28,7])**2)

print(tW)

yP = dfNor.iloc[:, 0] * np.sqrt(tW)/ 2e-03

print(yP)


uP = np.sqrt(dfNor.iloc[:, 1]**2 + dfNor.iloc[:, 2]**2 + dfNor.iloc[:, 3]**2) / np.sqrt(tW)


plt.plot(yP, uP)
#plt.xscale('log')
plt.xlabel('y+')
plt.ylabel('u+')
plt.title('Dimensionless Velocity Profile')
plt.show()




plt.plot(dfTan.iloc[:, 0], cf)
plt.xlabel('x')
plt.ylabel('Cf')
plt.title('Dimensionless Shear Stress')
plt.show()
