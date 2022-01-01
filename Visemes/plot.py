from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

xOut = [0.0, -0.965, -2.37, -3.7950000000000004, -2.3583333333333334, 0.0, 2.3583333333333334, 3.7950000000000004, 2.37, 0.965, 0.0]
yOut = [1.3425000000000002, 1.6058333333333334, 1.2058333333333335, 0.13083333333333333, -1.5233333333333334, -2.32, -1.5233333333333334, 0.13083333333333333, 1.2058333333333335, 1.6058333333333334, 1.3425000000000002]
tck,u     = interpolate.splprep( [xOut,yOut] ,s = 0 )
xnew,ynew = interpolate.splev( np.linspace( 0, 1, 100 ), tck,der = 0)
plt.plot(xOut ,yOut ,'o' , xnew ,ynew )


xIn = [0.0, -0.8975, -1.7041666666666666, -0.7941666666666668, 0.0, 0.7941666666666668, 1.7041666666666666, 0.8975, 0.0]
yIn = [0.6375, 0.6566666666666667, 0.34416666666666673, 0.040833333333333346, -0.2, 0.040833333333333346, 0.34416666666666673, 0.6566666666666667, 0.6375]
tck,u     = interpolate.splprep( [xIn,yIn] ,s = 0 )
xnew,ynew = interpolate.splev( np.linspace( 0, 1, 100 ), tck,der = 0)
plt.plot(xIn ,yIn ,'o' , xnew ,ynew )

plt.show()

